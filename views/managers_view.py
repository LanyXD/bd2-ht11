from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QGroupBox, QFormLayout, QLineEdit, QPushButton,
    QTableWidget, QHeaderView, QHBoxLayout
)


class ManagersView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Encargados")
        self.resize(650, 400)

        layout = QVBoxLayout()

        # Formulario
        gb_form = QGroupBox("Datos del Encargado")
        form = QFormLayout()
        self.txt_nombre = QLineEdit()
        self.txt_direccion = QLineEdit()
        self.txt_dpi = QLineEdit()

        form.addRow("Nombre:", self.txt_nombre)
        form.addRow("Dirección:", self.txt_direccion)
        form.addRow("DPI:", self.txt_dpi)
        gb_form.setLayout(form)

        # Tabla
        self.tbl_encargados = QTableWidget()
        self.tbl_encargados.setColumnCount(3)
        self.tbl_encargados.setHorizontalHeaderLabels(["Nombre", "Dirección", "DPI"])
        self.tbl_encargados.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Botones
        btns = QHBoxLayout()
        self.btn_agregar = QPushButton("Agregar")
        self.btn_editar = QPushButton("Editar")
        self.btn_eliminar = QPushButton("Eliminar")
        self.btn_buscar = QPushButton("Buscar")
        btns.addWidget(self.btn_agregar)
        btns.addWidget(self.btn_editar)
        btns.addWidget(self.btn_eliminar)
        btns.addWidget(self.btn_buscar)

        layout.addWidget(gb_form)
        layout.addWidget(self.tbl_encargados)
        layout.addLayout(btns)
        self.setLayout(layout)
