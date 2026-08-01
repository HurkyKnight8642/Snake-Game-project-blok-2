import random
import sys

import pygame

from instellingen import (
    FPS,
    GROEN,
    ROOD,
    VENSTER_BREEDTE,
    VENSTER_HOOGTE,
    VAK_GROOTTE,
    WIT,
    ZWART,
)


def spawn_eten(slang, cols, rows):
    while True:
        x = random.randint(0, cols - 1)
        y = random.randint(0, rows - 1)
        positie = (x, y)
        if positie not in slang:
            return positie


def teken_achtergrond(venster):
    venster.fill(ZWART)


def teken_slang(venster, slang):
    for x, y in slang:
        rect = pygame.Rect(x * VAK_GROOTTE, y * VAK_GROOTTE, VAK_GROOTTE, VAK_GROOTTE)
        pygame.draw.rect(venster, GROEN, rect)


def teken_eten(venster, eten):
    x, y = eten
    rect = pygame.Rect(x * VAK_GROOTTE, y * VAK_GROOTTE, VAK_GROOTTE, VAK_GROOTTE)
    pygame.draw.rect(venster, ROOD, rect)


def teken_score(venster, score):
    font = pygame.font.SysFont(None, 28)
    tekst = font.render(f"Score: {score}", True, WIT)
    venster.blit(tekst, (10, 10))


def main():
    pygame.init()
    scherm = pygame.display.set_mode((VENSTER_BREEDTE, VENSTER_HOOGTE))
    pygame.display.set_caption("Snake")
    klok = pygame.time.Clock()

    cols = VENSTER_BREEDTE // VAK_GROOTTE
    rows = VENSTER_HOOGTE // VAK_GROOTTE

    slang = [
        (cols // 2, rows // 2),
        (cols // 2 - 1, rows // 2),
        (cols // 2 - 2, rows // 2),
    ]
    richting = (1, 0)
    eten = spawn_eten(slang, cols, rows)
    score = 0
    game_over = False
    move_timer = 0
    move_interval = 1000 // FPS

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if game_over:
                    if event.key in (pygame.K_RETURN, pygame.K_r):
                        slang = [
                            (cols // 2, rows // 2),
                            (cols // 2 - 1, rows // 2),
                            (cols // 2 - 2, rows // 2),
                        ]
                        richting = (1, 0)
                        eten = spawn_eten(slang, cols, rows)
                        score = 0
                        game_over = False
                        move_timer = 0
                else:
                    if event.key == pygame.K_LEFT and richting != (1, 0):
                        richting = (-1, 0)
                    elif event.key == pygame.K_RIGHT and richting != (-1, 0):
                        richting = (1, 0)
                    elif event.key == pygame.K_UP and richting != (0, 1):
                        richting = (0, -1)
                    elif event.key == pygame.K_DOWN and richting != (0, -1):
                        richting = (0, 1)

        if not game_over:
            move_timer += klok.tick(FPS)
            if move_timer >= move_interval:
                move_timer = 0
                dx, dy = richting
                kop_x, kop_y = slang[0]
                nieuwe_kop = (kop_x + dx, kop_y + dy)

                if (
                    nieuwe_kop[0] < 0
                    or nieuwe_kop[0] >= cols
                    or nieuwe_kop[1] < 0
                    or nieuwe_kop[1] >= rows
                    or nieuwe_kop in slang[1:]
                ):
                    game_over = True
                else:
                    slang.insert(0, nieuwe_kop)
                    if nieuwe_kop == eten:
                        score += 1
                        eten = spawn_eten(slang, cols, rows)
                    else:
                        slang.pop()

        teken_achtergrond(scherm)
        teken_slang(scherm, slang)
        teken_eten(scherm, eten)
        teken_score(scherm, score)

        if game_over:
            font = pygame.font.SysFont(None, 48)
            tekst = font.render("Game Over", True, WIT)
            scherm.blit(tekst, (VENSTER_BREEDTE // 2 - 90, VENSTER_HOOGTE // 2 - 20))
            font2 = pygame.font.SysFont(None, 28)
            tekst2 = font2.render("Druk Enter of R om opnieuw te starten", True, WIT)
            scherm.blit(tekst2, (VENSTER_BREEDTE // 2 - 140, VENSTER_HOOGTE // 2 + 20))

        pygame.display.flip()


if __name__ == "__main__":
    main()
