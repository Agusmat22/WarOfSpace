import pygame
import random


def crear_lista_asteroides(img,ancho,alto):

    lista_asteroides = []

    for i in range(11):

        velocidad = random.randrange(2,7,1) #le doy una velocidad random de movimiento

        asteroide_nuevo = Asteroide(img,ancho,alto,velocidad)

        lista_asteroides.append(asteroide_nuevo)

    return lista_asteroides


def actualizar_lista_asteroides(lista_asteroides:list,ventana):

    for asteroide in lista_asteroides:

        asteroide.update(ventana)

def resetear_lista_asteroides(lista_asteroides):

    for asteroide in lista_asteroides:

        asteroide.resetear()

    return lista_asteroides


class Asteroide:  #creo el asteroide

    def __init__(self,img,ancho,alto,velocidad) -> None:
        
        self._superficie = pygame.image.load(img)
        self._superficie = pygame.transform.scale(self._superficie,(ancho,alto))
        
        self._rect = self._superficie.get_rect()
        self._rect.y = random.randrange(-700,-100,70)
        self._rect.x = random.randrange(30,660,70)
        self._velocidad = velocidad #velocidad a la que baja el asteroide


    def mover(self,altura_ventana):

        if self._rect.y < altura_ventana + 80:

            self._rect.y += self._velocidad

        else:

            self._rect.y = random.randrange(-700,-100,70)
            self._rect.x = random.randrange(30,660,70)

    def resetear(self):

        self._rect.y = random.randrange(-700,-100,70)
        self._rect.x = random.randrange(30,660,70)



    def update(self,ventana):

        ventana.blit(self._superficie,(self._rect))


    @property
    def superficie(self):

        return self._superficie
    
    @property
    def rect(self):

        return self._rect


