# tekenen.py
import pygame
import instellingen

def teken_alles(scherm, slang_lijst, eten_positie, score):
    scherm.fill(instellingen.ZWART)

    for segment in slang_lijst:
        rect = pygame.Rect(
            segment[0] * instellingen.GRID_GROOTTE,
            segment[1] * instellingen.GRID_GROOTTE,
            instellingen.GRID_GROOTTE,
            instellingen.GRID_GROOTTE
        )
        pygame.draw.rect(scherm, instellingen.GROEN, rect)

    eten_rect = pygame.Rect(
        eten_positie[0] * instellingen.GRID_GROOTTE,
        eten_positie[1] * instellingen.GRID_GROOTTE,
        instellingen.GRID_GROOTTE,
        instellingen.GRID_GROOTTE
    )
    pygame.draw.rect(scherm, instellingen.ROOD, eten_rect)

    font = pygame.font.SysFont(None, 30)
    tekst = font.render(f"Score: {score}", True, instellingen.WIT)
    scherm.blit(tekst, (10, 10))