import pygame
from abc import ABC, abstractmethod

BLOCK_SIZE = 50

class Surface(ABC): # Classe abstraite parente des classes Road, Grass, Checkpoint, Lava, Boost
    def __init__(self, x, y, color):
        """
        Constructeur 
        
        :params : x, y (integer), color (tuple) : position du bloc grass et color
            
        """
        self.__x_pos = x
        self.__y_pos = y
        self.__color = color
    
    """
    ========================= LES PROPERTIES ===========================
    """
    
    @property 
    def x_pos(self): # Coordonnée x récupérée dans Kart
        return self.__x_pos
    
    @property 
    def y_pos(self): # Coordonnée y récupérée dans Kart
        return self.__y_pos
    
    """
    ====================================================================
    """
    
    """
    ========================= METHODES DE SURFACE ===========================
    """
    def draw(self, screen):
        """
        Cette methode dessine un bloc de surface.

        :param screen: affichage de la fenêtre de jeu
         
        """
        pygame.draw.rect(screen, self.__color, (self.__x_pos, self.__y_pos, BLOCK_SIZE, BLOCK_SIZE))
        
    
    @abstractmethod
    def affect_kart(self, kart): # Méthode abstraite
        """
        Cette methode est implémentée dans les classes filles. 
        Elle permet d'adapter le comportement du kart selon la surface sur laquelle il se situe.
        
        :param kart (Kart): objet kart
        
        """
        pass
    
    """
    ========================= FIN METHODES DE SURFACE ===========================
    """