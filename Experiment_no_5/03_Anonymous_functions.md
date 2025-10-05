## Anonymous function in Python

In Python, an anonymous function is a function defined without a name, also commonly known as a lambda function. Unlike regular functions defined using the `def` keyword, `lambda` functions are created using the lambda keyword and are designed for small, single-expression operations.

---
### 1. Syntax :

```python
lambda arguments : expression
```
### 2. Example : 

```python
def add_numbers_def(a, b):
    return a + b

print(add_numbers_def(5, 3)) # Output: 8

# An anonymous (lambda) function to add two numbers
add_numbers_lambda = lambda a, b: a + b

print(add_numbers_lambda(5, 3)) # Output: 8
```