import time
wait_time = 1 
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempt", attempts + 1)
    print("Waiting for", wait_time, "seconds...")
    time.sleep(wait_time)  # Simulate waiting for a task to complete
    attempts += 1
    wait_time *= 2  # Exponentially increase the wait time for the next attempt
    print("Next attempt in", wait_time, "seconds...")
    if attempts == max_retries:
        print("Max retries reached. Exiting...")
        break
    print("Retrying...\n")  
