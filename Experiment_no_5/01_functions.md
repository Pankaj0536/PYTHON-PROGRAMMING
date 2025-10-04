# Functions in Python

## 📌 What is a Function?
A **function** in Python is a block of organized, reusable code that performs a specific task.  
Functions help to make code **modular, reusable, and easier to understand**.

Instead of writing the same code multiple times, you can define a function once and call it whenever needed.

---

## 🔹 Why Use Functions?
- Avoid code repetition (reusability)
- Makes program modular and easier to debug
- Improves readability
- Allows splitting a large problem into smaller tasks

---

## 🔹 Function Syntax in Python
in python the function defined using def
```python
def function_name(parameters):
    # function body
    return value
```

- `def` → keyword to define a function  
- `function_name` → name of the function  
- `parameters` → (optional) input values  
- `return` → (optional) output value  

---

## 🔹 Types of Functions

### 1. Function without parameters
```python
def greet():
    print("Hello, welcome to Python!")
```
Usage:
```python
greet()
```

---

### 2. Function with parameters
```python
def greet(name):
    print("Hello,", name)
```
Usage:
```python
greet("Pankaj")
```

---

### 3. Function with return value
```python
def add(a, b):
    return a + b
```
Usage:
```python
result = add(5, 3)
print("Sum is:", result)
```

---

### 4. Function with default parameters
```python
def greet(name="Guest"):
    print("Hello,", name)
```
Usage:
```python
greet()          # Hello, Guest
greet("Pankaj")  # Hello, Pankaj
```

---

### 5. Multiple return values
```python
def calc(a, b):
    return a+b, a-b, a*b
```
Usage:
```python
s, d, m = calc(10, 5)
print("Sum:", s, "Diff:", d, "Mul:", m)
```

---

### 6. Lambda Function (Anonymous Function)
```python
square = lambda x: x * x
print(square(5))   # 25
```

