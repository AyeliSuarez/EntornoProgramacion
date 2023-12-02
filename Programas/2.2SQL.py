# Ayeli Yaramit Suarez Soria, 951

from mysql.connector import connect, Error

# Desarrollar una clase llamada MySQLConnect que tenga como atributos: host, user, password, database.
# Debe crear sus métodos set y get (property, setters), conectar(), desconectar(), Investigar método close().


class MySQLConnect:
    def __init__(self, host, user, password, database):
        self._host = host
        self._user = user
        self._password = password
        self._database = database
        self._connection = None

    @property
    def host(self):
        return self._host

    @property
    def user(self):
        return self._user

    @property
    def password(self):
        return self._password

    @property
    def database(self):
        return self._database

    def conectar(self):
        try:
            self._connection = connect(
                host=self._host,
                user=self._user,
                password=self._password,
                database=self._database
            )
            return self._connection
        except Error as err:
            print(f"Error de conexión a la base de datos: {err}")
            return None

    def desconectar(self):
        if self._connection:
            self._connection.close()

# clase llamada PaisMySQL que herede de  MySQLConnect.agregar los atributos  de la clase padre.
# agregar métodos: insertar(id, nombre): Método para insertar datos en la Tabla Pais, debe recibir como parámetro
# las columnas de la tabla y debe retornar True si se inserta el dato o False en caso contrario.
# editar(nombre): Método para editar el nombre en la Tabla País. Validar que nombre no exista en la tabla.
# eliminar(id): Método para eliminar un elemento de la Tabla País. Debe tener como parámetro la llave primaria, retorna
# True si logró eliminarse y False en caso contrario. consultar(filter): Método que recibe un filtro(cadena) y retorna
# una lista de tuplas con los resultados del filtro de la Tabla País. Ejemplo: “id = 1” , “nombre like %A%”


class PaisMySQL(MySQLConnect):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)

    def insertar(self, id, nombre):
        try:
            cursor = self._connection.cursor()
            sql = "INSERT INTO Pais (id, nombre) VALUES (%s, %s)"
            val = (id, nombre)
            cursor.execute(sql, val)
            self._connection.commit()
            return True
        except Error as e:
            print(e)
            return False

    def editar(self, id, nombre):
        try:
            cursor = self._connection.cursor()
            sql = "SELECT * FROM Pais WHERE nombre = %s AND id != %s"
            val = (nombre, id)
            cursor.execute(sql, val)
            result = cursor.fetchone()
            if result:
                print("El nombre ya existe en la tabla.")
                return False
            else:
                sql = "UPDATE Pais SET nombre = %s WHERE id = %s"
                val = (nombre, id)
                cursor.execute(sql, val)
                self._connection.commit()
                return True
        except Error as e:
            print(e)
            return False

    def eliminar(self, id):
        try:
            cursor = self._connection.cursor()
            sql = "DELETE FROM Pais WHERE id = %s"
            val = (id,)
            cursor.execute(sql, val)
            self._connection.commit()
            return True
        except Error as e:
            print(e)
            return False

    def consultar(self, filtro):
        try:
            cursor = self._connection.cursor()
            sql = "SELECT * FROM Pais WHERE " + filtro
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(e)
            return []


# clase  OlimpiadaMySQL que herede de  MySQLConnect.  agregar los atributos  de la clase padre. siguientes métodos
# insertar(id, year): insertar datos en la Tabla Olimpiada, debe recibir como parámetro las columnas de la tabla y
# debe retornar True si se inserta el dato o False en caso contrario.
# editar(year):editar el año en la Tabla Olimpiada. Validar que el año no exista en la tabla.
# eliminar(id): eliminar un elemento de la Tabla Olimpiada. Debe tener como parámetro la llave primaria, retorna
# True si logró eliminarse y False en caso contrario.
# consultar(filter): Método que recibe un filtro(cadena) y retorna una lista de tuplas con los resultados del filtro
# de la Tabla Olimpiada. Ejemplo: “id = 1” , “year > 1990”

class OlimpiadaMySQL(MySQLConnect):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)

    def insertar(self, id, year):
        try:
            cursor = self._connection.cursor()
            sql = "INSERT INTO Olimpiada (id, year) VALUES (%s, %s)"
            val = (id, year)
            cursor.execute(sql, val)
            self._connection.commit()
            return True
        except Error as e:
            print(e)
            return False

    def editar(self, id, year):
        try:
            cursor = self._connection.cursor()
            sql = "SELECT * FROM Olimpiada WHERE year = %s AND id != %s"
            val = (year, id)
            cursor.execute(sql, val)
            result = cursor.fetchone()
            if result:
                print("El año ya existe en la tabla.")
                return False
            else:
                sql = "UPDATE Olimpiada SET year = %s WHERE id = %s"
                val = (year, id)
                cursor.execute(sql, val)
                self._connection.commit()
                return True
        except Error as e:
            print(e)
            return False

    def eliminar(self, id):
        try:
            cursor = self._connection.cursor()
            sql = "DELETE FROM Olimpiada WHERE id = %s"
            val = (id,)
            cursor.execute(sql, val)
            self._connection.commit()
            return True
        except Error as e:
            print(e)
            return False

    def consultar(self, filtro):
        try:
            cursor = self._connection.cursor()
            sql = "SELECT * FROM Olimpiada WHERE " + filtro
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(e)
            return []


# clase  ResultadosMySQL que herede de  MySQLConnect.  agregar los atributos de la clase padre.
# Debe agregar los siguientes métodos:
# insertar(idOlimpiada, idPais, idGenero, oro, plata, bronce): en la Tabla Resultados, debe recibir como parámetro
# las columnas de la tabla y debe retornar True si se inserta el dato o False en caso contrario.
# editar(oro, plata, bronce): Método para editar oro, plata, bronce en la Tabla Resultados.
# eliminar(idOlimpiada, idPais, idGenero): eliminar un elemento de la Tabla Resultados.
# Debe tener como parámetro la llave primaria compuesta, retorna True si logró eliminarse y False en caso contrario.
# consultar(filter): Método que recibe un filtro(cadena) y retorna una lista de tuplas con los resultados del filtro
# de la Tabla Resultados. Ejemplo: “idPais = 1” , “idPais = 1 and idOlimpiada=2”


class ResultadosMySQL(MySQLConnect):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)

    def insertar(self, idOlimpiada, idPais, idGenero, oro, plata, bronce):
        try:
            cursor = self._connection.cursor()
            sql = "INSERT INTO Resultados (idOlimpiada, idPais, idGenero, oro, plata, bronce) " \
                  "VALUES (%s, %s, %s, %s, %s, %s)"
            val = (idOlimpiada, idPais, idGenero, oro, plata, bronce)
            cursor.execute(sql, val)
            self._connection.commit()
            return True
        except Error as e:
            print(e)
            return False

    def editar(self, idOlimpiada, idPais, idGenero, oro, plata, bronce):
        try:
            cursor = self._connection.cursor()
            sql = "UPDATE Resultados SET oro = %s, plata = %s, bronce = %s " \
                  "WHERE idOlimpiada = %s AND idPais = %s AND idGenero = %s"
            val = (oro, plata, bronce, idOlimpiada, idPais, idGenero)
            cursor.execute(sql, val)
            self._connection.commit()
            return True
        except Error as e:
            print(e)
            return False

    def eliminar(self, idOlimpiada, idPais, idGenero):
        try:
            cursor = self._connection.cursor()
            sql = "DELETE FROM Resultados WHERE idOlimpiada = %s AND idPais = %s AND idGenero = %s"
            val = (idOlimpiada, idPais, idGenero)
            cursor.execute(sql, val)
            self._connection.commit()
            return True
        except Error as e:
            print(e)
            return False

    def consultar(self, filtro):
        try:
            cursor = self._connection.cursor()
            sql = "SELECT * FROM Resultados WHERE " + filtro
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(e)
            return []


if __name__ == "__main__":
    pais_db = PaisMySQL(host="localhost", user="root", password="12345", database="olimpiadas")
    olimpiada_db = OlimpiadaMySQL(host="localhost", user="root", password="12345", database="olimpiadas")
    resultados_db = ResultadosMySQL(host="localhost", user="root", password="12345", database="olimpiadas")

    pais_db.conectar()
    olimpiada_db.conectar()
    resultados_db.conectar()

    pais_db.insertar(1, "Argentina")
    olimpiada_db.insertar(1, 2023)
    resultados_db.insertar(1, 1, 1, 5, 3, 2)

    print(pais_db.consultar("id = 1"))
    print(olimpiada_db.consultar("id = 1"))
    print(resultados_db.consultar("idPais = 1"))

    pais_db.desconectar()
    olimpiada_db.desconectar()
    resultados_db.desconectar()
