import pygame
import laser
from enemigos.nave_enemiga import NaveEnemiga

lista_barra_vida = [ pygame.image.load('imagenes\\vida_boss\\vidas11.png'),
                    pygame.image.load('imagenes\\vida_boss\\vidas10.png'),
                    pygame.image.load('imagenes\\vida_boss\\vidas9.png'),
                    pygame.image.load('imagenes\\vida_boss\\vidas8.png'),
                    pygame.image.load('imagenes\\vida_boss\\vidas7.png'),
                    pygame.image.load('imagenes\\vida_boss\\vidas6.png'),
                    pygame.image.load('imagenes\\vida_boss\\vidas5.png'),
                    pygame.image.load('imagenes\\vida_boss\\vidas4.png'),
                    pygame.image.load('imagenes\\vida_boss\\vidas3.png'),
                    pygame.image.load('imagenes\\vida_boss\\vidas2.png'),
                    pygame.image.load('imagenes\\vida_boss\\vidas1.png'),           
]



def reescalar_imagen(lista_imagenes,ancho,alto):

    lista_reescalada = []

    for imagen in lista_imagenes:

        imagen_escalada = pygame.transform.scale(imagen,(ancho,alto))

        lista_reescalada.append(imagen_escalada)

    return lista_reescalada




#EL BOSS
class Boss(NaveEnemiga):

    def __init__(self, img, ancho, alto, x, y) -> None:
        super().__init__(img, ancho, alto, x, y,id,direccion_movimiento=None,pos_final=None) #heredo el valor de mi clase padre

        self._rect.y = -150
        self._posicion_final_y = 350
        self._direcion_movimiento_vertical = 'down'
        self._vida = 11 #le creo el atributo vidas para que resista a 11 disparos
        self._laser = laser.Laser('imagenes\\bola_poder_2.png',50,40)
        self._velocidad = 3.5 #velocidad de moviemiento

        self._barra_vida = reescalar_imagen(lista_barra_vida,120,35)
        self._rect_vida = self._barra_vida[0].get_rect()
        

    def mover(self,ancho_ventana): 

        #modifico el tipo de movimiento respecto a las naves enemigas
        if self._direcion_movimiento_vertical == 'down' and self._rect.y < self._posicion_final_y: #baja

            self._rect.y += self._velocidad

        else:

            self._direcion_movimiento_vertical = 'up'

            if self._direcion_movimiento_vertical == 'up' and self._rect.y > 110: #sube

                self._rect.y -= self._velocidad
            else:

                self._direcion_movimiento_vertical = 'down'

        if self._direcion_movimiento == 'right' and self._rect.x < ancho_ventana - 150:

            self._rect.x += self._velocidad

        else:
            self._direcion_movimiento = 'left'   #'left' = izquierda


            if self._direcion_movimiento == 'left' and self._rect.x > 0:

                self._rect.x -= self._velocidad

            else:

                self._direcion_movimiento = 'right'


    def disparar(self):

        if not self._disparo and self._rect.y > 140:

            self._disparo = True
            self._laser.rect.x = self._rect.x + 35
            self._laser.rect.y = self._rect.y + 110
    
    
    def resetear_boss(self):

        self._rect.y = -300

        self._disparo = False

        self._vida = 11



    def update(self, ventana, alto_ventana):

        #valido que la nave no hay colisionado con un laser
        if self._vida > 0:

            if self._disparo == True:

                if self._laser.rect.y < alto_ventana + 120:
                        
                    #velocidad del disparo
                    self._laser.rect.y += self._velocidad_disparo
                
                else:

                    self._disparo = False

                #ACTUALIZO EL LASER SIEMPRE Y CUANDO ESTE EN EJECUCION
                ventana.blit(self._laser.superficie,self._laser.rect)


            #actualiza la nave
            ventana.blit(self._superficie,(self._rect))
            self._rect_vida.x = self._rect.x + 11     # ACTUALIZO LA POSICON DE LA BARRA DE VIDA ACA ASI ESTA A LA PAR DEL MOVIMIENTO DEL BOSS
            self._rect_vida.y = self._rect.y - 30 
            ventana.blit(self._barra_vida[self._vida-1],(self._rect_vida))


