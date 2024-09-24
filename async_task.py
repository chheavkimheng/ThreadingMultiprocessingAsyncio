import asyncio

async def async_write_to_file(filename, data):
    """Asynchronously write data to a file."""
    await asyncio.sleep(1)  # Simulating non-blocking I/O
    with open(filename, 'w') as f:
        for number in data:
            f.write(f"{number}\n")
    print(f"Finished writing to {filename}.")

async def run_async_tasks(prime_numbers, index):
    """Run async tasks to write prime numbers to a specific file."""
    filename = f"primes_{index}.txt"
    await async_write_to_file(filename, prime_numbers)
