import pygame

class Laser:

    def __init__(self,img,ancho,alto) -> None:
        
        self._superficie = pygame.image.load(img)
        self._superficie = pygame.transform.scale(self._superficie,(ancho,alto))

        self._rect = self._superficie.get_rect()
        self._rect.x = 1000 #inicializo en este numero para que no moleste cuando se inicia el juego
        self._rect.y = 1000 #inicializo en este numero para que no moleste cuando se inicia el juego
         

        self._visible = False


    
    @property
    def rect(self):

        return self._rect
    
    
    @property
    def visible(self):
        
        return self._visible
    
    @property
    def superficie(self):

        return self._superficie


    
    @rect.setter
    def rect(self,valor):

        self._rect = valor

    @visible.setter
    def visible(self,valor):
        
        self._visible = valor

