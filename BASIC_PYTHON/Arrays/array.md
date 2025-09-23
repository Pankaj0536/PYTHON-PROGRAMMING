# 📘 Array in Python

## 🔹 General Definition
An **array** is a collection of elements **of the same data type** stored in contiguous memory locations.  
- Stores multiple values under a single name.  
- Each element can be accessed using an **index** (starting from `0`).  

---

## 🔹 In Python

Python does **not have built-in arrays** like C or Java. Instead, it provides two main ways:

### **1. List (commonly used in Python)**
Lists can store elements of **different types**, so they behave like a flexible array.  

```python
numbers = [10, 20, 30, 40]
print(numbers[2])  # Output: 30
```
###  **2. Array module (array)**

Python’s array module provides an array data structure where all elements must be of the same type.

```Python
import array
arr = array.array('i', [1, 2, 3, 4])  # 'i' means integer
print(arr[1])  # Output: 2
```

## 🔹Types of Array(collections) :

### Array are further divided into 4 types .

| Collection Type | Ordered | Changeable (Mutable) | Allows Duplicates | Indexed | Notes |
|-----------------|---------|-----------------------|-------------------|---------|-------|
| **List**        | ✔ Yes   | ✔ Yes                | ✔ Yes             | ✔ Yes   | Commonly used for dynamic collections |
| **Tuple**       | ✔ Yes   | ✘ No                 | ✔ Yes             | ✔ Yes   | Immutable version of list |
| **Set**         | ✘ No    | ✘ No*                | ✘ No              | ✘ No    | Elements are unique; unordered collection |
| **Dictionary**  | ✔ Yes** | ✔ Yes                | ✘ No (keys)       | ✔ Yes (keys) | Keys are unique; values can be duplicate |

