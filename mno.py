class Customer:

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def greet(self):
        if self.gender == "Male":
            print("Hello", self.name, "sir")
        else:
            print("Hello", self.name, "madam")

        new_customer = Customer("Uzair", "Male")
        return new_customer

cust = Customer("Alia", "Female")

new_cust = cust.greet()

print(new_cust.name)
