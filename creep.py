import random
import pygame
import core
from pygame.math import Vector2


class creep:
    def __int__(self):
        self.position = Vector2 (0,0)
        self.taille = 10
        self.couleur = (random.roudint(0,255),random.roudint(0,255),random.roudint(0,255))
        self.masse = 10

    def show (self, screen):
        pygame.draw.circle(screen,self.couleur,[int (self.position.x), int(self.position.y)], self.taille)
