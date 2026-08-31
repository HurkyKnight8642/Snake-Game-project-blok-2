# eten.py
import random
import instellingen

def spawn_eten(slang_lijst):
    max_x = (instellingen.BREEDTE // instellingen.GRID_GROOTTE) - 1
    max_y = (instellingen.HOOGTE // instellingen.GRID_GROOTTE) - 1

    while True:
        positie = (random.randint(0, max_x), random.randint(0, max_y))
        if positie not in slang_lijst:
            return positie