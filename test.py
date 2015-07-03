import sys
from PyQt4 import QtGui
import mainform

def main():
    app = QtGui.QApplication(sys.argv)
    form = mainform.MainForm()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()


