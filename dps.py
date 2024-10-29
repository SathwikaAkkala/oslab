import threading
import time
import random

# Class to represent a Philosopher
class Philosopher(threading.Thread):
    def __init__(self, id, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.id = id
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while True:
            # Thinking
            print(f"Philosopher {self.id} is thinking.")
            time.sleep(random.uniform(1, 3))  # Simulate thinking time

            # Hungry and trying to pick up forks
            print(f"Philosopher {self.id} is hungry.")
            first_fork, second_fork = (self.left_fork, self.right_fork) if self.id % 2 == 0 else (self.right_fork, self.left_fork)
            
            with first_fork:
                with second_fork:
                    # Eating
                    print(f"Philosopher {self.id} is eating.")
                    time.sleep(random.uniform(1, 3))  # Simulate eating time
                    print(f"Philosopher {self.id} has finished eating.")

# Main function to create philosophers
if __name__ == "__main__":
    # Get user input for the number of philosophers
    num_philosophers = int(input("Enter the number of philosophers: "))
    
    # Create forks (semaphores)
    forks = [threading.Semaphore(1) for _ in range(num_philosophers)]

    # Create and start philosophers
    philosophers = []
    for i in range(num_philosophers):
        philosopher = Philosopher(i, forks[i], forks[(i + 1) % num_philosophers])
        philosophers.append(philosopher)
        philosopher.start()

    # Join philosophers to prevent main program from exiting
    for philosopher in philosophers:
        philosopher.join()
