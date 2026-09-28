import random

bb = [1, 2, 3, 4, 5]

mp = random.randint(0, len(bb) - 1)
print(mp)
bb[mp] = 0
print(bb)

print(round(random.random(), 1))
