class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        return f"name is {self.name} and age is {self.age}"

    def get_info(self):
        return f" coat color is {self.coat_color}"


class JackRussellTerrier(Dog):

    def Jack(self,food):
        self.food = food
        print("food it eat is ",self.food)

    

class Bulldog(Dog):
    def Bull(self,color):
        self.color=color
        print("Its color is : ",self.color)

JackRussell=JackRussellTerrier("nicy","7month","grey")

print(JackRussell.description())
print(JackRussell.get_info())
JackRussell.Jack("chkn")

Bull=Bulldog("baby","6month","black")
print(Bull.description())
print(Bull.get_info())
JackRussell.Jack("apple")
