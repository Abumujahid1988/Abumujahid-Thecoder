### 🚀 The Readme file for Polymorphism Challenge: Vehicles Example

## 📌 Overview
This project demonstrates the concept of **polymorphism** in Python using vehicles.  
Polymorphism allows different classes to implement the same method (`move()`) in different ways.  

For example:
- A `Car` **drives** 🚗  
- A `Plane` **flies** ✈️  
- A `Boat` **sails** 🛥️  
- A `Bicycle` **pedals** 🚴  

All these classes share the same action (`move()`), but each defines it uniquely.

---

## 🏗️ Code Structure
- **Vehicle (Base Class)** → Defines a `move()` method (to be overridden).
- **Car, Plane, Boat, Bicycle (Subclasses)** → Each provides its own version of `move()`.

---

## ▶️ How to Run
1. Save the program in a file called `vehicles.py`.
2. Run it with:
   ```bash
   python vehicles.py
````

---

## 💻 Example Output

```text
🚗 The car is driving on the road.
✈️ The plane is flying in the sky.
🛥️ The boat is sailing on the water.
🚴 The bicycle is pedaling on the track.
```
