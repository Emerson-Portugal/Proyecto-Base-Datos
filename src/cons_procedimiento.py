import psycopg2
from conexion_sql import conexion

try:
    with conexion.cursor() as cursor:
        # Ejecutar la función mostrar_usuario
        cursor.execute("SELECT * FROM mostrar_usuario_f()")
        
        registros = cursor.fetchall()
        for registro in registros:
            print("ID Cliente: {}, Nombre: {}, Dirección: {}, Teléfono: {}".format(registro[0], registro[1], registro[2], registro[4]))
        
        print("Función mostrar_usuario ejecutada correctamente")
except psycopg2.Error as e:
    print("Ocurrió un error al consultar: ", e)
finally:
    conexion.close()
