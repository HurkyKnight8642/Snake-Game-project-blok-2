# scherm.py
import pygame
import instellingen

def maak_scherm():
    scherm = pygame.display.set_mode((instellingen.BREEDTE, instellingen.HOOGTE))
    pygame.display.set_caption("Snake Game")
    return scherm