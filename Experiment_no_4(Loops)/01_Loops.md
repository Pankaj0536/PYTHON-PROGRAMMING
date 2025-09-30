## Loops in Python
 Loops in Python are control flow statements that allow a block of code to be executed repeatedly. They are fundamental for automating repetitive tasks, iterating over data structures, and making code more efficient and concise.

 ### Python primarily offers two main types of loops:

- for loop:
Used for iterating over a sequence (like a list, tuple, string, or range) or other iterable objects.
  - It executes the code block for each item in the sequence.
  - Example:
```Python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
- while loop:
  - Used to repeatedly execute a block of code as long as a specified condition remains True.
  - The loop continues until the condition becomes False.
  - Example:
  
```bash
count = 0
while count < 5:
    print(count)
    count += 1
```