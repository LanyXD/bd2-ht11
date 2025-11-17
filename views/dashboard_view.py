from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTableWidget, QHeaderView,
    QHBoxLayout, QPushButton
)
from PyQt6.QtCore import Qt


class DashboardView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        # ===== TÍTULO =====
        title = QLabel("Proyectos Registrados")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 20pt; font-weight: bold; margin-bottom: 15px;")

        # ===== TABLA =====
        self.tbl_proyectos = QTableWidget()
        self.tbl_proyectos.setColumnCount(5)
        self.tbl_proyectos.setHorizontalHeaderLabels([
            "Nombre", "Fecha Inicio", "Fecha Fin", "Presupuesto", "Encargado"
        ])
        self.tbl_proyectos.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tbl_proyectos.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)

        # ===== BOTONES =====
        btns = QHBoxLayout()
        self.btn_agregar = QPushButton("Agregar Proyecto")
        self.btn_editar = QPushButton("Editar Proyecto")
        self.btn_buscar = QPushButton("Buscar Proyecto")
        self.btn_eliminar = QPushButton("Eliminar Proyecto")

        btns.addWidget(self.btn_agregar)
        btns.addWidget(self.btn_editar)
        btns.addWidget(self.btn_buscar)
        btns.addWidget(self.btn_eliminar)

        # ENSAMBLAR TODO
        layout.addWidget(title)
        layout.addLayout(btns)
        layout.addWidget(self.tbl_proyectos)
        self.setLayout(layout)
