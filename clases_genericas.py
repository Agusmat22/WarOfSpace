import pygame

class Imagen:

    def __init__(self,img,ancho,alto,x,y) -> None:
        self._superficie = pygame.image.load(img)
        self._superficie = pygame.transform.scale(self._superficie,(ancho,alto))
        self._rect = self._superficie.get_rect()
        self._rect.x = x
        self._rect.y = y


    def update(self,ventana):

        ventana.blit(self._superficie,self._rect)