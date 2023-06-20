import psycopg2

try:
    credenciales = {
        "dbname": "Negocios",
        "user": "postgres",
        "password": "admin7895",
        "host": "localhost",
        "port": 8086
    }
    conexion = psycopg2.connect(**credenciales)
    print("Conexion Exitosa")
except psycopg2.Error as e:
    print("Ocurrió un error al conectar a PostgreSQL: ", e)