from PyQt6.QtWidgets import QApplication


def center_on_screen(view):
    screen = QApplication.primaryScreen()
    screen_geometry = screen.availableGeometry()
    window_geometry = view.frameGeometry()
    window_geometry.moveCenter(screen_geometry.center())
    view.move(window_geometry.topLeft())
