#used to create customizable thing that can have a wide range of values

# an object will be represented by the class

class character:                                        #creates the class with a name of choice
    def __init__(self, attack, defense, health):                #__init__(self, etc etc) is used to describe what parameters the class has, self is used
        self.attack = attack                                    # to attach the values to the class
        self.defense = defense
        self.health = health                                    #self. will attach to a variable
    def health_potion(self):
        self.health += 40                                       #a function used to modify a parameter with already given values

tank = character(20, 90, 90)                #creates the object using the class, labelled with a name and values for the parameters
print(f"tank stats: {tank.__dict__}")                           #will state the values of the object as a dictionary and will also state the keys associated

glass_cannon = character(90, 10, 20)
print(f"glass cannon stats: {glass_cannon.health}")
                                                                #this shows the use of a health potion, of which will add to the previously stated health value
glass_cannon.health_potion()
print(f"glass cannon stats: {glass_cannon.health}")

