import pygame
import colores

def crear_titulo_pantalla(ventana,texto,tamaño,x,y,color,valor=None):
    #Round Pop
    font = pygame.font.SysFont("Round Pop", tamaño)

    if valor != None:

        text = font.render(f'{texto}{valor}', True, color)
    else:
        text = font.render(str(texto), True, color)

    ventana.blit(text,(x,y))

def imprimir_personaje(ventana,posicion,nombre,score,x,y):

    crear_titulo_pantalla(ventana,f'  {posicion}  ',30,x,y,colores.BLANCO_BEIGE) #x = 130  Y= 160
    crear_titulo_pantalla(ventana,nombre,30,x + 190,y,colores.BLANCO_BEIGE) #x = 320
    crear_titulo_pantalla(ventana,score,30,x + 410,y,colores.BLANCO_BEIGE) #x = 540

def imprimir_lista_usuarios(lista:list,ventana):

    x = 130
    y = 160

    for i in range(9):

        imprimir_personaje(ventana,i+1,lista[i][0],lista[i][1],x,y)

        y+=80




