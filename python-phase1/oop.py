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

laptop1 = Laptop("Dell XPS", 16, 2500)
laptop2 = Laptop("MacBook Air", 16, 1800)

laptop1.apply_discount(10)

laptop1.display_info()
laptop2.display_info()

