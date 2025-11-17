from models.db_client import MongoDBClient

class ManagersModel:
    def __init__(self):
        self.db = MongoDBClient(collection="managers")

    def create_manager(self, document):
        self.db.insert_data(document)

    def get_manager(self, dpi):
        return self.db.get_one({"dpi": dpi})

    def get_managers(self):
        return self.db.get_all()

    def update_manager(self, dpi_original, nuevos_datos):
        """
        dpi_original: el dpi que ya estaba en la DB (el de la fila seleccionada)
        nuevos_datos: lo que está actualmente en el formulario
        """
        return self.db.update_one({"dpi": dpi_original}, nuevos_datos)

    def delete_manager(self, dpi):
        self.db.delete_one({"dpi": dpi})