import sys
from PyQt6.QtWidgets import QApplication
from controllers.main_controller import MainController


def main():
    app = QApplication(sys.argv)
    with open("./rsc/style.qss", "r") as f:
        app.setStyleSheet(f.read())

    main_controller = MainController()
    main_controller.view.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
