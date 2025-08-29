### 📱 The Readme file for Smartphone & GamingPhone Program

## 📖 Overview

This program demonstrates **Object-Oriented Programming (OOP)** in Python by designing a custom class.
It includes:

* A **Smartphone** class with attributes and methods.
* A **GamingPhone** class that inherits from Smartphone, showing **inheritance** and **polymorphism**.
* Encapsulation of data (like battery life).

The program simulates real-life smartphone behavior, such as checking info, using battery, and playing games.

---

## 🏗️ Features

* **Smartphone class**

  * Attributes: brand, model, battery life, storage
  * Methods:

    * `display_info()` → shows phone details
    * `use_phone(hours)` → reduces battery life

* **GamingPhone class** (inherits from Smartphone)

  * Extra attribute: cooling system
  * Overridden method: `display_info()` (shows cooling system as well)
  * New method: `play_game(game, hours)` → simulates playing a game and drains battery

---

## ⚙️ How It Works

1. Create objects of `Smartphone` and `GamingPhone`.
2. Display their details.
3. Use phone methods like `use_phone()` or `play_game()`.
4. Observe how inheritance and method overriding works.

---

## 💻 Example Output

```
--- Smartphone Info ---
📱 Samsung Galaxy S23
🔋 Battery Life: 20 hours
💾 Storage: 128 GB
Used for 5h. Battery left: 15h

--- Gaming Phone Info ---
📱 Asus ROG Phone 7
🔋 Battery Life: 25 hours
💾 Storage: 256 GB
❄️ Cooling System: Liquid Cooling
🎮 Playing PUBG Mobile for 6h...
Used for 6h. Battery left: 19h
```

---

## 🎯 Concepts Demonstrated

* **Class & Objects**
* **Constructors (`__init__`)**
* **Encapsulation** (battery life management)
* **Inheritance** (GamingPhone inherits Smartphone)
* **Polymorphism** (method overriding: `display_info()`)

---

## 🚀 How to Run

1. Save the program as `smartphone.py`.
2. Run in terminal or VS Code:

   ```bash
   python smartphone.py
