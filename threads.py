import threading
import time

# Factorial function (recursive)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Thread function for factorial calculation
def factorial_thread(n):
    print(f"Calculating factorial of {n}\n", flush=True)
    result = factorial(n)
    print(f"Factorial of {n} is {result}\n", flush=True)

# Fibonacci function (recursive)
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Thread function for Fibonacci (recursive)
def fibonacci_recursive_thread(n):
    print(f"Calculating {n}th Fibonacci number (recursive)\n", flush=True)
    result = fibonacci_recursive(n)
    print(f"{n}th Fibonacci number (recursive) is {result}\n", flush=True)

# Fibonacci function (non-recursive for better performance)
def fibonacci_non_recursive(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Thread function for Fibonacci (non-recursive)
def fibonacci_non_recursive_thread(n):
    print(f"Generating Fibonacci series up to {n} (non-recursive)\n", flush=True)
    result = fibonacci_non_recursive(n)
    print(f"Fibonacci series up to {n} (non-recursive): {result}\n", flush=True)

# Main function to create threads
if __name__ == "__main__":
    # Get user input for n
    n = int(input("Enter a number (n) for factorial and Fibonacci calculations: "))

    # Create threads for each function
    factorial_thread_instance = threading.Thread(target=factorial_thread, args=(n,))
    fibonacci_recursive_thread_instance = threading.Thread(target=fibonacci_recursive_thread, args=(n,))
    fibonacci_non_recursive_thread_instance = threading.Thread(target=fibonacci_non_recursive_thread, args=(n,))

    # Start the threads
    factorial_thread_instance.start()
    fibonacci_recursive_thread_instance.start()
    fibonacci_non_recursive_thread_instance.start()

    # Wait for all threads to complete
    factorial_thread_instance.join()
    fibonacci_recursive_thread_instance.join()
    fibonacci_non_recursive_thread_instance.join()

    print("All threads have completed.")


