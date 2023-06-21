import pygame
import enemigos.asteroides as asteroides
import borde_score
import sonido
from pantalla_pausa import pantalla_pausa
import explosion
import clases_genericas
import herramienta



def nivel_2(ventana,nave_principal,fps,ancho_ventana,altura_ventana):

    fondo_nivel2 = clases_genericas.Imagen('imagenes\\space_2.jpg',ancho_ventana,780,0,0) #fondo pantalla

    #CREA LISTA DE ASTEROIDES
    lista_asteroides = asteroides.crear_lista_asteroides('imagenes\\asteroide.png',40,40)

    #TIEMPO PARA LA EXPLOSION
    tiempo = pygame.USEREVENT + 0
    pygame.time.set_timer(tiempo,70)

    animacion_explosion = explosion.Explosion()

    spawn_habilidad_velocidad = herramienta.Herramienta('imagenes\\elementos\\velocidad.png')

    #TIEMPO PARA SPAWNEAR VELOCIDAD EXTRA
    tiempo2 = pygame.USEREVENT + 1
    pygame.time.set_timer(tiempo2,15000)

    #TIEMPO PARA INDICAR CUANTO DURA LA HABILIDAD
    tiempo3 = pygame.USEREVENT + 2
    pygame.time.set_timer(tiempo3,8000)


    sonido_fondo = sonido.reproducir_sonido('sonido\\music_level22.mp3',0.1)
    sonido_fondo.play(-1)

    nivel = 2

    flag_run = True

    while flag_run:

        fps.tick(70)
        print(nave_principal.velocidad_movimiento)

        if nave_principal.score == 35 or nave_principal.vida <= 0:

            lista_asteroides = asteroides.resetear_lista_asteroides(lista_asteroides) #reseteo los asteroides de nuevo
            sonido_fondo.stop()
            nave_principal.velocidad_movimiento = 8 #restauro la velocidad de movimiento

            return nave_principal
        


        lista_eventos = pygame.event.get()
        
        for evento in lista_eventos:

            if evento.type == pygame.QUIT:

                exit()
            
            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_p:
                    #presiona P dispara la nave principal
                    nave_principal.disparar()

                if evento.key == pygame.K_ESCAPE:

                    pantalla_pausa(ventana)


            if animacion_explosion.explotar == True and evento.type == tiempo:

                animacion_explosion.indice += 1


            if evento.type == tiempo2:

                spawn_habilidad_velocidad.visible = True
            
            elif nave_principal.velocidad_movimiento != 8 and evento.type == tiempo3:

                nave_principal.velocidad_movimiento = 8



        spawn_habilidad_velocidad.mover()
        spawn_habilidad_velocidad.colision_velocidad(nave_principal,11)


        for asteroide in lista_asteroides:

            asteroide.mover(altura_ventana)

            if asteroide.rect.colliderect(nave_principal.laser.rect):

                animacion_explosion.explotar = True
                animacion_explosion.x = asteroide.rect.x
                animacion_explosion.y = asteroide.rect.y

                asteroide.resetear() #resatauro la posicion del asteroide
                
                nave_principal.disparo = False #cancelo el disparo ya que colisiono
                nave_principal.laser.rect.y = -2000 #MODIFICO LA POSICION DEL LASER AL COLISIONAR PARA QUE DESAPAREZCA DE LA IMAGEN
                nave_principal.score += 1 #POR CADA DISPARO ME SUMO UN PUNTO AL SCORE 
            
            elif nave_principal.rect.colliderect(asteroide.rect): #pregunta si algun asteroide toco a la nave principal

                nave_principal.vida -= 1
                nave_principal.score -= 5 #POR CADA DISPARO ME SUMO UN PUNTO AL SCORE

                asteroide.resetear()



        botones_presionados = pygame.key.get_pressed()

        if botones_presionados[pygame.K_RIGHT]:

            nave_principal.mover('right',ancho_ventana)
        
        elif botones_presionados[pygame.K_LEFT]:

            nave_principal.mover('left',ancho_ventana)




        fondo_nivel2.update(ventana)

        asteroides.actualizar_lista_asteroides(lista_asteroides,ventana)

        explosion.explosion_nave_principal(ventana,nave_principal,fps,animacion_explosion.lista_imagenes,nave_principal.rect.x,nave_principal.rect.y) 

        nave_principal.update(ventana)

        animacion_explosion.update(ventana)

        spawn_habilidad_velocidad.update(ventana)

        borde_score.mostrar_barra_partida(ventana,nave_principal.score,nave_principal.vida,nivel)

        pygame.display.flip()

    return nave_principal


