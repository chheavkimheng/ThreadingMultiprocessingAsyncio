import multiprocessing
import multiprocessing_task
import threading_task
import async_task
import generate_numbers

def main():
    # Step 1: Generate multiple numbers files and process them
    for i in range(5):
        numbers_file = f"numbers_{i}.txt"
        
        print(f"Generating {numbers_file}...")
        generate_numbers.generate_numbers_file(numbers_file, 10000, 100000, 1000000)

        # Step 2: Read numbers from file
        with open(numbers_file, "r") as f:
            numbers = [int(line.strip()) for line in f.readlines()]

        # Step 3: Run multiprocessing task to find primes
        print(f"Running multiprocessing task for {numbers_file}...")
        primes = multiprocessing_task.find_primes_in_range(numbers, chunk_size=len(numbers)//multiprocessing.cpu_count())
        print(f"Prime numbers found in {numbers_file}: {primes[:10]}...")  # Display only the first 10 for brevity

        # Step 4: Run threading task to simulate I/O
        print("Running threading I/O tasks...")
        threading_task.run_io_tasks()

        # Step 5: Run async tasks to write primes to a file
        print(f"Running async I/O tasks for primes_{i}.txt...")
        import asyncio
        asyncio.run(async_task.run_async_tasks(primes, i))
        
if __name__ == "__main__":
    main()
