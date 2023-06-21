<!-- ENCABEZADO TITULO -->
# Proyecto: War of Space
![mi proyecto](img_juego\menu.png)


## Creador:
* Agustin Matias Garcia Navas

## Descripcion:

El juego esta creado con la biblioteca PYGAME en PYTHON. El mismo se trata de una nave que se encuentra en el espacio y debe confrontar con varios obstaculos, tiene 3 niveles con diversas dificultades. En cada nivel aparecen elementos que ayudaran a la nave o la perjudicaran. La nave contiene 3 vidas. 


## Especificaciones

El juego contiene:
* POO
* SQLite
* Eventos
* Colisiones
* Manipulacion de rectangulos
* Temporizador
* Imagenes
* Audios 
* Ranking de puntuaciones


## Instrucciones
En esta ventana indico las instrucciones para poder utilizar la nave principal.
![mi proyecto](img_juego\instrucciones.png)

Fragmento de codigo:
```python
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
```

## Registrarse
Luego antes de empezar a jugar de forma obligatoria antes el usuario debe registrarse ingresando su nombre, en caso que se ingrese una cadena vacia el juego le indicara un mensaje de aviso para que ingrese por lo menos una letra.
![mi proyecto](img_juego\registro.png)

Fragmento de codigo donde valido el dato ingresado:
```python
        for evento in lista_eventos:

            if evento.type == pygame.QUIT:

                exit()

            if evento.type == pygame.KEYDOWN:

                if evento.unicode:
                    #valido que se presione una tecla alfabetica y que no contenga mas de 10 caracteres
                    if len(nombre_jugador) < 10 and re.search('^[a-z]*$',evento.unicode,re.IGNORECASE):

                        nombre_jugador += evento.unicode


                    elif evento.key == pygame.K_BACKSPACE:

                        nombre_jugador = nombre_jugador[:-1] #borro el ultimo caracter

                if evento.key == pygame.K_RETURN: #presionar ENTER para enviar el nombre

                    if len(nombre_jugador) > 0:

                        return nombre_jugador

                    else:

                        advertencia = True

        if advertencia == True:

            funciones.crear_titulo_pantalla(ventana,'Error, debe ingresar al menos una letra',20,140,315,colores.BLANCO_BEIGE) #si ingresa una cadena vacia le indico el mensaje
```

## Nivel 1
En el nivel 1 se debe vencer a las naves que se dividen en 2 etapas. La primera etapa es hasta llegar a 9 puntos y pasa a la segunda etapa donde las naves enemigas tiene mayor velocidad de disparo. Se debe alcanzar los 18 puntos para poder pasar al siguiente nivel. El elemento que participara en este nivel es la pocion que le otorgara a la nave en caso de absorberse una vida EXTRA en caso de no contener las 3
![mi proyecto](img_juego\naves_enemigas.png)
Etapa 2:
![mi proyecto](img_juego\naves_enemigas_etapa2.png)

Fragmento de codigo donde contiene las colisiones entre las naves enemigas para que no se superpongan:
```python
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
```

## Nivel 2
En el nivel 2 se debera eliminar los asteroides hasta conseguir 35 puntos, en caso que un asteroide colisione con la nave esta misma perdera 1 vida y 5 puntos. El elemento que participara en este nivel es la velocidad, en caso que la nave consiga colisionar con este mismo le otorgara 8 segundos de velocidad de movimiento extra.
![mi proyecto](img_juego\asteroides.png)

Fragmento de codigo donde contiene las colisiones entre los disparos de la nave principal y los asteroides:
```python
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
```

## Nivel 3
En el nivel 3 se debera derrotar al boss final el cual contara con 11 vidas. Este mismo tendra movimiento al azar por la ventana y disparara en algunos momentos mas rapidos. El elemento que participara en este nivel es el de relentizar la nave principal. En vez de ser un beneficio seria todo lo contrario. 
![mi proyecto](img_juego\boss.png)

Fragmento de codigo donde contiene los movimiento de la nave enemiga:
```python
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
```

## Derrota
La ventana de derrota siempre se ejecutara cuando la nave principal tenga 0 vidas. Esta ventana permite volver a jugar sin guardar el score o guardar el score y salir del juego.
![mi proyecto](img_juego\derrota.png)

Funcion:
```python
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
```

## Victoria
La ventana victoria se ejecutara cuando se vence al boss final.
![mi proyecto](img_juego\victoria.png)

Funcion:
```python
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
```

## Ranking de puntuaciones
La ventana se ejecutara cuando gane o cuando pierda las 3 vidas. Esta funcion se conecta con una base de datos local donde se almacena cada jugador con su nombre y score. Y muestro los 10 mayores puntajes de mayor a menor.
![mi proyecto](img_juego\tabla_de_record.png)

Funcion:
```python
def tabla_record(ventana,score,nombre,vida):

    if score == 46 or vida == 0:

        registro_de_jugadores(nombre,score)

        flag_inicio = True

        while flag_inicio: #pantalla de inicio

            lista_eventos = pygame.event.get()

            for evento in lista_eventos:

                if evento.type == pygame.QUIT:

                    exit()

                if evento.type == pygame.KEYDOWN:

                    if evento.key == pygame.K_ESCAPE:

                        exit()

            #lectura de la lista
            lista_jugadores = obtener_jugadores()
            
            fondo_registro = clases_genericas.Imagen('imagenes\\fondo_record.jpg',700,780,0,0)
            
            fondo_registro.update(ventana)

            #TABLA DE JUGADORES
            mensaje_tabla = '|  Posicion  |  Nombre  |  Score  |'

            funciones.crear_titulo_pantalla(ventana,mensaje_tabla,40,40,80,colores.BLANCO_BEIGE)
            
            funciones.imprimir_lista_usuarios(lista_jugadores,ventana) #imprime la lista de usuarios

            #mensaje de salir
            funciones.crear_titulo_pantalla(ventana,'Salir (esc)',32,275,14,colores.ROJO_CLARO)

            pygame.display.flip()
```




<!-- ENLACE DIRECTO AL PROYECTO-->

## :movie_camera: Video del proyecto

* [Mi video](https://youtu.be/JbZabmW5bCw)