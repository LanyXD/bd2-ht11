from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QGroupBox, QFormLayout, QLineEdit, QDoubleSpinBox,
    QComboBox, QPushButton, QTableWidget, QHeaderView, QHBoxLayout
)


class FamiliesView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Familias e Integrantes")
        self.resize(750, 450)

        layout = QVBoxLayout()

        # Datos de la familia
        gb_familia = QGroupBox("Datos de la Familia")
        form = QFormLayout()
        self.txt_nombre = QLineEdit()
        self.txt_direccion = QLineEdit()
        self.spn_ingresos = QDoubleSpinBox()
        self.spn_ingresos.setMaximum(999999)
        self.cmb_proyecto = QComboBox()

        form.addRow("Nombre:", self.txt_nombre)
        form.addRow("Dirección:", self.txt_direccion)
        form.addRow("Ingresos Mensuales:", self.spn_ingresos)
        form.addRow("Proyecto:", self.cmb_proyecto)
        gb_familia.setLayout(form)

        # Integrantes
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

        # Botones generales
        btns = QHBoxLayout()
        self.btn_guardar = QPushButton("💾 Guardar Familia")
        self.btn_cancelar = QPushButton("Cancelar")
        btns.addWidget(self.btn_guardar)
        btns.addWidget(self.btn_cancelar)

        layout.addWidget(gb_familia)
        layout.addWidget(gb_integrantes)
        layout.addLayout(btns)
        self.setLayout(layout)
