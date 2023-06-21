import pygame
import pantalla_inicio
import nave
import sonido
import levels.nivel_1 as nivel_1
import levels.nivel_2 as nivel_2
import levels.nivel_3 as nivel_3
from pantalla_derrota import pantalla_derrota
import pantalla_registro
import pantalla_record
from pantalla_victoria import pantalla_victoria

pygame.init()

#DIMENSIONES DE LA VENTANA PRINCIPAL
ANCHO_VENTANA = 700
ALTURA_VENTANA = 780

#DIMENSIONES PARA LOS NIVELES
ANCHO_VENTANA_NIVELES = 700
ALTURA_VENTANA_NIVELES = 700

RELOJ = pygame.time.Clock()

#sonido
sonido_fondo = sonido.reproducir_sonido_fondo(0.1)

#creo ventana del juego
ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTURA_VENTANA))
pygame.display.set_caption('War of Space')

pygame.mouse.set_visible(False) #HAGO INVISIBLE EL MOUSE EN EL JUEGO

#nave principal
nave_principal = nave.Nave('imagenes\\nave.png',90,90,315,670)

#nombre del jugador
nombre_jugador = ""

#ingreso al menu por primera vez
flag_menu = True

#ejecucion del juego
ejecucion_game = True

while ejecucion_game:

    if flag_menu == True:

        flag_menu = False

        sonido_fondo.play(-1)

        pantalla_inicio.pantalla_inicio(ventana) #INICIO DEL JUEGO

        nombre_jugador = pantalla_registro.registro(ventana)
        
        sonido_fondo.stop() #freno el sonido inicial    


    nave_principal = nivel_1.nivel_1(ventana,nave_principal,RELOJ,ANCHO_VENTANA_NIVELES,ALTURA_VENTANA_NIVELES) 
    nave_principal = nivel_2.nivel_2(ventana,nave_principal,RELOJ,ANCHO_VENTANA_NIVELES,ALTURA_VENTANA_NIVELES) 
    nave_principal = nivel_3.nivel_3(ventana,nave_principal,RELOJ,ANCHO_VENTANA_NIVELES,ALTURA_VENTANA_NIVELES)


    pantalla_derrota(ventana,nave_principal)
        
    pantalla_victoria(ventana,nave_principal)
                
    
    if nave_principal.vida == 0:

        ejecucion_game = False 


    sonido_fondo.play(-1)

    pantalla_record.tabla_record(ventana,nave_principal.score,nombre_jugador,nave_principal.vida)

    sonido_fondo.stop()
     
    

pygame.quit()