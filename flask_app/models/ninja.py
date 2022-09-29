from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.nombre= data['nombre']
        self.apellido = data['apellido']
        self.edad = data['edad']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    #Este método es para guardar algo en nuestra base de datos, en este caso, un Ninja.
    def save(cls,data):
        query = "INSERT INTO ninjas (nombre,apellido,edad, dojo_id) VALUES (%(nombre)s,%(apellido)s,%(edad)s,%(dojo_id)s)"
        resultado = connectToMySQL('esquema_dojos_y_ninjas').query_db(query,data)
        return resultado


    # No sé si requiera de esta función, puesto que no siento necesario tener que llamar a todos los ninjas en algún punto. De todas maneras lo cree por si lo llegara
    # a requerir.
    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM ninjas;"
    #     resultado =  connectToMySQL('esquema_dojos_y_ninjas').query_db(query)
    #     ninjas =[]
    #     for b in resultado:
    #         ninjas.append(cls(b))
    #     return ninjas