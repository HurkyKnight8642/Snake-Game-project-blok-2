# besturing.py - eigenaar: Moenes
# Leest het toetsenbord uit en bepaalt de richting.
# Een richting is een tuple: (0, -1) = omhoog, (0, 1) = omlaag,
# (-1, 0) = links, (1, 0) = rechts

# lees_toets(huidige_richting)
#   Kijkt welke pijltjestoets is ingedrukt en geeft de nieuwe richting terug.
#   Als er niets is ingedrukt: geef de huidige richting terug.
#   Voorkomt dat de slang direct omkeert (bijv. van links naar rechts).