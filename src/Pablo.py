from random import randint


class Pablo:
    def __init__(self) -> None:
        self.energy = 100
        self.happiness = 50
        self.health = 100
        self.poisoning = 0
        self.steps = 0
        self.poisoning_end = 0
        self.died = False

    def step_end(self):
        if self.steps < self.poisoning_end:
            self.health -= self.poisoning
        else:
            self.poisoning = 0
        if self.happiness <= 0:
            self.health -= 10
        if self.energy <= 0:
            self.health -= 5
        if self.health <= 0:
            print(f"Whoops... Pasha died... He lived for {self.steps} steps")

    def play(self):
        print("Dota2 in my heart!")
        self.energy -= 20
        self.happiness += 20
        if self.happiness > 100:
            self.happiness = 100

    def feed(self):
        if randint(0, 100) > 80:
            print("OHHH NOOOOO! I POISONED! [-5 health per step for 10 steps]")
            self.poisoning = 5
            self.poisoning_end = self.steps + 10
            self.health -= self.poisoning
        print("MMM Vkusno!")
        self.energy += 20
        self.health += 25
        if self.energy >= 100:
            self.energy = 100
        if self.health >= 100:
            self.health = 100
