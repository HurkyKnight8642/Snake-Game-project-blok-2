# besturing.py
import pygame

def verwerk_input(event, huidige_richting):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and huidige_richting != (0, 1):
            return (0, -1)
        if event.key == pygame.K_DOWN and huidige_richting != (0, -1):
            return (0, 1)
        if event.key == pygame.K_LEFT and huidige_richting != (1, 0):
            return (-1, 0)
        if event.key == pygame.K_RIGHT and huidige_richting != (-1, 0):
            return (1, 0)
    return huidige_richting