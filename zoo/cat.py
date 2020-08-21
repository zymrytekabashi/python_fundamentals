class Animal:
    def __init__(self, name, age, health, happiness):
        self.name=name
        self.age =age
        self.health = health
        self.happiness = happiness
    
    def display_info(self):
        print(f'Name of animal: {self.name} \nAge of animal: {self.age} \nHealth of animal: {self.health} \nHappiness{self.happiness}')
        
    def feed(self):
        self.health += 10
        self.happiness += 10 


class Cat(Animal):
    def __init__(self, family):
        super().__init__(self.name, self.age, self.health,self.happiness)
        self.family= family
        
    
class Dog(Animal):
    def __init__(self, color):
        super().__init__(self.name, self.age, self.health,self.happiness)
        self.color = color
        
class Lion(Animal):
    def __init__(self, weight):
        super().__init__(self.name,self.age, self.health, self.happiness)
        self.weight = weight
        
