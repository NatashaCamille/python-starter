class Customer:
    def __init__(self, name, age, membership_type):
        self.name = name
        self.age = age
        self.membership_type = membership_type
        print("customer created")

customers = [Customer("Camille", 30, "Gold"), Customer("Natasha", 29, "Platinum")]

print(customers[1].name)
 