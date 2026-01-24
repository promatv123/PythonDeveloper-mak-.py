from RPG import *


voin = Character("воин", 70)
luchnik = Archer("лучник", 50, 1)

print(f"{voin.name} hp: {voin.hp}")
voin.receive_damage(30)
print(f"{voin.name} hp до: {voin.hp}")
voin.heal(20)
print(f"{voin.name} hp теперь: {voin.hp}")
print("="*10)

print(f"{luchnik.name} hp: {luchnik.hp}, стрел: {luchnik.arrows}")
luchnik.shoot()
luchnik.shoot()
