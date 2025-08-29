# Assignment 1: Designing a Class called Smartphone.

# Parent Class
class Smartphone:
    def __init__(self, brand, model, battery_life, storage):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours
        self.storage = storage  # in GB

    # Method to display phone details
    def display_info(self):
        print(f"📱 {self.brand} {self.model}")
        print(f"🔋 Battery Life: {self.battery_life} hours")
        print(f"💾 Storage: {self.storage} GB")

    # Method to simulate using battery
    def use_phone(self, hours):
        if hours < self.battery_life:
            self.battery_life -= hours
            print(f"Used for {hours}h. Battery left: {self.battery_life}h")
        else:
            self.battery_life = 0
            print("Battery drained! Please recharge 🔌")

# Child Class (Inheritance)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery_life, storage, cooling_system):
        super().__init__(brand, model, battery_life, storage)
        self.cooling_system = cooling_system  # extra feature

    # Overriding method (Polymorphism)
    def display_info(self):
        super().display_info()
        print(f"❄️ Cooling System: {self.cooling_system}")

    # Extra method unique to GamingPhone
    def play_game(self, game, hours):
        print(f"🎮 Playing {game} for {hours}h...")
        self.use_phone(hours)


# --- Testing the classes ---
phone1 = Smartphone("Samsung", "Galaxy S23", 20, 128)
gaming_phone = GamingPhone("Asus", "ROG Phone 7", 25, 256, "Liquid Cooling")

print("\n--- Smartphone Info ---")
phone1.display_info()
phone1.use_phone(5)

print("\n--- Gaming Phone Info ---")
gaming_phone.display_info()
gaming_phone.play_game("PUBG Mobile", 6)