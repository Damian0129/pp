import random

Time_t = random.randint(3, 6)

if Time_t / 2 == 1.5:
    print("Горит зелённый")
elif Time_t / 2 == 3:
    print("Горит красный")
