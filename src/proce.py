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

## Crear Usuarios
def crear_usuario():
    try:
        # Obtener el objeto de conexión a la base de datos
        conn = conexion()

        with conn.cursor() as cursor:
            # Ejecutar la función crear_usuario
            id_usuario = input("ID Cliente: ")
            nombre_usuario = input("Nombre: ")
            direccion_usuario = input("Dirección: ")
            pais_usuario = input("ID País: ")
            telefono_usuario = input("Teléfono: ")

            cursor.execute(f"SELECT crear_usuario_f2('{id_usuario}', '{nombre_usuario}', '{direccion_usuario}', '{pais_usuario}', '{telefono_usuario}')")

            print("Función crear_usuario ejecutada correctamente")
    except psycopg2.Error as e:
        print("Ocurrió un error al consultar: ", e)
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
            # Agrega aquí la lógica para la operación de actualización
            pass
        elif operacion == "4":
            # Agrega aquí la lógica para la operación de eliminación
            pass
        elif operacion == "0":
            break
        else:
            print("Opción inválida. Por favor, elige una operación válida.")

if __name__ == "__main__":
    main()
