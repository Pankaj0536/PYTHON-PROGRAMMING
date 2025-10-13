# OOPs concepts in Python

Object-Oriented Programming (OOPs) is a way of writing programs where we group data and the actions that work on that data into units called objects.

---

## 1. Basic building blocks: classes and objects

* **Class**: a blueprint for objects. Defines attributes (data) and methods (functions).
* **Object (instance)**: a concrete realization of a class.

```python
class Dog:
     # constructor
    def __init__(self ,name ,age):       
        self.name = name                 # instance attribute
        self.age = age

    def bark(self):                      # instance method
        return f"{self.name} says woof!"

d = Dog("Rex", 3)
print(d.bark())  # Rex says woof!
```

`self` refers to the instance. `__init__` runs when a new object is created.

---

## 2. Encapsulation

Encapsulation groups data and methods and (optionally) limits access.

* Python uses naming conventions:

  * `public`: `obj.x`
  * `protected` (convention): `_x` (single underscore)
  * `private` (name mangling): `__x` becomes `_ClassName__x` internally

Use properties to control access (getter/setter pattern) idiomatically:

```python
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance   # private (name-mangled)

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = amount

acct = BankAccount(100)
print(acct.balance)  # 100
acct.balance = 200   # uses setter
```

---

## 3. Abstraction

Abstraction means exposing only what’s necessary and hiding internals. In Python, you do this by providing clear methods/properties and hiding implementation details (using `_` or `__` as above).

You can also use `abc` module (abstract base classes) to force subclasses to implement methods:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.1416 * self.r * self.r
```

---

## 4. Inheritance 

A class can inherit attributes & methods from another:

```python
class Animal:
    def speak(self):
        return "some sound"

class Cat(Animal):
    def speak(self):               # override
        return "meow"

c = Cat()
print(c.speak())  # meow
```

* **Single inheritance**: `class Child(Parent):`
* **Multiple inheritance**: `class C(A, B):` — Python supports this.
* **`super()`** helps call parent methods:

```python
class A:
    def __init__(self): print("A init")
class B(A):
    def __init__(self):
        super().__init__()   # calls A.__init__
        print("B init")
```

---

## 5. Polymorphism 

Polymorphism lets different classes be used via the same interface (methods with same name).

```python
class Dog:
    def speak(self): return "woof"
class Cat:
    def speak(self): return "meow"

for pet in (Dog(), Cat()):
    print(pet.speak())   # works for both -> polymorphism (duck typing)
```

Python follows **duck typing**: “if it walks like a duck...” — you don’t need a shared base class.

---

## 6. Special (magic/dunder) methods

Python classes can implement special methods to integrate with language features:

* `__str__`, `__repr__` — string representations
* `__len__`, `__iter__`, `__next__` — container/iterator protocol
* `__add__`, `__eq__`, `__lt__` — operator overloading
* `__enter__`, `__exit__` — context manager support (`with`)

Example:

```python
class Vector:
    def __init__(self, x, y): self.x, self.y = x, y
    def __add__(self, other): return Vector(self.x+other.x, self.y+other.y)
    def __repr__(self): return f"Vector({self.x}, {self.y})"

v = Vector(1,2) + Vector(3,4)
print(v)  # Vector(4, 6)
```

---

## 7. Class vs Instance variables

* **Instance variable**: `self.x` — unique to each object.
* **Class variable**: defined directly in class — shared by all instances.

```python
class Cat:
    species = "Felis catus"   # class variable

    def __init__(self, name):
        self.name = name      # instance variable
```

---

## 8. `@staticmethod` and `@classmethod`

* `@staticmethod`: function inside class namespace, no `self` or `cls`.
* `@classmethod`: receives `cls` (class object) — useful for alternative constructors.

```python
class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1

    @classmethod
    def from_fullname(cls, fullname):
        first = fullname.split()[0]
        return cls(first)

    @staticmethod
    def is_adult(age):
        return age >= 18
```

---

## 9. Composition vs Inheritance

* **Inheritance**: “is-a” relationship (Dog is-an Animal).
* **Composition**: “has-a” relationship (Car has-an Engine). Preferred when you want loose coupling.

```python
class Engine:
    def start(self): return "engine started"

class Car:
    def __init__(self):
        self.engine = Engine()   # composition
```

---

## 10. Multiple inheritance and MRO (Method Resolution Order)

Python uses C3 linearization for MRO. If you have `class C(A, B)`, method lookup follows `C -> A -> B -> object` depending on MRO. Use `Class.__mro__` or `help(Class)` to inspect.

Example showing MRO:

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.__mro__)  # shows lookup order
```
---

## 11. Interfaces / Protocols 

Python uses structural typing via `typing.Protocol` to specify expected method names without inheritance (fits duck typing style).

---

## 12. Best practices & design patterns (short)

* Keep classes small and focused (Single Responsibility Principle).
* Prefer composition over inheritance where logical.
* Use properties to encapsulate validation.
* Use abstract base classes only when you require explicit interface enforcement.
* Use `__repr__` for debugging-friendly representations.
* Avoid excessive use of `@property` that performs heavy computation — keep it light.

---

## 13. Small complete example that demonstrates many concepts

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make): self.make = make

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    wheels = 4                # class variable
    def __init__(self, make, model):
        super().__init__(make)
        self.model = model    # instance variable

    def start(self):          # implementation (polymorphism)
        return f"{self.make} {self.model} engine started"

    def __repr__(self):
        return f"Car({self.make!r}, {self.model!r})"

# composition example
class Garage:
    def __init__(self):
        self.vehicles = []

    def park(self, v: Vehicle):
        self.vehicles.append(v)

g = Garage()
c = Car("Toyota", "Corolla")
g.park(c)
print(g.vehicles)   # shows stored Car object
```

---

# 14. Quick reference checklist

* Class? — `class Name:`
* Constructor? — `def __init__(self, ...)`
* Instance method? — first param `self`
* Class method? — `@classmethod` + `cls`
* Static method? — `@staticmethod`
* Private attribute? — prefix `__` (name mangling)
* Property? — `@property` and `@x.setter`
* Abstract? — use `abc.ABC` + `@abstractmethod`
* Operator overloading? — implement `__add__`, `__eq__`, etc.
