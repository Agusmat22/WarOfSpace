import pygame

def cargar_imagenes():

    lista_imagenes = []

    for i in range(7):

        imagen = pygame.image.load(f"imagenes\\explosion\\explo{i+1}.png") #imagenes\\explosion\\explo1.png
        imagen = pygame.transform.scale(imagen, (50, 50))
        lista_imagenes.append(imagen)
        

    return lista_imagenes

def explosion_nave_principal(ventana,nave_principal,fps,lista_imagenes,x,y):

    if nave_principal.vida == 0:

        indice = 0

        while True:

            if indice < len(lista_imagenes):

                ventana.blit(lista_imagenes[indice], (x, y))
                pygame.display.flip()
                indice +=1
                fps.tick(10)

            else:
                indice= 0
                break






class Explosion:

    def __init__(self) -> None:
        
        self._imagen = cargar_imagenes() #cargo los fragmentos de la explosion
        self._explotar = False
        self._x = None
        self._y = None
        self._indice = 0


    def update(self,ventana):

        if self._explotar == True:

            if self._indice < len(self._imagen):

                ventana.blit(self._imagen[self._indice], (self._x, self._y))

            else:
                self._explotar = False

                self._indice= 0  # Reinicia el índice para la próxima explosión


    @property
    def explotar(self):

        return self._explotar
    
    @property
    def x(self):

        return self._x
    
    @property
    def y(self):

        return self._y
    
    @property
    def indice(self):

        return self._indice
    
    @property
    def lista_imagenes(self):

        return self._imagen
    

    
    @explotar.setter
    def explotar(self,valor):

        self._explotar = valor

    @x.setter
    def x(self,valor):

        self._x = valor
    
    @y.setter
    def y(self,valor):

        self._y = valor

    @indice.setter
    def indice(self,valor):

        self._indice = valor
