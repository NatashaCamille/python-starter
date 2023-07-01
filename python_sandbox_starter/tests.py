class Customer:
    def __init__(self, name, age, membership_type):
        self.name = name
        self.age = age
        self.membership_type = membership_type

#update membership   
    def update_membership(self, new_membrship):
        print("Calculating costs")
        self.membership_type = new_membrship

#Converting to string
    def __str__(self):
        print("converting to string")
        return self.name + " " + self.membership_type

#Compare customers
    # def __eq__(self, other):
    #     if self.name == other.name and self.membership_type == other.membership_type:
    #         return True
        
    #     return False

customers = [Customer("Camille", 30, "Gold"),
             Customer("Camille", 30, "Gold")]

#print(customers[1])
#customers[1].update_membership("Gold")
#print(customers[1])

print(customers[0] == customers[1])
 