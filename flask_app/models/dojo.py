from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.nombre= data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []  #Una lista vacia que irá guardando a los ninjas que se registren en determinados Dojos.

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        resultado =  connectToMySQL('esquema_dojos_y_ninjas').query_db(query)
        dojos =[]
        for x in resultado:
            dojos.append(cls(x))
        return dojos

    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (nombre) VALUES (%(nombre)s)"
        resultado = connectToMySQL('esquema_dojos_y_ninjas').query_db(query,data)
        return resultado

    @classmethod
    def get_dojos_with_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        resultado = connectToMySQL('esquema_dojos_y_ninjas').query_db(query, data)
        print(resultado)
        # los resultados serán una lista de ninjas en su respectivo dojo.
        dojo = cls(resultado[0])
        for row in resultado:

            # ahora parseamos los datos de ninjas para crear instancias de ninjas y agregarlas a nuestra lista
            ninja_data = {

                "id" : row["ninjas.id"],
                "nombre" : row["ninjas.nombre"],
                "apellido" : row["apellido"],
                "edad" : row["edad"],
                "created_at" : row["ninjas.created_at"],
                "updated_at" : row["ninjas.updated_at"]

            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo

