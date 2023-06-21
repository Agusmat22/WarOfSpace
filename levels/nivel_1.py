import pygame
import random
#nave enemiga
import enemigos.nave_enemiga as nave_enemiga
#borde del juego
import borde_score
import sonido
import herramienta
from pantalla_pausa import pantalla_pausa
import explosion
import clases_genericas


def nivel_1(ventana,nave_principal,fps,ancho_ventana,altura_ventana):

    fondo_nivel1 = clases_genericas.Imagen('imagenes\\space_1.jpg',ancho_ventana,780,0,0)

    #nave enemiga
    lista_naves_enemigas = nave_enemiga.crear_lista_naves(45,45,'imagenes\\nave_enemiga.png')
    #para preguntar por el ID en el for la nave enemiga
    numero_random = 0

    #TIEMPO PARA LAS NAVES ENEMIGAS PARA QUE DISPAREN ETAPA 1
    tiempo = pygame.USEREVENT + 0
    pygame.time.set_timer(tiempo,600)

    #TIEMPO PARA LAS NAVES ENEMIGAS PARA QUE DISPAREN ETAPA 2
    tiempo2 = pygame.USEREVENT + 1
    pygame.time.set_timer(tiempo2,250)

    #TIEMPO PARA SPAWNEAR VIDAS
    tiempo3 = pygame.USEREVENT + 2
    pygame.time.set_timer(tiempo3,14000)

    #TIEMPO PARA LA EXPLOSION
    tiempo4 = pygame.USEREVENT + 3
    pygame.time.set_timer(tiempo4,70)

    spawn_vidas = herramienta.Herramienta('imagenes\\elementos\\vida.png')

    animacion_explosion = explosion.Explosion()


    bandera_disparo_enemigo = False #bandera para avisar cuando debe disparar

    sonido_fondo = sonido.reproducir_sonido('sonido\\music_nivel1.mp3',0.1)

    sonido_fondo.play(-1)
    nivel = 1

    flag_run = True

    flag_etapa = '1' #para mostrar la etapa de la primera tanda de naves y la segunda

    flag_empezar_jugar = False


    while flag_run:

        fps.tick(70)

        if nave_principal.score == 9 and flag_etapa == '1': #cambia a la etapa 2
            flag_etapa = '2'

            lista_naves_enemigas = nave_enemiga.crear_lista_naves(45,45,'imagenes\\nave_enemiga2.png')

            flag_empezar_jugar = False
            nave_principal.rect.x = 315


        elif nave_principal.score == 18 or nave_principal.vida == 0: #retorno el valor ya que completo el nivel 1

            lista_naves_enemigas = nave_enemiga.crear_lista_naves(45,45,'imagenes\\nave_enemiga.png') #restauro las naves iniciales por si se quiere volver a empezar

            sonido_fondo.stop()

            return nave_principal


        lista_eventos = pygame.event.get()
        
        for evento in lista_eventos:

            if evento.type == pygame.QUIT:

                exit()
            
            if evento.type == pygame.KEYDOWN:

                if flag_empezar_jugar == True and evento.key == pygame.K_p:
                    #presiona P dispara la nave principal
                    nave_principal.disparar()

                if evento.key == pygame.K_ESCAPE:

                    pantalla_pausa(ventana)

            if flag_etapa == '1' and evento.type == tiempo:

                bandera_disparo_enemigo = True
                numero_random = random.randrange(0,len(lista_naves_enemigas),1)



            elif flag_etapa == '2' and evento.type == tiempo2:

                bandera_disparo_enemigo = True
                numero_random = random.randrange(0,len(lista_naves_enemigas),1)

            
            if evento.type == tiempo3:
                
                spawn_vidas.visible = True


            if animacion_explosion.explotar == True and evento.type == tiempo4:

                animacion_explosion.indice += 1
                


        #SPAWN DE HERRAMIENTAS QUE BRINDA VIDAS
        spawn_vidas.mover()
        spawn_vidas.colision_vida(nave_principal)


              
        for i,enemigo in enumerate(lista_naves_enemigas):
                
            enemigo.mover(ancho_ventana)


            if enemigo.rect.colliderect(nave_principal.laser.rect):  #pregunto si colisiono el laser de la nave principal con la nave enemiga
            
                nave_principal.disparo = False #si colisiona el laser de la nave principal desaparece
                nave_principal.laser.rect.y = 2000
                nave_principal.score += 1

                animacion_explosion.explotar = True
                animacion_explosion.x = enemigo.rect.x
                animacion_explosion.y = enemigo.rect.y

                enemigo.rect.y  = 3000 # quito la nave enemiga de la ventana

                lista_naves_enemigas.remove(enemigo) #elimino la nave de la lista


            elif nave_principal.rect.colliderect(enemigo.laser.rect): #pregunto si la nave_principal colisiono con el laser enemigo

                nave_principal.vida -= 1

                enemigo.laser.rect.y = 3000
            
        

            if i == numero_random and bandera_disparo_enemigo == True:

                enemigo.disparar()

                bandera_disparo_enemigo = False


            for otro_enemigo in lista_naves_enemigas:

                if enemigo != otro_enemigo and enemigo.rect.y == enemigo.pos_final and otro_enemigo.rect.y == otro_enemigo.pos_final:

                    flag_empezar_jugar = True #indico que la nave principal se puede mover

                    if enemigo.rect.colliderect(otro_enemigo.rect):
                        #print('Colisiono')

                        if enemigo.direccion_movimiento == 'right':

                            enemigo.direccion_movimiento = 'left'
                            otro_enemigo.direccion_movimiento = 'right'

                            enemigo.rect.x -= 5 
                            otro_enemigo.rect.x += 5 
                        
                        else:

                            enemigo.direccion_movimiento = 'right'
                            otro_enemigo.direccion_movimiento = 'left'

                            enemigo.rect.x += 5 
                            otro_enemigo.rect.x -= 5 

                        break #rompo el for cada vez que colisiona para que no siga preguntando
                 


                if len(lista_naves_enemigas) == 3: #aumento la dificultad (velocidad del disparo) cuando quedan 3 anves

                    enemigo.velocidad_disparo = 11

                elif len(lista_naves_enemigas) == 1:

                    enemigo.velocidad_disparo = 13



        if flag_empezar_jugar == True: #permito mover al personaje

            botones_presionados = pygame.key.get_pressed()

            if botones_presionados[pygame.K_RIGHT]:

                nave_principal.mover('right',ancho_ventana)
            
            elif botones_presionados[pygame.K_LEFT]:

                nave_principal.mover('left',ancho_ventana)
 


        fondo_nivel1.update(ventana)

        #actualizo las naves enemigas en el nivel 1
        nave_enemiga.actualizar_pantalla_lista_enemigos(lista_naves_enemigas,ventana,altura_ventana)

        spawn_vidas.update(ventana)

        explosion.explosion_nave_principal(ventana,nave_principal,fps,animacion_explosion.lista_imagenes,nave_principal.rect.x,nave_principal.rect.y) 


        nave_principal.update(ventana) #nave principal siempre la actualizo no importa el nivel


        animacion_explosion.update(ventana)

        borde_score.mostrar_barra_partida(ventana,nave_principal.score,nave_principal.vida,nivel)

        
        pygame.display.flip()


