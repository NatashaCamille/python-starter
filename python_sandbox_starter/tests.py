class Customer:
    def __init__(self, name, age, membership_type):
        self.name = name
        self.age = age
        self.membership_type = membership_type
        print("customer created")

c = Customer("Camille", 30, "Gold")
print(c.name, c.age, c.membership_type)