# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
    def __init__(self, name, color, value) -> None:
        self.name=name
        self.color=color
        self.value=value

# your code goes here
car1 = Vehicle(name="Fer",color="red",value=60000.00)
car2 = Vehicle(name="Jump",color="blue",value=10000.00)

# test code
print(car1.description())
print(car2.description())
