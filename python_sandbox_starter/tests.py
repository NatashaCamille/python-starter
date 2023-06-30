class Customer:
    def __init__(self, name, age, membership_type):
        self.name = name
        self.age = age
        self.membership_type = membership_type
    
    def update_membership(self, new_membrship):
        self.membership_type = new_membrship

customers = [Customer("Camille", 30, "Gold"),
             Customer("Natasha", 29, "Platinum")]

print(customers[1].membership_type)
customers[1].update_membership("Gold")
 