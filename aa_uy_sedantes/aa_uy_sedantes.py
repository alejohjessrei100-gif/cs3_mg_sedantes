class Zombies:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def move(self, movement):
        self.health = movement
        print("sigh, ...panting")

    def take_damage(self, health):
        self.health = health
        print("Grrh!")

    def attack_plant(self, damage):
        self.damage = damage
        print("Yrrh!")


class Plants:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage    

    def attack_zombie(self, damage):
        self.damage = damage
        print("Pew!")

    def take_damage(self, health):
        self.health= health

plant1 = Plants("Garpea_Shooter" , 67, 15)





zombie1 = Zombies("Garret_Uy", 100, 10)

    
        