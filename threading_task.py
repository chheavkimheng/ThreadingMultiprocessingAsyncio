import threading
import time
import random

def simulate_io_task(file_name, duration):
    """Simulate downloading or processing a file."""
    print(f"Starting download simulation for {file_name}...")
    time.sleep(duration)
    print(f"Finished downloading {file_name}.")

def run_io_tasks():
    """Run multiple I/O tasks concurrently."""
    threads = []
    for i in range(5):  # Simulating 5 downloads
        file_name = f"file_{i}.txt"
        duration = random.uniform(1, 3)  # Simulate variable download time
        thread = threading.Thread(target=simulate_io_task, args=(file_name, duration))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # Wait for all threads to complete
