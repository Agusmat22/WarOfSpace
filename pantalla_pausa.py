import pygame
import funciones
import clases_genericas
import colores

def pantalla_pausa(ventana):

    flag_inicio = True

    foto_titulo = clases_genericas.Imagen('imagenes\\pausa.png',400,70,135,150)

    while flag_inicio: #pantalla de inicio

        lista_eventos = pygame.event.get()

        for evento in lista_eventos:

            if evento.type == pygame.QUIT:

                exit()

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_ESCAPE:

                    flag_inicio = False

                elif evento.key == pygame.K_z:

                    exit()
                    
        ventana.fill((0,0,0))
        foto_titulo.update(ventana)
        funciones.crear_titulo_pantalla(ventana,'"ESC" para renaudar',27,200,460,colores.BLANCO_BEIGE)
        funciones.crear_titulo_pantalla(ventana,'"Z"Salir sin guardar',27,200,560,colores.BLANCO_BEIGE)
        pygame.display.flip()