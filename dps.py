import threading
import time
import random


NUM_PHILOSOPHERS = 5


forks = [threading.Semaphore(1) for _ in range(NUM_PHILOSOPHERS)]


def philosopher(i):
    while True:
        print(f"Philosopher {i} is thinking.")
        time.sleep(random.uniform(0.5, 1.5))
        
        print(f"Philosopher {i} is hungry.")
        
        
        left_fork = forks[i]
        right_fork = forks[(i + 1) % NUM_PHILOSOPHERS]

        with left_fork:
            with right_fork:
                print(f"Philosopher {i} is eating.")
                time.sleep(random.uniform(0.5, 1.5))  
        
        print(f"Philosopher {i} has finished eating.")


threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(NUM_PHILOSOPHERS)]


for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
