import threading
import time
import random
from queue import Queue

BUFFER_SIZE = 5

buffer = Queue(maxsize=BUFFER_SIZE)


def producer():
    while True:
        item = random.randint(1, 100)
        buffer.put(item)  
        print(f"Produced: {item}")
        time.sleep(random.uniform(0.1, 1)) 


def consumer():
    while True:
        item = buffer.get()  
        print(f"Consumed: {item}")
        buffer.task_done() 
        time.sleep(random.uniform(0.1, 1)) 


producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)


producer_thread.start()
consumer_thread.start()


producer_thread.join()
consumer_thread.join()
