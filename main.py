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
        self.constitution += 5

    def eat(self):
        print(f'{self.name} is eating')
        self.strength += 5

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
Cavalry = Warrior('Pegas', 40, 50, 40)

Infantry.sleep()
Infantry.eat()
Infantry.hit()
Infantry.run()
Infantry.show_stats()

Cavalry.sleep()
Cavalry.eat()
Cavalry.hit()
Cavalry.run()
Cavalry.show_stats()

