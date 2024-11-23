from sterren_module import *
import random

kleuren = ["red", "orange", "yellow", "lime green", "orchid", "magenta", "dodger blue", "crimson", "chocolate", "navy", "salmon", "green yellow", "teal", "cyan", "aquamarine", "hot pink", "firebrick", "royal blue", "wheat"]

for a in range(30):
    Gekozen_X = random.randint(-350, 350)
    Gekozen_Y = random.randint(-300 , 300)
    Gekozen_kleur = random.choice(kleuren)

    teken_ster(Gekozen_X, Gekozen_Y, Gekozen_kleur)
turtle.mainloop()