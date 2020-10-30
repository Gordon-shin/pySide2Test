import PySide2
from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication, QMessageBox, QFileDialog, QLineEdit
from PySide2.QtUiTools import QUiLoader


class Excel:
    def __init__(self):
        self.ui = QUiLoader().load('ui/transform.ui')
        self.ui.SRButton.clicked.connect(self.SRButtomHandler)
    def SRButtomHandler(self):
        self.openFileBrowser()
        ''':type : PySide2.QtWidgets.QLineEdit'''
        self.SRlineEdit

    def openFileBrowser(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        path, _ = dialog.getOpenFileName()
        self.srfilepath =path
        print(path)



if __name__ == '__main__':
    app = QApplication([])
    excel =Excel()
    excel.ui.show()
    app.exec_()