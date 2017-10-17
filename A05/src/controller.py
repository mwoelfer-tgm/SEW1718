from PySide.QtGui import *
from PySide.QtCore import *
import view
import model

class Controller(QWidget):
    def __init__(self):
        """
        When the controller gets initialized, the GUI gets set up, a model member is set and the buttons are connected
        to the respective functions

        Important: The Signal on the close Button which closes the windows already got connected
        to the close() slot in the QT-Designer:
        'QtCore.QObject.connect(self.button_close, QtCore.SIGNAL("clicked()"), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)'
        """
        QWidget.__init__(self)
        self.view = view.Ui_Form()
        self.view.setupUi(self)
        self.model = model.Model()
        self.view.button_submit.clicked.connect(self.submit)
        self.view.button_reset.clicked.connect(self.reset)

    def submit(self):
        """
        This method gets called when the Submit button gets pressed

        The get_route function from the model gets called, which returns the route and a status
        :return: None
        """
        # get_route gets called with the route-start, route-destionation and a paremeter which
        # determines whether the query should be done via XML or JSON
        route = self.model.get_route(self.view.input_start.text(), self.view.input_ziel.text(), self.view.mode.isChecked())
        self.view.output.setText(route[0])
        self.view.output_ok.setText(route[1])

    def reset(self):
        """
        Gets called when the reset button is pressed

        Sets all input and output fields to empty strings and unchecks the box
        :return:
        """
        self.view.output.setText("")
        self.view.input_ziel.setText("")
        self.view.input_start.setText("")
        self.view.output_ok.setText("")
        self.view.mode.setChecked(False)