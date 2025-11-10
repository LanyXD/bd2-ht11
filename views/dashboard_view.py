from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QHeaderView
from PyQt6.QtCore import Qt


class DashboardView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        title = QLabel("Proyectos Activos")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 16pt; font-weight: bold;")

        self.tbl_proyectos = QTableWidget()
        self.tbl_proyectos.setColumnCount(5)
        self.tbl_proyectos.setHorizontalHeaderLabels([
            "Nombre", "Fecha Inicio", "Fecha Fin", "Presupuesto", "Encargado"
        ])
        self.tbl_proyectos.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        layout.addWidget(title)
        layout.addWidget(self.tbl_proyectos)
        self.setLayout(layout)
