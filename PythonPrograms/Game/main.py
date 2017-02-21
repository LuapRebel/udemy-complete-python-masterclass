from player import Player
# import player as pl

tim = Player("Tim")

print(tim.name)
print(tim.lives)
tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)

tim.lives = 9
print(tim)

tim.level = 2
print(tim)

tim.level += 5
print(tim)

tim.level -= 1
print(tim)