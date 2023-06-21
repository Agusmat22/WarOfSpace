import pygame
import random
import sonido

sonido_herramienta = sonido.reproducir_sonido('sonido\\absorber_vida.mp3',0.1)


class Herramienta:

    def __init__(self,img) -> None:
        self._superficie = pygame.image.load(img)
        self._superficie = pygame.transform.scale(self._superficie,(35,35))
        self._rect= self._superficie.get_rect()
        self._rect.x = random.randrange(20,650,50)
        self._rect.y = -300
        self._velocidad = 5
        self._visible = False


    def mover(self):

        if self._visible == True and self._rect.y < 850:

            self._rect.y += self._velocidad

        else:

            self._rect.x = random.randrange(20,650,50)
            self._rect.y = -300
            self._visible = False

    def colision_vida(self,nave_principal):

        if self._rect.colliderect(nave_principal.rect):

            if nave_principal.vida < 3:

                nave_principal.vida += 1
                self._visible = False
                self._rect.y = -300
                sonido_herramienta.play()

    
    def colision_velocidad(self,nave_principal,velocidad):

        if self._rect.colliderect(nave_principal.rect):

            nave_principal.velocidad_movimiento = velocidad
            self._visible = False
            self._rect.y = -300
            sonido_herramienta.play()




    def update(self,ventana):

        if self._visible == True:

            ventana.blit(self._superficie,(self._rect))


    @property
    def visible(self):

        return self._visible
    
    

    
    @visible.setter
    def visible(self,valor):

        self._visible = valor








