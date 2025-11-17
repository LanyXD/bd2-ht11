# views/integrant_dialog.py
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QFormLayout, QLineEdit,
    QSpinBox, QPushButton, QHBoxLayout, QMessageBox
)


class IntegrantDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Nuevo integrante")

        layout = QVBoxLayout()
        form = QFormLayout()

        self.txt_nombre = QLineEdit()
        self.txt_apellido = QLineEdit()
        self.spn_edad = QSpinBox()
        self.spn_edad.setRange(0, 120)

        form.addRow("Nombre:", self.txt_nombre)
        form.addRow("Apellido:", self.txt_apellido)
        form.addRow("Edad:", self.spn_edad)

        btns = QHBoxLayout()
        self.btn_ok = QPushButton("Guardar")
        self.btn_cancel = QPushButton("Cancelar")
        btns.addWidget(self.btn_ok)
        btns.addWidget(self.btn_cancel)

        layout.addLayout(form)
        layout.addLayout(btns)
        self.setLayout(layout)

        self.btn_ok.clicked.connect(self.accept_data)
        self.btn_cancel.clicked.connect(self.reject)

    def accept_data(self):
        if not self.txt_nombre.text().strip():
            QMessageBox.warning(self, "Error", "El nombre es obligatorio.")
            return
        self.accept()

    def get_data(self) -> dict:
        return {
            "nombre": self.txt_nombre.text().strip(),
            "apellido": self.txt_apellido.text().strip(),
            "edad": int(self.spn_edad.value()),
        }
