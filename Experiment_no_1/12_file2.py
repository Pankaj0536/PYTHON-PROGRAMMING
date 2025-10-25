import time

# Open file in write mode
f = open("flushfile.txt", "w")

# Print initial message to file and screen
print("Downloading:", end="", file=f, flush=True)

for i in range(20):
    # Print progress block to file and screen
    print("█", end="", flush=True, file=f)
    time.sleep(0.1)  # faster for testing

# Print Done! to file and screen
print(" Done!", file=f)


f.close()

# Future wale pankaj isme problem kya hai muje bata