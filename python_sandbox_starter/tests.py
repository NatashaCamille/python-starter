class Customer:
    def __init__(self, name, age, membership_type):
        self.name = name
        self.age = age
        self.membership_type = membership_type
    
    def update_membership(self, new_membrship):
        print("Calculating costs")
        self.membership_type = new_membrship

    #Static method
    def read_customer():
        print("Reading customer from DB")

customers = [Customer("Camille", 30, "Gold"),
             Customer("Natasha", 29, "Platinum")]

print(customers[1].membership_type)
customers[1].update_membership("Gold")
print(customers[1].membership_type)

Customer.read_customer()
 