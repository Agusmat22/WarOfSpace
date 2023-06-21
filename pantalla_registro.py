import pygame
import funciones
import colores
import clases_genericas
import re

def registro(ventana):

    flag_inicio = True

    advertencia = False


    nombre_jugador = ""

    while flag_inicio: #pantalla de inicio

        lista_eventos = pygame.event.get()

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

                                        
        fondo_registro = clases_genericas.Imagen('imagenes\\fondo_registro.jpg',700,780,0,0)

        ingrese_nombre = clases_genericas.Imagen('imagenes\\nombre.png',500,95,95,100)

        recuadro = clases_genericas.Imagen('imagenes\\formulario.png',330,85,190,350)

        fondo_registro.update(ventana)

        recuadro.update(ventana)

        ingrese_nombre.update(ventana)

        funciones.crear_titulo_pantalla(ventana,nombre_jugador,30,245,370,colores.BLANCO_BEIGE) #muestro por ventana lo que escribe el usuario

        if advertencia == True:

            funciones.crear_titulo_pantalla(ventana,'Error, debe ingresar al menos una letra',20,140,315,colores.BLANCO_BEIGE) #si ingresa una cadena vacia le indico el mensaje



        pygame.display.flip()