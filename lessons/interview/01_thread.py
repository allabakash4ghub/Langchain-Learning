"""
GIL (Global Interpreter Lock):GIL, which stands for Global Interpreter Lock, is a notorious mechanism in Python that acts as a strict "one-at-a-time" rule for execution.
Even if your computer has a powerful 8-core or 16-core processor, the GIL ensures that only one thread can execute Python code at any single moment (in a standard GIL-enabled CPython implementation).

Concurrency:
Concurrency is about dealing with lots of things at once, while parallelism is about doing lots of things at once.
It means making progress on multiple tasks over the same period of time.
Crucially, concurrency does not mean tasks are running at the exact same fraction of a second (that is parallelism).
It just means the computer is switching back and forth between tasks so fast that it looks like they are happening at the same time.

Multithreading:
Multithreading is a programming technique that allows multiple threads to exist within the context of a single process, sharing the process's resources but able to execute independently.
In Python, the operating system spins up multiple "threads" (workers).
When one thread gets blocked waiting for something (like waiting for a website to respond or a file to download), the computer automatically switches to another thread to do work.

Asyncio:
Asyncio is a library to write concurrent code using the async/await syntax.
With asyncio, you typically use one thread.
The program uses an Event Loop to manage tasks.
When a task hits a waiting point (like a network request), it explicitly says:
"I'm going to be waiting for a bit, go work on something else!"
It does this using the keywords async and await.

Multiprocessing:
Multiprocessing is a programming technique that allows multiple processes to run concurrently, each with its own Python interpreter and memory space.
This means that each process can run on a separate CPU core, allowing for true parallelism.

If you have CPU-intensive tasks, such as:
- Training machine learning models.
- Performing large mathematical calculations.
- Processing large datasets.
- Running computationally expensive Python functions.
Asyncio and traditional GIL-enabled multithreading are generally not the best solutions.

What exactly does GIL do?
GIL is a lock mechanism that allows only one thread at a time to execute Python bytecode within a given interpreter.

Important: The GIL does not mean only one thread exists. Multiple threads can exist and make progress, but they cannot execute Python bytecode simultaneously in the traditional GIL-enabled CPython interpreter.
Does GIL affect all operations?
Not equally.

Consider two types of operations:
Operation	Example	GIL impact
CPU-bound	Mathematical calculations, image processing in Python	Significant
I/O-bound	API calls, database queries, downloading files	Usually less significant

Why?

When a thread waits for an I/O operation, such as a network response, it generally releases the GIL.

Another thread can then acquire the GIL and execute Python code.

This is why multithreading can be useful even though Python has the GIL.


"""


### Math operations are CPU-bound, so GIL is applied here and Multithreading is not applied here.


import threading
import time

def calculate(thread_name):

    print(f"{thread_name} started")

    total = 0

    for i in range(50_000):
        total += i

    print(f"{thread_name} completed. Total = {total}")


start_time = time.perf_counter()

# Create two threads
t1 = threading.Thread(target=calculate, args=("Thread-1",))
t2 = threading.Thread(target=calculate, args=("Thread-2",))

# Start both threads
t1.start()
t2.start()

# Wait for both threads
t1.join()
t2.join()

end_time = time.perf_counter()

print(f"\nTotal elapsed time: {end_time - start_time:.2f} seconds")








#### I/O-bound operations so generally releases the GIL and Multithreading is applied here.
import threading
import time
def calculate_square(numbers):

    thread_name = threading.current_thread().name

    print(f"{thread_name} started")

    for n in numbers:
        time.sleep(0.2)  # Simulate I/O waiting
        print(f"{thread_name}: Square of {n} is {n * n}")

    print(f"{thread_name} completed")


# Start timer
start_time = time.perf_counter()

# Create threads
t1 = threading.Thread(
    target=calculate_square,
    args=([1, 2, 3, 4, 5],),
    name="Thread-1"
)

t2 = threading.Thread(
    target=calculate_square,
    args=([6, 7, 8, 9, 10],),
    name="Thread-2"
)

# Start both threads
t1.start()
t2.start()

# Wait for both threads to complete
t1.join()
t2.join()

# Calculate elapsed time
end_time = time.perf_counter()

print("\nBoth threads completed!")
print(f"Total elapsed time: {end_time - start_time:.2f} seconds")


