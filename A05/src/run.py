import sys, controller
from PySide.QtGui import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = controller.Controller()
    c.show()

    sys.exit(app.exec_())
