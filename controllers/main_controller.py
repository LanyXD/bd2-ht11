from views.main_window import MainWindow
# views
from views.dashboard_view import DashboardView
from views.projects_view import ProjectsView
from views.managers_view import ManagersView
from views.families_view import FamiliesView


class MainController:
    def __init__(self):
        self.view = MainWindow()

        self.dashboard_view = DashboardView()
        self.projects_view = ProjectsView()
        self.managers_view = ManagersView()
        self.families_view = FamiliesView()

        self.view.add_widget(self.dashboard_view)
        self.view.add_widget(self.projects_view)
        self.view.add_widget(self.managers_view)
        self.view.add_widget(self.families_view)

        self.view.action_dashboard.triggered.connect(lambda: self.page_dashboard())
        self.view.action_projects.triggered.connect(lambda: self.page_projects())
        self.view.action_managers.triggered.connect(lambda: self.page_managers())
        self.view.action_families.triggered.connect(lambda: self.page_families())

    def page_dashboard(self):
        self.view.set_index(0)
        self.view.status_bar.showMessage("Vista: Principal")

    def page_projects(self):
        self.view.set_index(1)
        self.view.status_bar.showMessage("Vista: Proyectos")

    def page_managers(self):
        self.view.set_index(2)
        self.view.status_bar.showMessage("Vista: Encargados")

    def page_families(self):
        self.view.set_index(3)
        self.view.status_bar.showMessage("Vista: Familias")
