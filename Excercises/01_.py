'''
AIM : 
 Word Frequency Counter: Write a program that counts the frequency of each word in a multi-line paragraph. Ensure it ignores case and removes common punctuation (., !, ?).
'''

# Multi-line paragraph input
text = """Hello world!
This is a test.
Hello again, world?"""

# Step 1: Convert to lowercase
text = text.lower()

# Step 2: Remove punctuation
punctuations = ".,!?"
for p in punctuations:
    text = text.replace(p, "")

# Step 3: Split into words
words = text.split()

# Step 4: Count frequency
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Step 5: Print result
print("Word Frequency:")
for word, count in word_count.items():
    print(word, ":", count)
