import psycopg2

def conexion():
    try:
        credenciales = {
            "dbname": "Negocios",
            "user": "postgres",
            "password": "admin7895",
            "host": "localhost",
            "port": 8086
        }
        conn = psycopg2.connect(**credenciales)
        print("Conexión exitosa")
        return conn  # Devuelve la conexión creada
    except psycopg2.Error as e:
        print("Ocurrió un error al conectar a PostgreSQL: ", e)

