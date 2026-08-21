# Week 5 — Object-Oriented Programming

This week you learn to model real-world things in code using **classes**. Object-Oriented Programming (OOP) lets you bundle data (attributes) and behavior (methods) together into reusable blueprints, and to build specialized versions of those blueprints through inheritance.

---

## Concepts Covered

### 1. Classes and Objects

A **class** is a blueprint. An **object** (or *instance*) is a specific thing built from that blueprint.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name      # instance attribute
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof!")

my_dog = Dog("Rex", "Labrador")   # Create an object
my_dog.bark()                      # Rex says: Woof!
print(my_dog.name)                 # Rex
```

- `__init__` is the **constructor** — it runs automatically when you create a new object and sets up its initial state.
- `self` refers to the specific object being created or used. Always make it the first parameter of every method.
- Attributes set with `self.` belong to each individual object.

---

### 2. Inheritance

Inheritance lets a **child class** reuse and extend the code of a **parent class**.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Cat(Animal):          # Cat inherits from Animal
    def speak(self):        # Override the parent's method
        print(f"{self.name} says: Meow!")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof!")

animals = [Cat("Whiskers"), Dog("Rex")]
for animal in animals:
    animal.speak()
# Whiskers says: Meow!
# Rex says: Woof!
```

The child class automatically has access to everything in the parent class.

---

### 3. `super()`

`super()` calls the parent class's version of a method. Use it in `__init__` to avoid repeating initialization code:

```python
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)   # Run Vehicle's __init__
        self.doors = doors              # Add Car-specific attribute

my_car = Car("Toyota", "Camry", 4)
print(my_car.make)    # Toyota
print(my_car.doors)   # 4
```

---

### 4. Polymorphism

**Polymorphism** means "many forms." It lets you call the same method name on different objects and get behavior appropriate to each:

```python
shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5)]

for shape in shapes:
    print(shape.area())   # Each class has its own area() definition
```

This works because each class defines its own `area()`. The caller doesn't need to know which type of shape it has — it just calls `area()` and gets the right answer.

---

### 5. Abstract Behavior and `NotImplementedError`

Sometimes you want a parent class to **require** that every child class implement a method — without providing a default body. Use `NotImplementedError` as a signal:

```python
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
```

If someone creates a subclass of `Shape` and forgets to implement `area()`, they will get a clear `NotImplementedError` instead of a confusing result.

---

## Hints for This Week's Assignment

- **Think in nouns and verbs.** Nouns become classes (or attributes), verbs become methods.
- `__init__` runs **once**, when the object is created. Don't put code there that you want to repeat — that belongs in a regular method.
- Always pass `self` as the first argument to every method inside a class, but when *calling* a method, you don't pass `self` — Python handles it automatically.
- If you forget `self.` before an attribute name in `__init__`, you create a local variable that disappears immediately. Always use `self.attribute_name = value`.
- Use `super().__init__(...)` in child classes to ensure the parent is initialized properly before you add your own setup.
- Raise `NotImplementedError` in the parent to signal clearly: "every child class MUST implement this method."
- Test each class independently before combining them — create an object, call its methods, and verify the output.
