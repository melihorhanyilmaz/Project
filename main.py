from PyQt5.QtWidgets import QApplication
from atmloginpage import LoginScreen
import sys


if __name__ == "__main__":
    app = QApplication([])
    window = LoginScreen()
    window.show()
    sys.exit(app.exec_())