import os
import sys 
from PyQt5.QtWidgets import *


def main(): 
    app = QApplication(sys.argv) 
                                                                                          

    w = MyWindow() 
    w.show() 
    sys.exit(app.exec_()) 

 
class MyWindow(QWidget): 
    def __init__(self, *args): 
        QWidget.__init__(self, *args) 
 
        label = QLabel(self.tr("Press ENTER to see the status of a default process with PID: 2006   "))
        self.le = QLineEdit("PRESS ENTER!")
        self.te = QTextEdit()
        layout = QVBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(self.le)
        layout.addWidget(self.te)
        self.setLayout(layout) 
        self.le.returnPressed.connect(self.run_command)

    def run_command(self):
        cmd = 'cat /proc/2006/status'
	
        a = os.popen(cmd).read()
        self.te.setText(a)
  
if __name__ == "__main__": 
    main()
