from confluent_kafka import Consumer

def main():
    print("Starting consumer...")
    # Configure the consumer
    consumer_config = {
        'bootstrap.servers': 'redpanda-0:9092',  # Redpanda broker
        'group.id': 'my_consumer_group',       # Consumer group
        'auto.offset.reset': 'earliest',       # Start at the earliest message
    }
    consumer = Consumer(consumer_config)

    # Subscribe to the topic
    consumer.subscribe(['test'])

    print("Listening for messages...")
    while True:
        msg = consumer.poll(1.0)  # Poll for new messages
        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        print(f"Received: {msg.value().decode('utf-8')} from topic {msg.topic()}")


if __name__ == "__main__":
    main()
