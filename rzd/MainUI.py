import sys
from PyQt5 import QtWidgets
from ui import Ui_MainWindow
import json





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
        import sys
        import  subprocess
        from subprocess import check_call
        import os
        #os.system('python rzd.py')        
        #originalDir = os.path.dirname(full_path)
        #check_call([sys.executable or 'python', script_path], cwd=os.path.dirname(script_path))
        subprocess.Popen(['python3', 'rzd.py'])
        #subprocess.Popen([sys.executable,'-c', 'rzd.py'])


app = QtWidgets.QApplication([])
application = RzdPars()
application.show()

sys.exit(app.exec())
