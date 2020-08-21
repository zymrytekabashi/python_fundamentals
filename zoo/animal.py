class Animal:
    def __init__(self):
        self.name=name
        self.age =age
        self.health = health
        self.happiness = happiness
    
    def display_info(name, age, health, happiness):
        print(f'Name of animal: {self.name} \nAge of animal: {self.age} \nHealth of animal: {self.health} \nHappiness{self.happiness}')
        
    def feed(self):
        self.health += 10
        self.happiness += 10    
        