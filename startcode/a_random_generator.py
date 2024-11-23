import random

BV = ["Super", "Mega", "Ultra", "Toffe", "Magische",]
ZELF = ["Coder", "Ninja", "Expert", "Gamer",]
for a in range(10):
    Gekozen_BV = random.choice(BV)
    Gekozen_ZELF = random.choice(ZELF)
    print(Gekozen_BV + Gekozen_ZELF)