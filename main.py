import psycopg2 

import config

connection = psycopg2.connect(
    host="localhost",
    database="pruebasdata",
    user="postgres",
    password=config.password,
    port="5432"
)

connection.autocommit = True
print(connection)

def crear_tabla():
    cursor = connection.cursor()
    query = "CREATE TABLE customers(customerid INT PRIMARY KEY, name VARCHAR(50), occupation VARCHAR(50), email VARCHAR(50), company VARCHAR(50), phonenumber VARCHAR(20), age INT)"
    try:
        cursor.execute(query)
        print("La tabla ha sido creada exitosamente")
    except psycopg2.errors.DuplicateTable:
        print("La tabla ya existe")
    except psycopg2.Error as e:
        print(f"Ocurrió un error al crear la tabla: {e}")
    cursor.close()

#crear_tabla()

def eliminar_tabla():
    cursor = connection.cursor()
    query = "DROP TABLE IF EXISTS customers"
    try:
        cursor.execute(query)
        print("La tabla ha sido eliminada exitosamente")
    except psycopg2.Error as e:
        print(f"Ocurrió un error al eliminar la tabla: {e}")
    cursor.close()

#eliminar_tabla()

def insertar_datos():
    cursor = connection.cursor()
    query = "INSERT INTO customers(customerid, name, occupation, email, company, phonenumber, age) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    try:
        cursor.execute(query, (1, 'Juan Perez', 'Desarrollador', 'juanperez@example.com', 'ABC Inc.', '555-1234', 30))
        cursor.execute(query, (2, 'Maria Gomez', 'Diseñadora', 'mariagomez@example.com', 'XYZ Ltda.', '555-5678', 25))
        cursor.execute(query, (3, 'Pedro Ramirez', 'Gerente', 'pedroramirez@example.com', 'MNO SA', '555-9012', 40))
        connection.commit()
        print("Los datos han sido insertados exitosamente")
    except psycopg2.Error as e:
        connection.rollback()
        print(f"{e}")
    cursor.close()

insertar_datos()

def actualizar_datos():
    cursor = connection.cursor()
    query = "UPDATE customers SET age = %s WHERE customerid = %s"
    try:
        cursor.execute(query, (35, 1))
        connection.commit()
        print("El dato ha sido actualizado exitosamente")
    except psycopg2.Error as e:
        connection.rollback()
        print(f"Ocurrió un error al actualizar el dato: {e}")
    cursor.close()

#actualizar_datos()
