# Week 5 — Object-Oriented Programming
### Classes, Objects, Inheritance, Polymorphism, and super()

---

## Welcome!

Everything you've written so far has been functions and variables floating around together. Object-Oriented Programming (OOP) is a way to organize your code by bundling related data and behavior together into a single package called an **object**. It's the way most real software in the world is built.

---

## Concept 1: Classes and Objects

**Analogy:** Think of a class as a **blueprint** or **cookie cutter**. The blueprint for a house describes what every house built from it will have — bedrooms, bathrooms, walls. But the blueprint *itself* isn't a house. When you actually build one, *that's* an object (also called an **instance**).

- `class Dog:` → the blueprint (describes all dogs)
- `my_dog = Dog("Rex", "Labrador")` → one specific dog built from the blueprint

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name      # This dog's name
        self.breed = breed    # This dog's breed

    def bark(self):
        print(f"{self.name} says: Woof!")

my_dog = Dog("Rex", "Labrador")
my_dog.bark()                   # Rex says: Woof!
print(my_dog.name)              # Rex
```

**Breaking down `__init__`:**
- `__init__` is the **constructor** — it runs automatically every time you create a new object
- `self` refers to *this specific object*. It's how the object talks about itself. Always list it first in method definitions, but never pass it when calling
- `self.name = name` stores the value `name` onto *this* object so it remembers it later

**Analogy for `self`:** If there are 30 Dog objects, each one needs its own memory slot for its name. `self.name` gives each dog its own personal name tag, separate from all other dogs.

---

## Concept 2: Inheritance — "Is a Kind Of"

Inheritance lets you create a **new class that gets everything from an existing class for free**, and then add or change things.

**Analogy:** A `Car` is a kind of `Vehicle`. Every vehicle has an engine and can move. A car *inherits* all of that and adds: four wheels, doors, and a stereo. You don't redesign the engine from scratch.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Cat(Animal):       # Cat inherits from Animal — Cat "is a kind of" Animal
    def speak(self):     # Override (replace) the speak method with cat-specific behavior
        print(f"{self.name} says: Meow!")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof!")

my_cat = Cat("Whiskers")
my_dog = Dog("Rex")

my_cat.speak()    # Whiskers says: Meow!
my_dog.speak()    # Rex says: Woof!
```

`Cat` didn't have to define `__init__` — it **inherited** it from `Animal` automatically.

---

## Concept 3: `super()` — Calling the Parent

`super()` gives you access to the parent class's version of a method. Use it when the child class has *more* setup to do, but still needs the parent's setup to run first.

**Analogy:** You start a new job. Your manager (parent) shows you the general onboarding (parent's `__init__`). Then your department head (child class) adds department-specific training (`super()` calls the manager's onboarding first, then adds its own steps).

```python
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)   # Run Vehicle's setup first
        self.doors = doors              # Then add Car's own attribute

my_car = Car("Toyota", "Camry", 4)
print(my_car.make)    # Toyota  — from Vehicle
print(my_car.doors)   # 4       — from Car
```

---

## Concept 4: Polymorphism — "Same Interface, Different Behavior"

**Polymorphism** means you can call the same method name on different types of objects, and each one does the right thing for its type.

**Analogy:** The word "speak" means something different for a cat, a dog, and a parrot. But you can say "speak!" to any of them and get a correct, animal-appropriate response. You don't need to know what kind of animal it is first.

```python
animals = [Cat("Whiskers"), Dog("Rex"), Cat("Luna")]

for animal in animals:
    animal.speak()    # Each object knows its own version of speak()
# Whiskers says: Meow!
# Rex says: Woof!
# Luna says: Meow!
```

This is powerful because your loop doesn't care what type each animal is — it just calls `speak()` and trusts the right thing will happen.

---

## Concept 5: NotImplementedError — Forcing Subclasses to Do Their Job

Sometimes you want a parent class to say: "I can't do this myself, but every class that inherits from me MUST do it." You signal this by raising `NotImplementedError`.

**Analogy:** A job posting says "Must know how to code." It doesn't teach you to code — that's your responsibility. If you show up without that skill, you've violated the requirement.

```python
class Shape:
    def area(self):
        raise NotImplementedError("Every shape must implement area()")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

# This would crash:
# s = Shape()
# s.area()  →  NotImplementedError: Every shape must implement area()

# This works:
c = Circle(5)
print(c.area())   # 78.53...
```

---

## Assignment Instructions

**File to create:** `module_05/shapes.py`

You'll build a shape hierarchy from scratch. Each step adds one class or one method.

---

### Step 1 — Create the `Shape` base class

The parent class that all shapes will inherit from.

It needs:
- `__init__(self, color)` — stores `color` as an attribute
- `area(self)` — raises `NotImplementedError("Subclasses must implement area()")`
- `perimeter(self)` — raises `NotImplementedError("Subclasses must implement perimeter()")`
- `describe(self)` — **returns** (don't print!) a string like:
  `"A red shape with area 78.54 and perimeter 31.42"`
  This method calls `self.area()` and `self.perimeter()` to get the numbers, then formats them to 2 decimal places.

Test that `NotImplementedError` works:
```python
s = Shape("red")
s.area()   # Should raise NotImplementedError
```

---

### Step 2 — Create `Circle`

Inherits from `Shape`. Needs radius.

- `__init__(self, color, radius)` — call `super().__init__(color)`, then store `radius`
- `area(self)` → `math.pi * radius²` (use `import math` at the top of the file)
- `perimeter(self)` → `2 * math.pi * radius`

```python
c = Circle("blue", 5)
print(c.area())        # 78.53981...
print(c.perimeter())   # 31.41592...
print(c.describe())    # A blue shape with area 78.54 and perimeter 31.42
```

---

### Step 3 — Create `Rectangle`

Inherits from `Shape`. Needs width and height.

- `area(self)` → `width * height`
- `perimeter(self)` → `2 * (width + height)`

```python
r = Rectangle("green", 4, 6)
print(r.describe())   # A green shape with area 24.00 and perimeter 20.00
```

---

### Step 4 — Create `Triangle`

Inherits from `Shape`. Needs three side lengths: `a`, `b`, `c`.

- `perimeter(self)` → `a + b + c`
- `area(self)` — use Heron's formula. Don't worry if it looks scary, just copy the pattern:

```python
import math
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
```

(The variable `s` here is the "semi-perimeter" — unrelated to `self`. Rename it `semi` if that's confusing.)

```python
t = Triangle("yellow", 3, 4, 5)   # A right triangle!
print(t.area())        # 6.0
print(t.perimeter())   # 12
```

---

### Step 5 — Demonstrate polymorphism

Create a list with one of each shape. Loop through and call `describe()` on each — your loop should NOT check what type each shape is:

```python
shapes = [
    Circle("red", 3),
    Rectangle("green", 4, 6),
    Triangle("blue", 3, 4, 5),
]

for shape in shapes:
    print(shape.describe())
```

---

### Step 6 — Create `Square`

`Square` is a special rectangle — both sides are equal. Inherit from `Rectangle` (not `Shape`).

- `__init__(self, color, side)` — call `super().__init__(color, side, side)` (pass the same value for both width and height)
- You do NOT need to define `area()` or `perimeter()` — they're inherited from `Rectangle` and already work!

```python
sq = Square("purple", 5)
print(sq.describe())   # A purple shape with area 25.00 and perimeter 20.00
```

---

### Step 7 — `largest_shape(shapes)` function

Write a standalone function (outside any class) that takes a list of shapes and returns the one with the greatest area.

```python
biggest = largest_shape(shapes)
print(f"Largest shape: {biggest.describe()}")
```

---

### Common Mistakes to Avoid

- Forgetting `self.` when storing attributes → the value disappears after `__init__` finishes
- Forgetting to call `super().__init__(...)` → the parent's attributes never get set up
- Trying to call `area()` on a `Shape()` object directly → `NotImplementedError`
- Printing inside `describe()` instead of returning → the value is lost

---

### Checklist Before Submitting

- [ ] `Shape` exists with `area()`, `perimeter()`, and `describe()`
- [ ] `area()` and `perimeter()` in `Shape` raise `NotImplementedError`
- [ ] `describe()` in `Shape` *returns* a string (not prints), with 2 decimal places
- [ ] `Circle`, `Rectangle`, `Triangle` all inherit from `Shape` and implement both methods
- [ ] All child `__init__` methods call `super().__init__(color)`
- [ ] `Square` inherits from `Rectangle` and needs no extra math methods
- [ ] The polymorphism loop calls `describe()` without any `if isinstance(...)` type checks
- [ ] `largest_shape()` correctly finds the shape with the greatest area
