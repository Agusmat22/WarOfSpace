import pygame
import funciones
import clases_genericas
import colores
import sonido

""" ME FALTA PENSAR LA LOGICA, CONTINUARLO """


def pantalla_derrota(ventana,nave_principal):

    if nave_principal.vida == 0: 

        flag_run = True

        foto_titulo_derrota = clases_genericas.Imagen('imagenes\\derrota.png',550,70,70,110)

        fondo_derrota = clases_genericas.Imagen('imagenes\\fondo_final_derrota.jpg',700,780,0,0)

        sonido_fondo = sonido.reproducir_sonido('sonido\\music_derrota.mp3',0.1)

        sonido_fondo.play()

        while flag_run:


            lista_eventos = pygame.event.get()

            for evento in lista_eventos:

                if evento.type == pygame.QUIT:

                    exit()

                if evento.type == pygame.KEYDOWN:

                    if evento.key == pygame.K_a:

                        nave_principal.resetear_nave()
                        
                        sonido_fondo.stop()

                        return nave_principal

                    elif evento.key == pygame.K_b:

                        sonido_fondo.stop()

                        return nave_principal


            fondo_derrota.update(ventana)
            foto_titulo_derrota.update(ventana)
            funciones.crear_titulo_pantalla(ventana,f'Score: {nave_principal.score}',45,240,340,colores.BLANCO_BEIGE)
            funciones.crear_titulo_pantalla(ventana,'A) Volver a jugar',27,140,590,colores.BLANCO_BEIGE)
            funciones.crear_titulo_pantalla(ventana,'B) Guardar el puntaje y salir',27,140,650,colores.BLANCO_BEIGE)

            pygame.display.flip()


        


    