from fastapi import FastAPI, Body
from confluent_kafka import Producer
from confluent_kafka.admin import AdminClient, NewTopic

app = FastAPI()

# Configure the producer
producer_config = {
    'bootstrap.servers': 'redpanda-0:9092',  # Redpanda broker
}
producer = Producer(producer_config)

def delivery_report(err, msg):
    """ Delivery callback for confirmation """
    if err is not None:
        print(f"Delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

@app.post("/")
def read_root(message: str = Body(), topic: str = Body()):
    producer.produce(topic, key=str(message), value=message, callback=delivery_report)
    return {"message": "Message sent"}


@app.post("/create-topic")
def create_topic(message: str = Body()):
    admin_client = AdminClient({
        'bootstrap.servers': 'redpanda-0:9092'  # Replace with your Redpanda broker
    })
    # Define the topic to create
    new_topic = NewTopic(
        message,
        num_partitions=3,  # Number of partitions
        replication_factor=1  # Replication factor (Redpanda supports 1 in single-node setups)
    )

    # Attempt to create the topic
    try:
        futures = admin_client.create_topics([new_topic])
        for topic, future in futures.items():
            try:
                future.result()  # Block until the topic is created or an error is thrown
                print(f"Topic '{topic}' created successfully.")
            except Exception as e:
                print(f"Failed to create topic '{topic}': {e}")
    except Exception as e:
        print(f"Error creating topics: {e}")

    return {"message": "Topic created"}