from enemy import Enemy, Troll, Vampyre

ugly_troll = Troll("Pug")
print(ugly_troll)
ugly_troll.take_damage(4)
print(ugly_troll)

another_troll = Troll("Ug")
print(another_troll)

brother = Troll("Urg")
print(brother)

# ugly_troll.grunt()
# another_troll.grunt()
# brother.grunt()

nosferatu = Vampyre("Nosferatu")
print(nosferatu)
nosferatu.take_damage(4)
print(nosferatu)

print("-" * 40)

another_troll.take_damage(30)
print(another_troll)

while nosferatu.alive:
    nosferatu.take_damage(1)
    print(nosferatu)