# views/family_dialog.py
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QGridLayout, QLineEdit, QDoubleSpinBox,
    QPushButton, QHBoxLayout, QLabel, QGroupBox, QTableWidget,
    QHeaderView, QMessageBox
)
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox
from .integrant_dialog import IntegrantDialog


class FamilyDialog(QDialog):
    def __init__(self, parent=None, data=None):
        super().__init__(parent)
        self.setWindowTitle("Familia beneficiada")
        self.integrantes = []

        layout = QVBoxLayout()

        # ===== DATOS FAMILIA =====
        gb_fam = QGroupBox("Datos de la familia")
        grid = QGridLayout()

        self.txt_nombre = QLineEdit()
        self.txt_direccion = QLineEdit()
        self.spn_ingresos = QDoubleSpinBox()
        self.spn_ingresos.setMaximum(999_999)

        grid.addWidget(QLabel("Nombre:"),   0, 0)
        grid.addWidget(self.txt_nombre,     0, 1)
        grid.addWidget(QLabel("Dirección:"), 1, 0)
        grid.addWidget(self.txt_direccion,   1, 1)
        grid.addWidget(QLabel("Ingresos mensuales:"), 2, 0)
        grid.addWidget(self.spn_ingresos,          2, 1)

        gb_fam.setLayout(grid)

        # ===== INTEGRANTES =====
        gb_int = QGroupBox("Integrantes")
        vbox_int = QVBoxLayout()

        self.tbl_integrantes = QTableWidget()
        self.tbl_integrantes.setColumnCount(3)
        self.tbl_integrantes.setHorizontalHeaderLabels(["Nombre", "Apellido", "Edad"])
        self.tbl_integrantes.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        btns_int = QHBoxLayout()
        self.btn_add_int = QPushButton("Agregar integrante")
        self.btn_del_int = QPushButton("Eliminar integrante")
        btns_int.addWidget(self.btn_add_int)
        btns_int.addWidget(self.btn_del_int)

        vbox_int.addWidget(self.tbl_integrantes)
        vbox_int.addLayout(btns_int)
        gb_int.setLayout(vbox_int)

        # ===== BOTONES DIALOGO =====
        btns = QHBoxLayout()
        self.btn_ok = QPushButton("Guardar familia")
        self.btn_cancel = QPushButton("Cancelar")
        btns.addWidget(self.btn_ok)
        btns.addWidget(self.btn_cancel)

        layout.addWidget(gb_fam)
        layout.addWidget(gb_int)
        layout.addLayout(btns)
        self.setLayout(layout)

        # Señales
        self.btn_add_int.clicked.connect(self.add_integrant)
        self.btn_del_int.clicked.connect(self.del_integrant)
        self.btn_ok.clicked.connect(self.accept_family)
        self.btn_cancel.clicked.connect(self.reject)

        # Si viene data (modo edición)
        if data:
            self.load_data(data)

    # ===== Integrantes =====
    def add_integrant(self):
        dlg = IntegrantDialog(self)
        if dlg.exec():
            integrante = dlg.get_data()
            self.integrantes.append(integrante)
            self.refresh_table()

    def del_integrant(self):
        row = self.tbl_integrantes.currentRow()
        if row == -1:
            return
        self.integrantes.pop(row)
        self.refresh_table()

    def refresh_table(self):
        self.tbl_integrantes.setRowCount(len(self.integrantes))
        for r, integ in enumerate(self.integrantes):
            self.tbl_integrantes.setItem(r, 0, QTableWidgetItem(integ["nombre"]))
            self.tbl_integrantes.setItem(r, 1, QTableWidgetItem(integ["apellido"]))
            self.tbl_integrantes.setItem(r, 2, QTableWidgetItem(str(integ["edad"])))

    # ===== Guardar / cargar =====
    def accept_family(self):
        if not self.txt_direccion.text().strip():
            QMessageBox.warning(self, "Error", "La dirección es obligatoria.")
            return

        self.accept()

    def get_data(self) -> dict:
        return {
            "nombre": self.txt_nombre.text().strip(),
            "direccion": self.txt_direccion.text().strip(),
            "ingreso_mensual": float(self.spn_ingresos.value()),
            "integrantes": self.integrantes,
        }

    def load_data(self, data: dict):
        self.txt_nombre.setText(data.get("nombre", ""))
        self.txt_direccion.setText(data.get("direccion", ""))
        self.spn_ingresos.setValue(data.get("ingreso_mensual", 0))
        self.integrantes = data.get("integrantes", [])
        self.refresh_table()
