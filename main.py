class Warrior():
    def __init__(self, name, con, str, dex):
        self.name = name
        self.constitution = con
        self.strength = str
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
        print(f'Constitution: {self.constitution}')
        print(f'Strength: {self.strength}')
        print(f'Dexterity: {self.dexterity}')


#Создаем 1го воина

Infantry = Warrior('Rumpel', 60, 40, 30)
cavalry = Warrior('Pegas', 40, 50, 40)
print(Infantry.name)
print(Infantry.constitution)
print(Infantry.strength)
print(Infantry.dexterity)

Infantry.show_stats()

print(cavalry.name)
print(cavalry.constitution)
print(cavalry.strength)
print(cavalry.dexterity)

cavalry.show_stats()




