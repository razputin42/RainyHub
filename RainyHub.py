from RainyDM.RainyDM import DMTool
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QHBoxLayout, QPushButton, QSizePolicy
import sys, os


class DMButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


class RainyHub(QMainWindow):
    def __init__(self):
        super().__init__()
        self._setup_ui()
        # self._setup_menu()
        self.bind_signals()
        self._display_ui()
        self.setStyleSheet(open(os.path.join("assets", "styles", "default.css")).read())

    def _setup_ui(self):
        self.window_frame = QFrame()
        self.window_frame.setLayout(QHBoxLayout())
        # self.window_frame.layout().setContentsMargins(0, 0, 0, 0)
        button = DMButton()
        button.clicked.connect(self.open_rainydm)
        self.window_frame.layout().addWidget(button)
        self.setFixedSize(300, 300)
        self.setWindowTitle("RainyHub")

    def bind_signals(self):
        pass

    def _display_ui(self):
        self.setCentralWidget(self.window_frame)

    def open_rainydm(self):
        os.chdir("RainyDM")
        self.rainy_dm = DMTool()
        self.close()
        self.rainy_dm.show()


def open_hub():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    form = RainyHub()  # We set the form to be our ExampleApp (design)

    form.show()  # Show the form
    sys.exit(app.exec_())  # and execute the app


if __name__ == "__main__":
    open_hub()
