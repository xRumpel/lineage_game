class Warrior():
    def __init__(self, name, str, con, dex):
        self.name = name
        self.strength = str
        self.constitution = con
        self.dexterity = dex

    def attack(self, target):
        target.hp -= self.strength

    def heal(self, target):
        target.hp += self.constitution

    def sleep(self):
        print(f'{self.name} is sleeping')
        self.constitution += 2

    def eat(self):
        print(f'{self.name} is eating')
        self.constitution += 5

    def hit(self):
        print(f'{self.name} is hitting')
        self.strength -= 6

    def run(self):
        print(f'{self.name} is running')
        self.dexterity -= 7

    def show_stats(self):
        print(f'Name: {self.name}')
        print(f'Strength: {self.strength}')
        print(f'Constitution: {self.constitution}')
        print(f'Dexterity: {self.dexterity}')