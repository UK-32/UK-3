class Manager:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self):
        print("I am",self.name,"and i am",self.age)

m1 = Manager("Bilal",22)
m2 = Manager("Ali",32)
m3 = Manager("Akif",42)

L = [m1,m2,m3]

for i in L:
    i.intro()
