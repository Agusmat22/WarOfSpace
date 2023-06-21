import pygame
import funciones
import clases_genericas
import colores
import sonido



def pantalla_victoria(ventana,nave_principal):    

    if nave_principal.score == 46:

        flag_run = True

        foto_titulo_victoria = clases_genericas.Imagen('imagenes\\titulo_victoria.png',550,115,75,70)
        fondo_victoria = clases_genericas.Imagen('imagenes\\fondo_victoria.jpg',700,780,0,0)

        sonido_fondo = sonido.reproducir_sonido('sonido\\music_victoria.mp3',0.1)

        sonido_fondo.play(-1)
        while flag_run:


            lista_eventos = pygame.event.get()

            for evento in lista_eventos:

                if evento.type == pygame.QUIT:

                    exit()

                if evento.type == pygame.KEYDOWN:

                    if evento.key == pygame.K_a:
                        
                        sonido_fondo.stop()
                        return nave_principal

                

            fondo_victoria.update(ventana)
            foto_titulo_victoria.update(ventana)
            funciones.crear_titulo_pantalla(ventana,f'Score: {nave_principal.score}',35,265,650,colores.BLANCO_BEIGE)
            funciones.crear_titulo_pantalla(ventana,'A)Guardar el puntaje',25,200,720,colores.BLANCO_BEIGE)

            pygame.display.flip()


        


    