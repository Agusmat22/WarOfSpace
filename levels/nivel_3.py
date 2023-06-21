import pygame
#borde del juego
import borde_score
#boss
import enemigos.boss_enemigo as boss_enemigo
import sonido
import random
from pantalla_pausa import pantalla_pausa
import clases_genericas
import herramienta
import explosion


""" HICE EL INICIO DEL JUEGO, TRATAR DE DISMINUIR CODIGO Y QUE QUEDE MAS LIMPIO """

def nivel_3(ventana,nave_principal,fps,ancho_ventana,altura_ventana):

    fondo_nivel3 = clases_genericas.Imagen('imagenes\\space_3.jpg',ancho_ventana,780,0,0) #fondo pantalla

    #boss
    boss = boss_enemigo.Boss('imagenes\\boss_1.png',150,150,320,-100)

    animacion_explosion = explosion.Explosion()

    #TIEMPO PARA EXPLOTAR NAVE PRINCIPAL
    tiempo6 = pygame.USEREVENT + 4
    pygame.time.set_timer(tiempo6,70)

    #TIEMPO PARA EL DISPARO DEL BOSS
    tiempo = pygame.USEREVENT + 0
    pygame.time.set_timer(tiempo,600)

    #TIEMPO PARA MOVER CAMBIAR LA DIRECCION DE MOVIMIENTO DEL BOSS
    tiempo2 = pygame.USEREVENT + 1
    pygame.time.set_timer(tiempo2,1500)

    spawn_relentizador = herramienta.Herramienta('imagenes\\elementos\\paralisis.png')

    #TIEMPO PARA SPAWNEAR RELENTIZADOR DE VELOCIDAD
    tiempo3 = pygame.USEREVENT + 2
    pygame.time.set_timer(tiempo3,5000)

    #TIEMPO PARA INDICAR CUANTO DURA LA HABILIDAD aplicada
    tiempo4 = pygame.USEREVENT + 3
    pygame.time.set_timer(tiempo4,3000)

    #TIEMPO PARA AUMENTAR LA VELOCIDAD DEL DISPARO DEL BOSS
    tiempo7 = pygame.USEREVENT + 5
    pygame.time.set_timer(tiempo7,5000)

    #TIEMPO DURABILIDAD DE DICHA MODIFICACION
    tiempo8 = pygame.USEREVENT + 6
    pygame.time.set_timer(tiempo8,3000)

    sonido_fondo = sonido.reproducir_sonido('sonido\\music_level3.mp3',0.1)

    nivel = 3

    flag_run = True

    sonido_fondo.play(-1)


    while flag_run:


        #indico que den 70 vueltas por segundo en el bucle
        fps.tick(70)

        if nave_principal.score == 46 or nave_principal.vida == 0:
            
            boss.resetear_boss()
            sonido_fondo.stop()

            return nave_principal
        
        

        lista_eventos = pygame.event.get()
        
        for evento in lista_eventos:

            if evento.type == pygame.QUIT:

                flag_run = False  #CORROBORAR DESPUES Y ELIMINAR YA QUE EXIT SALE DIRECTAMENTE DEL JUEGO
                exit()
            
            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_p:
                    #presiona P dispara la nave principal
                    nave_principal.disparar()
                
                if evento.key == pygame.K_ESCAPE:

                    pantalla_pausa(ventana)


            if animacion_explosion.explotar == True:

                animacion_explosion.indice += 1


            if evento.type == tiempo: #temporizador para disparar

                boss.disparar()

            if evento.type  == tiempo2: #sirve para mover la nave de forma aleatoria 

                valor_aleatorio = random.randrange(1,3,1)

                if valor_aleatorio == 1:

                    boss.direccion_movimiento = 'left'

                else:

                    boss.direccion_movimiento = 'right'


            if evento.type == tiempo3:

                spawn_relentizador.visible = True

            elif nave_principal.velocidad_movimiento != 8 and evento.type == tiempo4:

                nave_principal.velocidad_movimiento = 8


            if evento.type == tiempo7: #aumenta la velocidad del disparo en el boss

                boss.velocidad_disparo = 13

            elif boss.velocidad_disparo != 9 and evento.type == tiempo8:

                boss.velocidad_disparo = 9

            

        
        spawn_relentizador.mover() #elemento que relentiza la nave si colisiona
        spawn_relentizador.colision_velocidad(nave_principal,3)
    

        if boss.vida > 0 and boss.rect.colliderect(nave_principal.laser.rect):

            boss.vida -=1 #le resto una vida
            
            nave_principal.disparo = False #si colisiona el laser de la nave principal desaparece
            nave_principal.laser.rect.y = 2000
            nave_principal.score += 1

            if boss.vida == 0:

                boss.nave_visible = False
                boss.rect.y  = 3000 #random.randrange(-300,1000,35) (no me acuerdo porque hice esto, NO ELIMINAR POR AHORA)
                boss.laser.rect.x = 3000
                boss.laser.rect.y = 3000
    
        elif nave_principal.rect.colliderect(boss.laser.rect): #pregunto si la nave_principal colisiono con la bola de poder del boss

            nave_principal.vida -= 1
            
            boss.laser.rect.y = 2000 #EL DISPARO DEL ENEMIGO LO SACO DE LA VENTANA ASI NO ME SIGUE IMPACTANDO



        boss.mover(ancho_ventana) #EL BOSS SE MUEVE

        botones_presionados = pygame.key.get_pressed()

        if botones_presionados[pygame.K_RIGHT]:

            nave_principal.mover('right',ancho_ventana)
        
        elif botones_presionados[pygame.K_LEFT]:

            nave_principal.mover('left',ancho_ventana)



        fondo_nivel3.update(ventana)
        boss.update(ventana,altura_ventana)
        animacion_explosion.update(ventana)

        explosion.explosion_nave_principal(ventana,nave_principal,fps,animacion_explosion.lista_imagenes,nave_principal.rect.x,nave_principal.rect.y) 
            
        spawn_relentizador.update(ventana)
        nave_principal.update(ventana)

        borde_score.mostrar_barra_partida(ventana,nave_principal.score,nave_principal.vida,nivel)


        pygame.display.flip()

    return nave_principal

#pygame.quit()

