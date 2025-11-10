from PyQt6.QtWidgets import QMainWindow, QWidget, QStackedLayout, QToolBar, QStatusBar
from PyQt6.QtGui import QAction
from utils.window_utils import center_on_screen


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.status_bar = None
        self.main_layout = None
        self.action_dashboard = None
        self.action_families = None
        self.action_projects = None
        self.action_managers = None
        self.setup_ui()

    def setup_ui(self):
        self.setup_window()
        self.setup_central_widget()
        self.setup_toolbar()
        self.setup_status_bar()

    def setup_window(self):
        self.setWindowTitle("HT-11 | Gestión de Proyectos Comunitarios")
        self.setFixedSize(1024, 700)
        center_on_screen(self)

    def setup_central_widget(self):
        central_widget = QWidget(self)
        self.main_layout = QStackedLayout()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

    def setup_toolbar(self):
        toolbar = QToolBar("Navegación")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        self.action_dashboard = QAction("🏠 Principal", self)
        self.action_projects = QAction("📁 Proyectos", self)
        self.action_managers = QAction("👤 Encargados", self)
        self.action_families = QAction("👪 Familias", self)

        toolbar.addAction(self.action_dashboard)
        toolbar.addSeparator()
        toolbar.addAction(self.action_projects)
        toolbar.addAction(self.action_managers)
        toolbar.addAction(self.action_families)

    def setup_status_bar(self):
        self.status_bar = QStatusBar()
        self.status_bar.showMessage("Listo")
        self.setStatusBar(self.status_bar)

    def add_widget(self, widget):
        self.main_layout.addWidget(widget)

    def set_index(self, index: int):
        self.main_layout.setCurrentIndex(index)
