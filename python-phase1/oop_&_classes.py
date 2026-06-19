class Laptop:
    def __init__(self, name, ram, price):
        self.name = name
        self.ram = ram
        self.price = price

    def display_info(self):
        print(f"Laptop Name: {self.name} - RAM: {self.ram}GB - Price: ${self.price}")

    def apply_discount(self, percentage):
        laptop_discount = self.price * (percentage / 100)
        self.price -= laptop_discount

laptops = [
    Laptop("Dell XPS 13", 16, 999),
    Laptop("MacBook Pro", 8, 1299),
    Laptop("HP Spectre x360", 8, 1099),
    Laptop("Lenovo ThinkPad X1 Carbon", 16, 1199)
]

most_expensive_laptop = laptops[0]



for laptop in laptops:
    if laptop.price > most_expensive_laptop.price:
        most_expensive_laptop = laptop

print("Most Expensive Laptop:")
most_expensive_laptop.display_info()