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

---

## Assignment Instructions

**File to create:** `module_05/shapes.py`

You will build a small shape hierarchy using classes, inheritance, and polymorphism. Follow each step in order.

---

### Step 1 — Create the `Shape` base class

Create a class called `Shape` with:
- An `__init__` method that accepts and stores a `color` string (e.g., `"red"`).
- A method `area(self)` that raises `NotImplementedError` with the message `"Subclasses must implement area()"`.
- A method `perimeter(self)` that raises `NotImplementedError` with the message `"Subclasses must implement perimeter()"`.
- A method `describe(self)` that **returns** a string like: `"A red shape with area 78.54 and perimeter 31.42"`. (It should call `self.area()` and `self.perimeter()` internally, and format both values to 2 decimal places.)

---

### Step 2 — Create the `Circle` subclass

Create a class `Circle` that inherits from `Shape`.

- `__init__` takes `color` and `radius`. Call `super().__init__(color)` and store `radius`.
- `area(self)` returns `π * radius²`. Use `import math` and `math.pi`.
- `perimeter(self)` returns `2 * π * radius` (circumference).

Test it:
```python
c = Circle("blue", 5)
print(c.area())        # 78.539...
print(c.perimeter())   # 31.415...
print(c.describe())    # A blue shape with area 78.54 and perimeter 31.42
```

---

### Step 3 — Create the `Rectangle` subclass

Create a class `Rectangle` that inherits from `Shape`.

- `__init__` takes `color`, `width`, and `height`. Store both dimensions.
- `area(self)` returns `width * height`.
- `perimeter(self)` returns `2 * (width + height)`.

---

### Step 4 — Create the `Triangle` subclass

Create a class `Triangle` that inherits from `Shape`.

- `__init__` takes `color`, `a`, `b`, `c` (the three side lengths).
- `perimeter(self)` returns `a + b + c`.
- `area(self)` uses **Heron's formula**:

```python
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
```

---

### Step 5 — Demonstrate polymorphism

Create a list containing at least one `Circle`, one `Rectangle`, and one `Triangle` with different colors. Loop over the list and call `describe()` on each shape — you should not need to check what type each shape is.

```python
shapes = [
    Circle("red", 3),
    Rectangle("green", 4, 6),
    Triangle("blue", 3, 4, 5),
]

for shape in shapes:
    print(shape.describe())
```

Expected output (values may differ based on your dimensions):
```
A red shape with area 28.27 and perimeter 18.85
A green shape with area 24.00 and perimeter 20.00
A blue shape with area 6.00 and perimeter 12.00
```

---

### Step 6 — Add a `Square` subclass

Create a class `Square` that inherits from **`Rectangle`** (not `Shape` directly).

- `__init__` takes `color` and `side`. Call `super().__init__(color, side, side)`.
- You do **not** need to override `area()` or `perimeter()` — they should work automatically through inheritance.

Add a `Square` to your shapes list and verify `describe()` works correctly.

---

### Step 7 — Find the largest shape

Write a standalone function (outside any class) called `largest_shape(shapes)` that accepts a list of shapes and returns the one with the greatest area.

```python
biggest = largest_shape(shapes)
print(f"Largest: {biggest.describe()}")
```

---

### Checklist Before Submitting

- [ ] `Shape` base class exists with `area()`, `perimeter()`, and `describe()`.
- [ ] `area()` and `perimeter()` in `Shape` raise `NotImplementedError`.
- [ ] `Circle`, `Rectangle`, and `Triangle` all correctly implement `area()` and `perimeter()`.
- [ ] `Square` inherits from `Rectangle` and works without redefining area/perimeter.
- [ ] All subclasses call `super().__init__(color)` (or equivalent).
- [ ] The polymorphism loop calls `describe()` on all shapes without type-checking.
- [ ] `largest_shape()` function works correctly.
- [ ] All output is formatted to 2 decimal places.
