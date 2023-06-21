import pygame
import laser
import sonido

sonido_disparo = sonido.reproducir_sonido('sonido\\FruitCollectedSound.wav',0.2)


class Nave:

    def __init__(self,img,ancho,alto,x,y) -> None:
        
        self._superficie = pygame.image.load(img)
        self._superficie = pygame.transform.scale(self._superficie,(ancho,alto))

        self._rect = self._superficie.get_rect()
        self._rect.x = x
        self._rect.y = y

        self._velocidad = 8  #velocidad de movimiento de la nave
        self._disparo = False
        self._velocidad_disparo = 9 

        #laser
        self._laser = laser.Laser('imagenes\\laser_blue.png',7,30)
        
        #score de la nave
        self._score = 0

        self._vida = 3 #vidas de la nave

        
    def mover(self,tipo,ancho_ventana):

        if tipo == 'right' and self._rect.x < ancho_ventana - 100:

            self._rect.x += self._velocidad

        elif tipo == 'left' and self._rect.x > 6:

            self._rect.x -= self._velocidad

    def disparar(self):

        if not self._disparo and self._vida > 0:

            self._disparo = True
            self._laser.rect.x = self.rect.x + 41
            self._laser.rect.y = self.rect.y - 25
            sonido_disparo.play()

    def resetear_nave(self):

        self.score = 0
        self.vida = 3
        self.rect.x = 315
        self.rect.y = 670 
        self._disparo = False
           
 
    def update(self,ventana):

        if self._vida > 0:

            if self._disparo == True:

                if self._laser.rect.y > 80: #100 ya que el juego comienza en 100 porque tiene la barra de score
                        
                    #velocidad del disparo
                    self._laser.rect.y -=  self._velocidad_disparo 
                
                else:
                    self._laser.rect.y = 2000 #PONGO UN NUMERO RANDOM PARA QUE EL RECTANGULO DESAPAREZCA 
                    self._disparo = False

                #ACTUALIZO EL LASER SIEMPRE Y CUANDO ESTE EN EJECUCION
                ventana.blit(self._laser.superficie,self._laser.rect)


            #actualiza la nave
            ventana.blit(self._superficie,(self._rect))

        else:

            self._laser.rect.y = 2000 #el disparo de la nave principal desaparece
            self._rect.x = 2000

    @property
    def visible(self):

        return self._nave_visible
    
    @property
    def superficie(self):

        return self._superficie
    
    @property
    def rect(self):

        return self._rect
    
    @property
    def laser(self):

        return self._laser
    
    @property
    def disparo(self):

        return self._disparo
    
    @property
    def score(self):

        return self._score
    
    @property
    def velocidad_disparo(self):

        return self._velocidad_disparo
    
    @property
    def vida(self):

        return self._vida
    
    @property
    def velocidad_movimiento(self):

        return self._velocidad
    
    
    @visible.setter
    def visible(self,valor):

        self._nave_visible = valor
    
    @laser.setter
    def disparo(self,valor):

        self._laser = valor

    @disparo.setter
    def disparo(self,disparo):

        self._disparo = disparo

    @score.setter
    def score(self,valor):

        self._score = valor

    @velocidad_disparo.setter
    def velocidad_disparo(self,valor):

        self._velocidad_disparo = valor

    @vida.setter
    def vida(self,valor):

        self._vida = valor

    @velocidad_movimiento.setter
    def velocidad_movimiento(self,valor):

        self._velocidad = valor
    
   
