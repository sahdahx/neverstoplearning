class Player:
    def __init__(self, name, health=100, energy=100):
        self.name = name
        self.health = health
        self.energy = energy

    def attack(self, target, damage=1):
        target.health -= damage
        self.energy -= damage  
        print(f"{self.name} attacking {damage} damage to {target.name}!")
        if target.is_attacked(player_name=self.name):
            self.health -= target.damage

    def show_info(self):
        print(f"{self.name} energy: {self.energy}")
        print(f"{self.name} health: {self.health}")


class Monster:
    def __init__(self, name, health=600):
        self.name = name
        self.health = health            #nilai dinamis
        self.health_init = self.health  #nilai default
        self.damage = 10

    def is_attacked(self, player_name):
        print(f"{self.name} attack {self.damage} damage to {player_name}")
        return self.health < self.health_init
    
    def show_info(self):
        print(f"{self.name} health: {self.health}")

player1 = Player(name="Asada")
player2 = Player(name="Senku")
dragon = Monster(name="Drag")
scorpion = Monster(name="Scale")

player1.attack(target=dragon, damage=80)
player2.attack(target=scorpion, damage=50)
#dragon.attack()

#print(player1.__dict__)
#print(player2.__dict__)

player1.show_info()
player2.show_info()
dragon.show_info()