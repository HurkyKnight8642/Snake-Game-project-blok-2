# main.py
import pygame
import sys
import scherm
import slang
import eten
import botsing
import tekenen
import besturing
import instellingen

def main():
    pygame.init()
    venster = scherm.maak_scherm()
    klok = pygame.time.Clock()

    slang_lijst = slang.start_slang()
    richting = (1, 0)
    eten_positie = eten.spawn_eten(slang_lijst)
    score = 0

    spelen = True
    while spelen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            richting = besturing.verwerk_input(event, richting)

        gegeten = (slang_lijst[0][0] + richting[0], slang_lijst[0][1] + richting[1]) == eten_positie
        slang_lijst = slang.beweeg(slang_lijst, richting, gegeten)

        if gegeten:
            score += 1
            eten_positie = eten.spawn_eten(slang_lijst)

        if botsing.check_botsing(slang_lijst):
            spelen = False

        tekenen.teken_alles(venster, slang_lijst, eten_positie, score)
        pygame.display.flip()
        klok.tick(instellingen.SNELHEID)

    pygame.quit()

if __name__ == "__main__":
    main()