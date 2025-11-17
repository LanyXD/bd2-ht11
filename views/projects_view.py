from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QGridLayout, QLineEdit, QDateEdit,
    QDoubleSpinBox, QCheckBox, QComboBox, QPushButton, QHBoxLayout,
    QLabel, QGroupBox, QTableWidget, QHeaderView
)
from PyQt6.QtCore import QDate


class ProjectsView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nuevo Proyecto")

        layout = QVBoxLayout()

        # ====== DATOS DEL PROYECTO ======
        gb_proyecto = QGroupBox("Datos del Proyecto")
        grid = QGridLayout()

        self.txt_nombre = QLineEdit()
        self.dt_inicio = QDateEdit()
        self.dt_inicio.setDate(QDate.currentDate())
        self.dt_fin = QDateEdit()
        self.dt_fin.setDate(QDate.currentDate())
        self.spn_presupuesto = QDoubleSpinBox()
        self.spn_presupuesto.setMaximum(9_999_999)
        self.cmb_encargado = QComboBox()
        self.chk_finalizado = QCheckBox("Finalizado")

        grid.addWidget(QLabel("Nombre:"),        0, 0)
        grid.addWidget(self.txt_nombre,          0, 1)

        grid.addWidget(QLabel("Encargado:"),     0, 2)
        grid.addWidget(self.cmb_encargado,       0, 3)

        grid.addWidget(QLabel("Fecha Inicio:"),  1, 0)
        grid.addWidget(self.dt_inicio,           1, 1)

        grid.addWidget(QLabel("Fecha Fin:"),     1, 2)
        grid.addWidget(self.dt_fin,              1, 3)

        grid.addWidget(QLabel("Presupuesto:"),   2, 0)
        grid.addWidget(self.spn_presupuesto,     2, 1)

        grid.addWidget(QLabel("Estado:"),        2, 2)
        grid.addWidget(self.chk_finalizado,      2, 3)

        grid.setColumnStretch(1, 1)
        grid.setColumnStretch(3, 1)

        gb_proyecto.setLayout(grid)

        # ====== FAMILIAS BENEFICIADAS ======
        gb_familias = QGroupBox("Familias beneficiadas")

        vbox_familias = QVBoxLayout()
        self.tbl_familias = QTableWidget()
        self.tbl_familias.setColumnCount(4)
        self.tbl_familias.setHorizontalHeaderLabels(
            ["Nombre", "Dirección", "Ingresos", "Integrantes"]
        )
        self.tbl_familias.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        btn_fam = QHBoxLayout()
        self.btn_add_familia = QPushButton("Agregar familia")
        self.btn_edit_familia = QPushButton("Editar familia")
        self.btn_del_familia = QPushButton("Eliminar familia")
        btn_fam.addWidget(self.btn_add_familia)
        btn_fam.addWidget(self.btn_edit_familia)
        btn_fam.addWidget(self.btn_del_familia)

        vbox_familias.addWidget(self.tbl_familias)
        vbox_familias.addLayout(btn_fam)
        gb_familias.setLayout(vbox_familias)

        # ====== BOTONES GENERALES ======
        btns = QHBoxLayout()
        self.btn_guardar = QPushButton("💾 Guardar proyecto")
        self.btn_cancelar = QPushButton("Cancelar")
        btns.addWidget(self.btn_guardar)
        btns.addWidget(self.btn_cancelar)

        # ENSAMBLE
        layout.addWidget(gb_proyecto)
        layout.addWidget(gb_familias)
        layout.addLayout(btns)
        self.setLayout(layout)
