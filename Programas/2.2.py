import mysql.connector


class MySQLConnect:
    def __init__(self, host, user, password, database):
        self._host = host
        self._user = user
        self._password = password
        self._database = database
        self._connection = None

    def conectar(self):
        try:
            self._connection = mysql.connector.connect(
                host=self._host,
                user=self._user,
                password=self._password,
                database=self._database
            )
            return self._connection
        except mysql.connector.Error as err:
            print(f"Error de conexión a la base de datos: {err}")
            return None

    def desconectar(self):
        if self._connection:
            self._connection.close()
            self._connection = None


class PaisMySQL(MySQLConnect):
    def insertar(self, id, nombre):
        try:
            connection = self.conectar()
            if connection:
                cursor = connection.cursor()
                query = "INSERT INTO Pais (id, nombre) VALUES (%s, %s)"
                values = (id, nombre)
                cursor.execute(query, values)
                connection.commit()
                cursor.close()
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print(f"Error al insertar país: {err}")
            return False
        finally:
            self.desconectar()

    def editar(self, nombre):
        try:
            connection = self.conectar()
            if connection:
                cursor = connection.cursor()
                query = "UPDATE Pais SET nombre = %s WHERE nombre = %s"
                new_values = ("NuevoNombre", nombre)
                cursor.execute(query, new_values)
                connection.commit()
                cursor.close()
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print(f"Error al editar país: {err}")
            return False
        finally:
            self.desconectar()

    def eliminar(self, id):
        try:
            connection = self.conectar()
            if connection:
                cursor = connection.cursor()
                query = "DELETE FROM Pais WHERE id = %s"
                value = (id,)
                cursor.execute(query, value)
                connection.commit()
                cursor.close()
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print(f"Error al eliminar país: {err}")
            return False
        finally:
            self.desconectar()

    def consultar(self, filtro):
        try:
            connection = self.conectar()
            if connection:
                cursor = connection.cursor()
                query = f"SELECT * FROM Pais WHERE {filtro}"
                cursor.execute(query)
                results = cursor.fetchall()
                cursor.close()
                return results
            else:
                return None
        except mysql.connector.Error as err:
            print(f"Error al consultar países: {err}")
            return None
        finally:
            self.desconectar()


class OlimpiadaMySQL(MySQLConnect):
    def insertar(self, id, year):
        try:
            connection = self.conectar()
            cursor = connection.cursor()

            cursor.execute(f"SELECT * FROM Olimpiada WHERE year = {year}")
            result = cursor.fetchone()
            if result:
                return False

            cursor.execute(f"INSERT INTO Olimpiada (id, year) VALUES ({id}, {year})")
            connection.commit()
            return True
        except Exception as e:
            print(f"Error al insertar olimpiada: {e}")
            return False
        finally:
            self.desconectar()

    def editar(self, id, new_year):
        try:
            connection = self.conectar()
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM Olimpiada WHERE year = %s", (new_year,))
            result = cursor.fetchone()
            if result:
                return False

            cursor.execute("UPDATE Olimpiada SET year = %s WHERE id = %s", (new_year, id))
            connection.commit()
            return True
        except Exception as e:
            print(f"Error al editar olimpiada: {e}")
            return False
        finally:
            self.desconectar()

    def eliminar(self, id):
        try:
            connection = self.conectar()
            cursor = connection.cursor()

            cursor.execute(f"DELETE FROM Olimpiada WHERE id = {id}")
            connection.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar olimpiada: {e}")
            return False
        finally:
            self.desconectar()

    def consultar(self, filter):
        try:
            connection = self.conectar()
            cursor = connection.cursor()

            cursor.execute(f"SELECT * FROM Olimpiada WHERE {filter}")
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(f"Error al consultar olimpiadas: {e}")
            return []
        finally:
            self.desconectar()


class ResultadosMySQL(MySQLConnect):
    def insertar(self, idOlimpiada, idPais, idGenero, oro, plata, bronce):
        try:
            connection = self.conectar()
            cursor = connection.cursor()

            cursor.execute("INSERT INTO Resultados (idOlimpiada, idPais, idGenero, oro, plata, bronce) "
                           "VALUES (%s, %s, %s, %s, %s, %s)",
                           (idOlimpiada, idPais, idGenero, oro, plata, bronce))
            connection.commit()
            return True
        except Exception as e:
            print(f"Error al insertar resultado: {e}")
            return False
        finally:
            self.desconectar()
