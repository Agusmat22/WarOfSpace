import funciones
import clases_genericas

lista_vidas = [clases_genericas.Imagen('imagenes\\vida.png',40,40,550,20),
                clases_genericas.Imagen('imagenes\\vida.png',40,40,600,20),
                clases_genericas.Imagen('imagenes\\vida.png',40,40,650,20),
]
    


def mostrar_barra_partida(ventana,score,vidas,nivel):

    img_borde = clases_genericas.Imagen('imagenes\\borde.jpg',700,80,0,0)
    
    img_borde.update(ventana)
    

    for i in range(vidas):

        lista_vidas[i].update(ventana)


    funciones.crear_titulo_pantalla(ventana,'Score: ',40,270,20,(255,255,255),score)
    funciones.crear_titulo_pantalla(ventana,'Nivel: ',30,20,25,(255,255,255),nivel)


#clases_genericas.crear_fondo_niveles()





