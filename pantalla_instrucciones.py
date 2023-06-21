import pygame
import clases_genericas


def pantalla_instrucciones(ventana):

    flag_inicio = True

    fondo_instrucciones = clases_genericas.Imagen('imagenes\\fondo_instrucciones.jpg',700,780,0,0)

    while flag_inicio: #pantalla de inicio

        lista_eventos = pygame.event.get()

        for evento in lista_eventos:

            if evento.type == pygame.QUIT:

                exit()

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_ESCAPE:

                    flag_inicio = False
                    

        fondo_instrucciones.update(ventana)
        pygame.display.flip()