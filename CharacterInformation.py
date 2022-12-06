class Character:
    class Hero:
        def __init__(self, name, ID, level, loot):
            self.name = input(name)
            self.ID = input(ID)
            self.level = input(level)
            self.loot = input(loot)

    Hero_A = Hero('Enter the hero name: ','Enter the character ID number: ','Enter the hero level: ','Enter the hero loot value: ')

    class Boss:
        def __init__(self, name, ID, level, HP, attack):
            self.name = input(name)
            self.ID = input(ID)
            self.level = input(level)
            self.HP = input(HP)
            self.attack = input(attack)

    Boss_A = Boss('Enter the boss name: ','Enter the character ID number: ','Enter the boss level: ','Enter the boss HP: ', 'Enter the boss attack damage: ')

    print('Hero information: ')

    print(Hero_A)

    print('Boss information: ')

    print(Boss_A)
