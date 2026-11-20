import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

class Conectar:
    def __init__(self):
        try:
            self.c = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME")
            )
            self.cursor = self.c.cursor(dictionary=True)
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos:", error)
            self.c = None
            self.cursor = None

    def obtener_cliente(self):
        self.cursor.execute("SELECT * FROM cliente")
        return self.cursor.fetchall()

    def agregar_cliente(self, DNI,nombre, apellido, tel, fecha_nac):
        self.cursor.execute(
             "INSERT INTO cliente (DNI, nombre, apellido, tel, fecha_nac) VALUES (%s, %s, %s, %s, %s)",
               (DNI, nombre, apellido, tel, fecha_nac))
        self.c.commit()

    def eliminar_cliente(self, id_cliente):
        self.cursor.execute("DELETE FROM cliente WHERE id_cliente = %s", (id_cliente,))
        self.c.commit()

    def listar_clientes(self):
        self.cursor.execute("SELECT * FROM cliente")
        for cliente in self.cursor.fetchall():
            print(cliente)

    def editar_cliente(self, id_cliente, DNI, nombre, apellido, tel, fecha_nac):
        self.cursor.execute("UPDATE cliente set DNI=%s, nombre=%s, apellido=%s, tel=%s, fecha_nac= %s WHERE id_cliente= %s",
                            (DNI, nombre, apellido, tel, fecha_nac, id_cliente))
        self.c.commit()

conexion=Conectar()
# conexion.agregar_cliente("37354954", "Micaela", "Velazco", "113344433", "1993-02-04")
# clientes=conexion.listar_clientes()

# conexion.eliminar_cliente(11)
# conexion.eliminar_cliente(12)
# conexion.eliminar_cliente(13)
# conexion.eliminar_cliente(14)
# conexion.agregar_cliente("34546789","soledad", "pastoruti", "1125586754", "1900-04-24")
# clientes=conexion.listar_clientes()
# conexion.editar_cliente(21,"44035674", "Sebitas", "2000", "1155445432", "1999-06-08")
# clientes=conexion.listar_clientes()


