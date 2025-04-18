# Creating pet class
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.hapiness = 5
        self.tricks = []


    def eat(self):
        print(f"{self.name} is eating 🍖 ...")
        self.hunger = max(0, self.hunger - 3) # Ensures that it does not go below 0
        self.hapiness = min(10, self.hapiness + 1) #Hapiness cant go above 10
        

    def sleep(self):
        print(f"{self.name} is sleeping 😴...")
        self.energy = min(10, self.energy + 5) # Energy max is 10
        

    def play(self):
        print(f"{self.name} is playing 🥎...")
        self.energy = max(0, self.energy - 2) # Energy cant go below 0
        self.hapiness = min(10, self.hapiness + 2)
        self.hunger = min(10, self.hunger + 1) # Hunger max is 10

    def get_status(self):
        print(f"{self.name}'s current status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.hapiness}")
        print(f"Tricks: {self.tricks}")

    def train(self, trick):
        self.tricks.append(trick)
       

    def show_tricks(self):
        print(f"{self.name} knows these tricks ✨: {self.tricks}")


