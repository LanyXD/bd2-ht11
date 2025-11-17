from views.managers_view import ManagersView
from models.managers_models import ManagersModel
from utils.message import mostrar_mensaje
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox

class ManagerController:
    def __init__(self, managers_view=None, managers_model=None):
        self.managers_view = managers_view or ManagersView()
        self.managers_model = managers_model or ManagersModel()

        self.managers_view.btn_agregar.clicked.connect(self.create_manager)
        self.managers_view.btn_editar.clicked.connect(self.edit_manager)
        self.managers_view.btn_eliminar.clicked.connect(self.delete_manager)
        self.managers_view.btn_buscar.clicked.connect(self.search_manager)

        self.managers_view.tbl_encargados.cellClicked.connect(self.load_data_into_form)
        self.dpi_original = None

    def create_manager(self):
        nombre = self.managers_view.txt_nombre.text()
        direccion = self.managers_view.txt_direccion.text()
        dpi =  self.managers_view.txt_dpi.text()

        if not nombre:
            mostrar_mensaje("Error", "Debes ingresar un nombre", "error")
            return
        if not direccion:
            mostrar_mensaje("Error", "Debes ingresar la direccion", "error")
            return
        if not dpi.isdigit():
            mostrar_mensaje("Error", "El dpi debe ser un número válido", "error")
            return

        try:
            self.managers_model.create_manager({
                "nombre": nombre,
                "direccion": direccion,
                "dpi": dpi
            })
            mostrar_mensaje("Info", "Encargado agregado con éxito", "Info")

            self.load_managers()

            self.managers_view.txt_nombre.clear()
            self.managers_view.txt_direccion.clear()
            self.managers_view.txt_dpi.clear()

        except Exception as e:
            mostrar_mensaje("Error", f"No se pudo guardar el encargado:\n{e}", "error")

    def load_managers(self):
        datos = self.managers_model.get_managers()

        self.managers_view.tbl_encargados.setRowCount(len(datos))
        self.managers_view.tbl_encargados.setColumnCount(3)

        for fila, doc in enumerate(datos):
            self.managers_view.tbl_encargados.setItem(fila, 0, QTableWidgetItem(doc.get("nombre", "")))
            self.managers_view.tbl_encargados.setItem(fila, 1, QTableWidgetItem(doc.get("direccion", "")))
            self.managers_view.tbl_encargados.setItem(fila, 2, QTableWidgetItem(doc.get("dpi", "")))

    def load_data_into_form(self, fila):
        if fila == -1:
            return

        dpi = self.managers_view.tbl_encargados.item(fila, 2).text()
        encargado = self.managers_model.get_manager(dpi)

        if not encargado:
            mostrar_mensaje("Error", "No se encontró el encargado.", "error")
            return

        # Guardamos el DPI original para saber a quién actualizar
        self.dpi_original = encargado["dpi"]

        self.managers_view.txt_nombre.setText(encargado.get("nombre", ""))
        self.managers_view.txt_direccion.setText(encargado.get("direccion", ""))
        self.managers_view.txt_dpi.setText(encargado.get("dpi", ""))

    def edit_manager(self):
        fila = self.managers_view.tbl_encargados.currentRow()
        if fila == -1:
            mostrar_mensaje("Error", "Debe seleccionar un encargado primero.", "error")
            return

        nombre = self.managers_view.txt_nombre.text()
        direccion = self.managers_view.txt_direccion.text()
        dpi = self.managers_view.txt_dpi.text()

        if not nombre:
            mostrar_mensaje("Error", "Debes ingresar un nombre", "error")
            return
        if not direccion:
            mostrar_mensaje("Error", "Debes ingresar la direccion", "error")
            return
        if not dpi.isdigit():
            mostrar_mensaje("Error", "El dpi debe ser un número válido", "error")
            return

        nuevos_datos = {
            "nombre" : nombre,
            "direccion" : direccion,
            "dpi" : dpi
        }

        try:
            resultado = self.managers_model.update_manager(self.dpi_original, nuevos_datos)

            if resultado.modified_count == 0:
                mostrar_mensaje("Info", "No se realizaron cambios (datos iguales o no encontrado).", "info")
            else:
                mostrar_mensaje("Info", "Encargado actualizado correctamente.", "info")

            # Recargar tabla
            self.load_managers()

        except Exception as e:
            mostrar_mensaje("Error", f"No se pudo actualizar el encargado:\n{e}", "error")

    def delete_manager(self):
        fila = self.managers_view.tbl_encargados.currentRow()
        if fila == -1:
            mostrar_mensaje("Error", "Debe seleccionar un encargado primero.", "error")
            return

        self.managers_model.delete_manager(self.dpi_original)

        reply = QMessageBox.question(
            self.managers_view,
            "Confirmar eliminación",
            f"¿Seguro que deseas eliminar al encargado con DPI: {self.dpi_original}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.No:
            return

        try:
            self.managers_model.delete_manager(self.dpi_original)

            mostrar_mensaje("Info", "Encargado eliminado correctamente.", "info")

            self.load_managers()  # refrescar tabla

            # Limpiar formulario
            self.managers_view.txt_nombre.clear()
            self.managers_view.txt_direccion.clear()
            self.managers_view.txt_dpi.clear()

        except Exception as e:
            mostrar_mensaje("Error", f"Ocurrió un error al eliminar:\n{e}", "error")

    def search_manager(self):
        fila = self.managers_view.tbl_encargados.currentRow()
        if fila == -1:
            mostrar_mensaje("Error", "Debe seleccionar un encargado primero.", "error")
            return

        mostrar_mensaje("Info", f"Encargado con DPI: {self.dpi_original} existe", "Info")
