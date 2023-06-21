import pygame
import clases_genericas
import funciones
import colores
from database.base_de_datos import registro_de_jugadores
from database.base_de_datos import obtener_jugadores



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
