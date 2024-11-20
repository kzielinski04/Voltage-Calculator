from PySide6.QtWidgets import QApplication, QWidget

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.setFixedSize(400, 600)
        self.setWindowTitle("Voltage Calculator")
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    app.exec()