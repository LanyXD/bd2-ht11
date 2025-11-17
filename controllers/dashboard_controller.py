# controllers/dashboard_controller.py
from PyQt6.QtWidgets import (QTableWidgetItem)
from models.projects_models import ProjectsModel
from views.dashboard_view import DashboardView
from utils.message import mostrar_mensaje
from PyQt6.QtWidgets import QInputDialog


class DashboardController:
    def __init__(self, view=None, parent_controller=None):
        self.view = view or DashboardView()
        self.model = ProjectsModel()

        # referencia al MainController para cambiar páginas
        self.parent_controller = parent_controller

        # conectar botones
        self.view.btn_agregar.clicked.connect(self.go_to_add_project)
        self.view.btn_editar.clicked.connect(self.edit_project)
        self.view.btn_buscar.clicked.connect(self.search_project)
        self.view.btn_eliminar.clicked.connect(self.delete_project)

        # cargar datos en tabla
        self.load_table()

    # ==========================
    #  CARGAR TABLA
    # ==========================
    def load_table(self):
        proyectos = self.model.get_projects()

        tbl = self.view.tbl_proyectos
        tbl.setRowCount(len(proyectos))

        for i, p in enumerate(proyectos):
            tbl.setItem(i, 0, QTableWidgetItem(p.get("nombre", "")))
            tbl.setItem(i, 1, QTableWidgetItem(p.get("fecha_inicio", "")))
            tbl.setItem(i, 2, QTableWidgetItem(p.get("fecha_fin", "")))
            tbl.setItem(i, 3, QTableWidgetItem(str(p.get("presupuesto", 0))))
            encargado = p.get("encargado", {})
            tbl.setItem(i, 4, QTableWidgetItem(encargado.get("nombre", "")))

    # ==========================
    #   AGREGAR
    # ==========================
    def go_to_add_project(self):
        self.parent_controller.page_projects()

    # ==========================
    #    EDITAR
    # ==========================
    def edit_project(self):
        row = self.view.tbl_proyectos.currentRow()
        if row == -1:
            mostrar_mensaje("Error", "Seleccione un proyecto primero.", "error")
            return

        nombre = self.view.tbl_proyectos.item(row, 0).text()

        # cargar el proyecto desde Mongo
        proyectos = self.model.get_projects()
        proyecto = next((p for p in proyectos if p["nombre"] == nombre), None)

        if not proyecto:
            mostrar_mensaje("Error", "El proyecto no existe en la base de datos.", "error")
            return

        # redirigir a página de proyectos
        self.parent_controller.page_projects()

        # cargar los datos en el formulario
        self.parent_controller.projects_controller.load_project(proyecto)

    # ==========================
    #    BUSCAR
    # ==========================
    def search_project(self):
        nombre, ok = QInputDialog.getText(None, "Buscar proyecto", "Ingrese el nombre:")
        if not ok or not nombre.strip():
            return

        proyectos = self.model.get_projects()
        found = None

        for i, p in enumerate(proyectos):
            if p["nombre"].lower() == nombre.strip().lower():
                found = i
                break

        if found is None:
            mostrar_mensaje("Error", "Proyecto no encontrado.", "error")
            return

        self.view.tbl_proyectos.selectRow(found)

    # ==========================
    #    ELIMINAR
    # ==========================
    def delete_project(self):
        nombre, ok = QInputDialog.getText(None, "Eliminar proyecto", "Ingrese el nombre del proyecto:")
        if not ok or not nombre.strip():
            return

        try:
            self.model.delete_project_by_name(nombre.strip())
            mostrar_mensaje("Info", "Proyecto eliminado.", "info")
            self.load_table()
        except Exception as e:
            mostrar_mensaje("Error", f"No se pudo eliminar:\n{e}", "error")
