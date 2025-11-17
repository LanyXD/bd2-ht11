from models.projects_models import ProjectsModel
from views.projects_view import ProjectsView
from views.family_dialog import FamilyDialog
from utils.message import mostrar_mensaje
from models.managers_models import ManagersModel
from PyQt6.QtCore import QDate

class ProjectsController:
    def __init__(self, view: ProjectsView = None, model: ProjectsModel = None):
        self.view = view or ProjectsView()
        self.model = model or ProjectsModel()
        self.managers_model = ManagersModel()

        self.editing_id = None  # para saber si estamos editando o creando

        # lista en memoria de familias embebidas
        self.familias = []
        self.load_encargados()

        # señales
        self.view.btn_add_familia.clicked.connect(self.add_family)
        self.view.btn_edit_familia.clicked.connect(self.edit_family)
        self.view.btn_del_familia.clicked.connect(self.del_family)
        self.view.btn_guardar.clicked.connect(self.save_project)

    # ===== Familias =====
    def add_family(self):
        dlg = FamilyDialog(self.view)
        if dlg.exec():
            fam = dlg.get_data()
            self.familias.append(fam)
            self.refresh_families_table()

    def edit_family(self):
        row = self.view.tbl_familias.currentRow()
        if row == -1:
            mostrar_mensaje("Error", "Seleccione una familia primero.", "error")
            return
        dlg = FamilyDialog(self.view, data=self.familias[row])
        if dlg.exec():
            self.familias[row] = dlg.get_data()
            self.refresh_families_table()

    def del_family(self):
        row = self.view.tbl_familias.currentRow()
        if row == -1:
            mostrar_mensaje("Error", "Seleccione una familia primero.", "error")
            return
        self.familias.pop(row)
        self.refresh_families_table()

    def refresh_families_table(self):
        tbl = self.view.tbl_familias
        tbl.setRowCount(len(self.familias))
        for i, fam in enumerate(self.familias):
            nombre = fam.get("nombre", "")
            direccion = fam.get("direccion", "")
            ingresos = fam.get("ingreso_mensual", 0)
            n_integrantes = len(fam.get("integrantes", []))

            from PyQt6.QtWidgets import QTableWidgetItem
            tbl.setItem(i, 0, QTableWidgetItem(nombre))
            tbl.setItem(i, 1, QTableWidgetItem(direccion))
            tbl.setItem(i, 2, QTableWidgetItem(f"{ingresos:.2f}"))
            tbl.setItem(i, 3, QTableWidgetItem(str(n_integrantes)))

    # ===== Guardar proyecto completo =====
    def save_project(self):
        if not self.view.txt_nombre.text().strip():
            mostrar_mensaje("Error", "El nombre del proyecto es obligatorio.", "error")
            return

        if self.view.cmb_encargado.currentIndex() <= 0:
            mostrar_mensaje("Error", "Debe seleccionar un encargado.", "error")
            return

        doc = {
            "nombre": self.view.txt_nombre.text().strip(),
            "fecha_inicio": self.view.dt_inicio.date().toString("yyyy-MM-dd"),
            "fecha_fin": self.view.dt_fin.date().toString("yyyy-MM-dd"),
            "presupuesto": float(self.view.spn_presupuesto.value()),
            "encargado": self.view.cmb_encargado.currentData(),
            "finalizado": self.view.chk_finalizado.isChecked(),
            "familias_beneficiadas": self.familias,
        }

        try:
            if self.editing_id is None:
                # crear nuevo
                self.model.create_project(doc)
                mostrar_mensaje("Info", "Proyecto creado con éxito.", "info")
            else:
                self.model.update_project(self.editing_id, doc)
                mostrar_mensaje("Info", "Proyecto actualizado con éxito.", "info")
                self.editing_id = None  # reset

        except Exception as e:
            mostrar_mensaje("Error", f"No se pudo guardar el proyecto:\n{e}", "error")

        self.view.txt_nombre.clear()
        self.view.dt_inicio.setDate(QDate.currentDate())
        self.view.dt_fin.setDate(QDate.currentDate())
        self.view.spn_presupuesto.setValue(0)
        self.view.chk_finalizado.setChecked(False)
        self.view.cmb_encargado.setCurrentIndex(0)

        self.familias = []  # vaciar la lista interna
        self.view.tbl_familias.setRowCount(0)  # limpiar la tabla

    def load_encargados(self):
        encargados = self.managers_model.get_managers()

        self.view.cmb_encargado.clear()
        self.view.cmb_encargado.addItem("Seleccione un encargado", None)

        for enc in encargados:
            nombre = enc.get("nombre", "")
            datos_ocultos = {
                "_id": str(enc.get("_id", "")),
                "nombre" : enc.get("nombre", ""),
                "dpi": enc.get("dpi", ""),
                "direccion": enc.get("direccion", "")
            }

            self.view.cmb_encargado.addItem(nombre, datos_ocultos)

    def load_project(self, doc):
        self.editing_id = doc.get("_id")

        self.view.txt_nombre.setText(doc.get("nombre", ""))
        self.view.dt_inicio.setDate(QDate.fromString(doc.get("fecha_inicio"), "yyyy-MM-dd"))
        self.view.dt_fin.setDate(QDate.fromString(doc.get("fecha_fin"), "yyyy-MM-dd"))
        self.view.spn_presupuesto.setValue(float(doc.get("presupuesto", 0)))
        self.view.chk_finalizado.setChecked(doc.get("finalizado", False))

        # encargado
        encargado = doc.get("encargado", {})
        idx = self.view.cmb_encargado.findText(encargado.get("nombre", ""))
        if idx != -1:
            self.view.cmb_encargado.setCurrentIndex(idx)

        # familias
        self.familias = doc.get("familias_beneficiadas", [])
        self.refresh_families_table()


