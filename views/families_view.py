from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QGroupBox, QGridLayout, QLineEdit, QDoubleSpinBox,
    QComboBox, QPushButton, QTableWidget, QHeaderView, QHBoxLayout, QLabel
)


class FamiliesView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Familias e Integrantes")
        self.resize(750, 450)

        layout = QVBoxLayout()

        # ==========================
        #  DATOS DE LA FAMILIA
        # ==========================
        gb_familia = QGroupBox("Datos de la Familia")
        grid = QGridLayout()

        # Inputs
        self.txt_nombre = QLineEdit()
        self.txt_direccion = QLineEdit()
        self.spn_ingresos = QDoubleSpinBox()
        self.spn_ingresos.setMaximum(999999)
        self.cmb_proyecto = QComboBox()

        # INPUTS EN PAREJAS
        grid.addWidget(QLabel("Nombre:"), 0, 0)
        grid.addWidget(self.txt_nombre,   0, 1)

        grid.addWidget(QLabel("Dirección:"), 0, 2)
        grid.addWidget(self.txt_direccion,   0, 3)

        grid.addWidget(QLabel("Ingresos Mensuales:"), 1, 0)
        grid.addWidget(self.spn_ingresos,             1, 1)

        grid.addWidget(QLabel("Proyecto:"), 1, 2)
        grid.addWidget(self.cmb_proyecto,   1, 3)

        grid.setColumnStretch(1, 1)
        grid.setColumnStretch(3, 1)

        gb_familia.setLayout(grid)

        # ==========================
        #  INTEGRANTES
        # ==========================
        gb_integrantes = QGroupBox("Integrantes")
        vbox = QVBoxLayout()

        self.tbl_integrantes = QTableWidget()
        self.tbl_integrantes.setColumnCount(3)
        self.tbl_integrantes.setHorizontalHeaderLabels(["Nombre", "Apellido", "Edad"])
        self.tbl_integrantes.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        btns_int = QHBoxLayout()
        self.btn_add_int = QPushButton("Agregar Integrante")
        self.btn_del_int = QPushButton("Eliminar Integrante")
        btns_int.addWidget(self.btn_add_int)
        btns_int.addWidget(self.btn_del_int)

        vbox.addWidget(self.tbl_integrantes)
        vbox.addLayout(btns_int)
        gb_integrantes.setLayout(vbox)

        # ==========================
        #  BOTONES GENERALES
        # ==========================
        btns = QHBoxLayout()
        self.btn_guardar = QPushButton("💾 Guardar Familia")
        self.btn_cancelar = QPushButton("Cancelar")
        btns.addWidget(self.btn_guardar)
        btns.addWidget(self.btn_cancelar)

        # Agregar todo al layout principal
        layout.addWidget(gb_familia)
        layout.addWidget(gb_integrantes)
        layout.addLayout(btns)
        self.setLayout(layout)
