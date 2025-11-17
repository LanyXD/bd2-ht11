from models.db_client import MongoDBClient
from bson import ObjectId

class ProjectsModel:
    def __init__(self):
        self.db = MongoDBClient(collection="projects")

    def create_project(self, document: dict):
        self.db.insert_data(document)

    def get_projects(self):
        return self.db.get_all()

    def delete_project_by_name(self, nombre):
        self.db.collection.delete_one({"nombre": nombre})

    def update_project(self, id_, new_doc):
        self.db.collection.update_one(
            {"_id": ObjectId(str(id_))},
            {"$set": new_doc}
        )

