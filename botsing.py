# botsing.py
import instellingen

def check_botsing(slang_lijst):
    kop = slang_lijst[0]
    max_x = instellingen.BREEDTE // instellingen.GRID_GROOTTE
    max_y = instellingen.HOOGTE // instellingen.GRID_GROOTTE

    # Botsing met de rand
    if kop[0] < 0 or kop[0] >= max_x or kop[1] < 0 or kop[1] >= max_y:
        return True

    # Botsing met zichzelf
    if kop in slang_lijst[1:]:
        return True

    return False