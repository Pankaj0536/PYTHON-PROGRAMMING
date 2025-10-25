#  In this file we will see the use of flush parameter in print statement 

import time # import time module for delay

for i in range(100):
    print(f"[TOTAL = 100] Task {i+1} completed", end="\r", flush=True)
    time.sleep(0.1)

print("\nAll tasks completed successfully.")
