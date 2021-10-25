import sys
from PyQt5 import QtWidgets
from ui import Ui_MainWindow
import json
import  subprocess




class RzdPars(QtWidgets.QMainWindow):
    def __init__(self):
        super(RzdPars, self).__init__()
        with open('routes.json', 'r') as f:
            self.data = json.load(f)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.checkBoxes = []
        self.Init_UI()
        self.updateOut()

    def Init_UI(self):
        self.ui.add_Button.clicked.connect(self.addPath)
        self.ui.delete_last_Button.clicked.connect(self.delLast)
        self.ui.accept_Button.clicked.connect(self.jsonSave)
    def addPath(self):
        if self.ui.input_station_from.text() == '' or self.ui.input_station_to.text() == '' or self.ui.input_date.text() == '':
            return
        else:
            self.data.append([self.ui.input_station_from.text(), self.ui.input_station_to.text(), self.ui.input_date.text()])
            self.updateOut()
    def updateOut(self):
        str = ''
        for e in self.data:
            str = str + e[0] + ' -> ' + e[1] + ' ' + e[2] + '\n'
        self.ui.outputPath.setText(str)

    def delLast(self):
        try:
            self.data.pop()
            self.updateOut()
        except:
            return

    def jsonSave(self):
        with open('routes.json', 'w') as json_data:
            json.dump(self.data, json_data, indent=2)
        subprocess.Popen(['python3', 'rzd.py'])


app = QtWidgets.QApplication([])
application = RzdPars()
application.show()

sys.exit(app.exec())
