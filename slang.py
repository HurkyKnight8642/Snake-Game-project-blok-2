# slang.py
import instellingen

def start_slang():
    # Begin met een slang van 1 segment, ongeveer in het midden
    start_x = (instellingen.BREEDTE // instellingen.GRID_GROOTTE) // 2
    start_y = (instellingen.HOOGTE // instellingen.GRID_GROOTTE) // 2
    return [(start_x, start_y)]

def beweeg(slang_lijst, richting, gegeten):
    kop_x, kop_y = slang_lijst[0]
    nieuwe_kop = (kop_x + richting[0], kop_y + richting[1])

    nieuwe_slang = [nieuwe_kop] + slang_lijst
    if not gegeten:
        nieuwe_slang.pop()  # staart weghalen als er niet gegeten is

    return nieuwe_slang