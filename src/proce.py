import psycopg2
from conexion_sql import conexion

## Mostrar Usuarios
def mostrar_usuario():
    try:
        # Obtener el objeto de conexión a la base de datos
        conn = conexion()

        with conn.cursor() as cursor:
            # Ejecutar la función mostrar_usuario
            cursor.execute("SELECT * FROM mostrar_usuario_f()")
            
            registros = cursor.fetchall()
            for registro in registros:
                print("ID Cliente: {}, Nombre: {}, Dirección: {}, Teléfono: {}".format(registro[0], registro[1], registro[2], registro[4]))
            
            print("Función mostrar_usuario ejecutada correctamente")
    except psycopg2.Error as e:
        print("Ocurrió un error al consultar: ", e)
    finally:
        conn.close()


def crear_usuario():
    try:
        # Obtener el objeto de conexión a la base de datos
        conn = conexion()

        with conn.cursor() as cursor:
            # Ejecutar la función crear_usuario
            id_usuario = input('Id del Usuario: ')
            nombre_usuario = input('Nombre Uuario: ')
            direccion_usuario = input('Direccion Usuario: ')
            pais_usuario = input('Id del Pais: ')
            telefono_usuario = input('Telefono: ')

            cursor.callproc('crear_usuario_f2', [id_usuario, nombre_usuario, direccion_usuario, pais_usuario, telefono_usuario])

            # Confirmar los cambios en la base de datos
            conn.commit()

            print("Usuario creado correctamente")
    except psycopg2.Error as e:
        print("Ocurrió un error al crear el usuario: ", e)
    finally:
        conn.close()


def actualizar_usuario():
    try:
        # Obtener el objeto de conexión a la base de datos
        conn = conexion()

        with conn.cursor() as cursor:
            # Ejecutar la función crear_usuario
            id_usuario = input('Nuevo ID: ')
            nombre_usuario = input('Nuevo Nombre: ')
            direccion_usuario = input('Nueva Direcion: ')
            pais_usuario = input('Nuevo ID Pais: ')
            telefono_usuario = input('Nuevo Telefono: ')

            cursor.callproc('actualizar_usuario', [id_usuario, nombre_usuario, direccion_usuario, pais_usuario, telefono_usuario])

            # Confirmar los cambios en la base de datos
            conn.commit()

            print("Usuario actualizado correctamente")
    except psycopg2.Error as e:
        print("Ocurrió un error al crear el usuario: ", e)
    finally:
        conn.close()


def eliminar_usuario():
    try:
        # Obtener el objeto de conexión a la base de datos
        conn = conexion()

        with conn.cursor() as cursor:
            # Ejecutar el procedimiento almacenado para eliminar el usuario
            id_usuario = input('ID del Usuario a eliminar: ')
            cursor.execute("CALL eliminar_usuario(%s)", [id_usuario])


            # Confirmar los cambios en la base de datos
            conn.commit()

            print("Usuario eliminado correctamente")
    except psycopg2.Error as e:
        print("Ocurrió un error al eliminar el usuario: ", e)
    finally:
        conn.close()


def main():
    while True:
        operacion = input("Elige la Operacion: 1-Crear, 2-Listar, 3-Actualizar, 4-Eliminar, 0-Salir: ")

        if operacion == "1":
            crear_usuario()
        elif operacion == "2":
            mostrar_usuario()
        elif operacion == "3":
            actualizar_usuario()
        elif operacion == "4":
            eliminar_usuario ()
        elif operacion == "0":
            break
        else:
            print("Opción inválida. Por favor, elige una operación válida.")

if __name__ == "__main__":
    main()
