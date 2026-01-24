class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.max_hp = hp
    
    def attack(self):
        print(f"{self.name} атакует")

    def receive_damage(self, amount):

        try:
            dmg = int(amount)
        except Exception:
            dmg = 0
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} получил {dmg} урона, теперь HP: {self.hp}")

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            print("здоровее нету")
            self.hp = self.max_hp
        print(f"{self.name} восстановил {amount} здоровья, теперь: {self.hp}")

class Archer(Character):
    def __init__(self, name, health, arrows):
        super().__init__(name, health)
        self.arrows = arrows

    def shoot(self):
        if self.arrows > 0:
            self.arrows -= 1
            print(f"{self.name} выстрел из лука, осталось боеприпасов: {self.arrows}")
        else:   
            print("стрелы закончились")

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            print("здоровее нету")
            self.hp = self.max_hp
        print(f"{self.name} восстановил {amount} здоровья, теперь: {self.hp}")