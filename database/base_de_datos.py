import sqlite3


def crear_tabla():

    with sqlite3.connect('database\\registros.db') as conexion:  #conecto con la base de datos  


        try:

            sentencia = ''' create table jugadores

                        (
                                id integer primary key autoincrement,
                                nombre text,
                                score real
                        )
                        '''
            
            conexion.execute(sentencia)

            print('Se creo la base de datos')

        except sqlite3.OperationalError:

            print('La table personaje ya existe')

    
def insertar_fila(nombre,score):

    with sqlite3.connect('Galaxian_2\\database\\bd_btf.db') as conexion:

        try:
            
            conexion.execute("insert into jugadores(nombre,score) values (?,?)", (nombre,score))
            conexion.commit()
            print('Se guardo al personaje correctamente')

            
        except:

            print('Error')


def mostrar_jugadores():

    with sqlite3.connect('database\\registros.db') as conexion:

        cursor=conexion.execute("SELECT * FROM jugadores")

        for fila in cursor:
            print(fila)


def eliminar_jugadores():

    with sqlite3.connect('database\\registros.db') as conexion:

        sentencia = "DELETE FROM jugadores WHERE id>5"
        cursor=conexion.execute(sentencia,(id,))
        conexion.commit()


def obtener_jugadores():

    with sqlite3.connect('database\\registros.db') as conexion:

        cursor = conexion.execute("SELECT nombre, score FROM jugadores ORDER BY score DESC LIMIT 10")
        jugadores = cursor.fetchall()
        return jugadores


############################################################
#creacion de registro de jugadores
def registro_de_jugadores(nombre:str,score:int):

    with sqlite3.connect('database\\registros.db') as conexion:  #conecto con la base de datos  

        try:
            
            conexion.execute("insert into jugadores(nombre,score) values (?,?)", (nombre,score))
            conexion.commit()
            print('Se guardo al personaje correctamente')
   
        except:

            print('Error')



    """ crear_tabla()
    insertar_fila(nombre,score) """




#crear_tabla()

