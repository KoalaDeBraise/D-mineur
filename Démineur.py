import pygame
import sys 
from pygame import *

class objets:
    def __init__(self,screen):
        self.screen = screen
        self.lignes = [((60,0),(60,600)), ((120,0),(120,600)), ((180,0),(180,600)), ((240,0),(240,600)), ((300,0),(300,600)), ((360,0),(360,600)), ((420,0),(420,600)), ((480,0),(480,600)), ((540,0),(540,600)), ((0,60),(600,60)), ((0,120),(600,120)), ((0,180),(600,180)), ((0,240),(600,240)), ((0,300), (600,300)), ((0,360),(600,360)), ((0,420),(600,420)), ((0,480),(600,480)), ((0,540),(600,540))]

    def afficher(self):
        for lines in self.lignes:
            pygame.draw.line(self.screen,(0,0,0),lines[0],lines[1],2)

class jeu:
    def __init__(self):
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('Minesweeper')
        self.JeuAllumé = True
        self.objets = objets(self.screen)
    
    def fonctions(self):
        while self.JeuAllumé:
            for event in pygame.event.get():

                if event.type == pygame.QUIT: 
                    sys.exit()

            self.screen.fill((180, 180, 180))
            self.objets.afficher()
            pygame.display.flip()

if  __name__ == '__main__':
    pygame.init()
    jeu().fonctions()
    pygame.quit()