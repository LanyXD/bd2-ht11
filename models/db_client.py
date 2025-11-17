from pymongo import MongoClient

class MongoDBClient:
    def __init__(self, uri="mongodb://localhost:27017", dbname="ht11_families", collection="projects"):
        self.client = MongoClient(uri)
        self.db = self.client[dbname]
        self.collection = self.db[collection]

    def insert_data(self, datos):
        self.collection.insert_one(datos)

    def get_one(self, dpi):
        return self.collection.find_one(dpi)
    def get_all(self):
        return list(self.collection.find())

    def update_one(self, filtro, nuevos_datos):
        """
        filtro: dict con las condiciones para encontrar el doc (ej: {"dpi": "123"})
        nuevos_datos: dict con los campos a actualizar (ej: {"nombre": "Nuevo nombre"})
        """
        return self.collection.update_one(filtro, {"$set": nuevos_datos})

    def delete_one(self, dpi):
        self.collection.delete_one(dpi)


"""
db = MongoDBClient()


from datetime import datetime
hoy = datetime.now()

db.insert_data(
    {
        "nombre": "Proyecto2",
        "fecha_inicio": hoy,
        "fecha_fin": hoy,
        "presupuesto": 20000,
        "encargado": "Cesar",
        "finalizado": False,
        "familias_beneficiadas": [
            {
                "direccion": "14 calle 31-12",
                "ingreso_mensual": 1500,
                "integrantes": [
                    {"nombre": "Carlos", "apellido": "Herrera", "edad": 22},
                    {"nombre": "Carlos", "apellido": "Herrera", "edad": 22},
                    {"nombre": "Carlos", "apellido": "Herrera", "edad": 22},
                    {"nombre": "Carlos", "apellido": "Herrera", "edad": 22},
                    {"nombre": "Carlos", "apellido": "Herrera", "edad": 22}
                ]
            },
            {
                "direccion": "12 calle 25-51",
                "ingreso_mensual": 1500,
                "integrantes": [
                    {"nombre": "Carlos", "apellido": "Herrera", "edad": 22},
                    {"nombre": "Carlos", "apellido": "Herrera", "edad": 22},
                    {"nombre": "Carlos", "apellido": "Herrera", "edad": 22},
                    {"nombre": "Carlos", "apellido": "Herrera", "edad": 22},
                    {"nombre": "Carlos", "apellido": "Herrera", "edad": 22}
                ]
            },
            {
                "direccion": "12 calle 25-51",
                "ingreso_mensual": 1500,
                "integrantes": [
                    {"nombre": "Carlos", "apellido": "Herrera", "edad": 22},
                    {"nombre": "Carlos", "apellido": "Herrera", "edad": 22},
                    {"nombre": "Carlos", "apellido": "Herrera", "edad": 22},
                    {"nombre": "Carlos", "apellido": "Herrera", "edad": 22},
                    {"nombre": "Carlos", "apellido": "Herrera", "edad": 22}
                ]
            }
        ]
    }
)

db.insert_data(
    {"nombre": "Eduardo",
     "direccion" : "14 avenidad 31-01",
     "dpi" : "2131-32131-3123"}
)

print(db.get_all())
"""