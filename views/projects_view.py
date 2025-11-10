from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QLineEdit, QDateEdit,
    QDoubleSpinBox, QCheckBox, QComboBox, QPushButton, QHBoxLayout
)
from PyQt6.QtCore import QDate


class ProjectsView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nuevo Proyecto")
        self.resize(400, 350)

        layout = QVBoxLayout()
        form = QFormLayout()

        self.txt_nombre = QLineEdit()
        self.dt_inicio = QDateEdit()
        self.dt_inicio.setDate(QDate.currentDate())
        self.dt_fin = QDateEdit()
        self.dt_fin.setDate(QDate.currentDate())
        self.spn_presupuesto = QDoubleSpinBox()
        self.spn_presupuesto.setMaximum(9999999)
        self.chk_finalizado = QCheckBox("Finalizado")
        self.cmb_encargado = QComboBox()

        form.addRow("Nombre:", self.txt_nombre)
        form.addRow("Fecha Inicio:", self.dt_inicio)
        form.addRow("Fecha Fin:", self.dt_fin)
        form.addRow("Presupuesto:", self.spn_presupuesto)
        form.addRow("Encargado:", self.cmb_encargado)
        form.addRow("", self.chk_finalizado)

        btns = QHBoxLayout()
        self.btn_guardar = QPushButton("💾 Guardar")
        self.btn_cancelar = QPushButton("Cancelar")
        btns.addWidget(self.btn_guardar)
        btns.addWidget(self.btn_cancelar)

        layout.addLayout(form)
        layout.addLayout(btns)
        self.setLayout(layout)
