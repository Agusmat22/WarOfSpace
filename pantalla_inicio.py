import pygame
import funciones
import clases_genericas
import colores
from pantalla_instrucciones import pantalla_instrucciones

def pantalla_inicio(ventana):

    flag_inicio = True

    foto_titulo = clases_genericas.Imagen('imagenes\\titulo_inicio.png',550,70,70,110)

    fondo_inicio = clases_genericas.Imagen('imagenes\\fondo_inicio.jpg',700,780,0,0)

    while flag_inicio: #pantalla de inicio

        lista_eventos = pygame.event.get()

        for evento in lista_eventos:

            if evento.type == pygame.QUIT:

                exit()

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_SPACE:

                    flag_inicio = False

                if evento.key == pygame.K_z:

                    pantalla_instrucciones(ventana)
                    

        fondo_inicio.update(ventana)
        foto_titulo.update(ventana)

        funciones.crear_titulo_pantalla(ventana,'Presione:',27,275,305,colores.BLANCO_BEIGE)

        funciones.crear_titulo_pantalla(ventana,'"espacio" si desea jugar',22,205,420,colores.BLANCO_BEIGE)

        funciones.crear_titulo_pantalla(ventana,'"z" para visualizar las instrucciones',22,135,470,colores.BLANCO_BEIGE)
        pygame.display.flip()