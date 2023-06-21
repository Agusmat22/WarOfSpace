import random
import laser
from nave import Nave






def crear_lista_naves(ancho,alto,imagen):

    lista_naves_enemigas = []

    lista_x = [140,340,540]

    descuento_tiempo = 0

    for i in range(9):    #9 

        if i < 3:
            posicion_final_y = 300
            
            y = -150  

        elif i < 6:
            descuento_tiempo = 3
            posicion_final_y = 200
            y = -250 
        
        else:
            descuento_tiempo = 6
            posicion_final_y = 120
            y = -350 


        if i % 2 == 0: #para que se muevan de forma aleatoria

            direccion_mov = 'right'
        else:
            direccion_mov = 'left'

        nave_enemiga = NaveEnemiga(imagen,ancho,alto,lista_x[i-descuento_tiempo],y,i,direccion_mov,posicion_final_y)

        lista_naves_enemigas.append(nave_enemiga)

    return lista_naves_enemigas


#actualiza la lista de enemigos
def actualizar_pantalla_lista_enemigos(lista_enemigos,ventana,alto_ventana):

    for nave_enemiga in lista_enemigos:

        nave_enemiga.update(ventana,alto_ventana)



class NaveEnemiga(Nave):

    def __init__(self,img,ancho,alto,x,y,id,direccion_movimiento,pos_final) -> None:
        super().__init__(img,ancho,alto,x,y)

        self._laser = laser.Laser('imagenes\\laser_red.png',5,20)   #guardo el objeto en un atributo, preguntar al profesor si esta bien!!!!
        self._id = id
        self._direcion_movimiento = direccion_movimiento
        self._posicion_final_y = pos_final#random.randrange(100,400,50)   #indico el tope hasta donde puede bajar la nave
        self._velocidad = 2 #velocidad de moviemiento
        self._velocidad_bajada = 2
        self._vida = 1
        self._estado_movimiento = True


    def mover(self,ancho_ventana):
    
        if self._rect.y < self._posicion_final_y:

            self._rect.y += self._velocidad_bajada

        else:

        
            if self._estado_movimiento == True:

                if self._direcion_movimiento == 'right' and self._rect.x < ancho_ventana - 50:

                    self._rect.x += self._velocidad

                else:
                    self._direcion_movimiento = 'left'   #'left' = izquierda


                    if self._direcion_movimiento == 'left' and self._rect.x > 0:

                        self._rect.x -= self._velocidad

                    else:

                        self._direcion_movimiento = 'right' 


    def disparar(self):
        
        if not self._disparo and self._rect.y == self._posicion_final_y :  #valido que la nave alla ingresado a la ventana para disparar  CORREGIR ''  ''

            self._disparo = True
            self._laser.rect.x = self._rect.x + 20
            self._laser.rect.y = self._rect.y + 34


    def update(self,ventana,alto_ventana):

        #valido que la nave no hay colisionado con un laser
        if self._disparo == True:

            if self._laser.rect.y < alto_ventana + 100: #ya que el juego comienza desde la posicion Y100 por el score
                    
                #velocidad del disparo
                self._laser.rect.y += self._velocidad_disparo -2
            
            else:

                self._disparo = False

            #ACTUALIZO EL LASER SIEMPRE Y CUANDO ESTE EN EJECUCION
            ventana.blit(self._laser.superficie,self._laser.rect)


        #actualiza la nave
        ventana.blit(self._superficie,(self._rect))
    
   

    @property
    def id(self):

        return self._id

    
    @property
    def posicion_final_y(self):

        return self._posicion_final_y
    
    @property
    def direccion_movimiento(self):

        return self._direcion_movimiento
    
    @property
    def estado_movimiento(self):

        return self._estado_movimiento
    
    @property
    def pos_final(self):

        return self._posicion_final_y
    
    @direccion_movimiento.setter
    def direccion_movimiento(self,valor):

        self._direcion_movimiento = valor
    
    @estado_movimiento.setter
    def estado_movimiento(self,valor):

        self._estado_movimiento = valor
    


    
