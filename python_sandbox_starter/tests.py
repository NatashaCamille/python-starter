class Customer:
    def __init__(self, name, age, membership_type):
        self.name = name
        self.age = age
        self.membership_type = membership_type
    
    def update_membership(self, new_membrship):
        print("Calculating costs")
        self.membership_type = new_membrship

    def __str__(self):
        print("converting to string")
        return self.name + " " + self.membership_type
customers = [Customer("Camille", 30, "Gold"),
             Customer("Natasha", 29, "Platinum")]

print(customers[1])
customers[1].update_membership("Gold")
print(customers[1])


 