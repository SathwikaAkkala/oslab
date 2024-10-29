import threading
import queue
import time
import random

# Buffer size for the queue
BUFFER_SIZE = 5

# Create a queue to represent the shared buffer
buffer = queue.Queue(BUFFER_SIZE)

# Producer function
def producer(produce_count):
    for _ in range(produce_count):
        item = random.randint(1, 100)  # Produce a random item
        buffer.put(item)  # Add item to the buffer
        print(f"Produced {item}. Buffer size: {buffer.qsize()}")
        time.sleep(random.uniform(0.5, 1.5))  # Simulate time taken to produce an item

# Consumer function
def consumer(consume_count):
    for _ in range(consume_count):
        item = buffer.get()  # Retrieve an item from the buffer
        print(f"Consumed {item}. Buffer size: {buffer.qsize()}")
        buffer.task_done()  # Indicate that the item has been processed
        time.sleep(random.uniform(0.5, 1.5))  # Simulate time taken to consume an item

# Main function to create and manage threads
if __name__ == "__main__":
    # Get user input for the number of items to produce and consume
    produce_count = int(input("Enter the number of items to produce: "))
    consume_count = int(input("Enter the number of items to consume: "))

    # Create producer and consumer threads
    producer_thread = threading.Thread(target=producer, args=(produce_count,))
    consumer_thread = threading.Thread(target=consumer, args=(consume_count,))

    # Start the threads
    producer_thread.start()
    consumer_thread.start()

    # Wait for both threads to complete
    producer_thread.join()
    consumer_thread.join()

    print("All items have been produced and consumed.")

