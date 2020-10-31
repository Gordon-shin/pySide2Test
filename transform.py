from PySide2 import QtWidgets, QtXml
from PySide2.QtWidgets import QApplication, QMessageBox, QFileDialog
from PySide2.QtUiTools import QUiLoader
from Function.ExcelHandler import ExcelHandler


class Excel:
    def __init__(self):
        self.ui = QUiLoader().load('ui/transform.ui')
        """:rtype : PySide2.QtWidgets"""
        self.ui.SRButton.clicked.connect(self.SRButtomHandler)
        self.ui.SCButton.clicked.connect(self.SCButtonHandler)
        self.ui.CreateButton.clicked.connect(self.CreateButtonHandler)
    """输入文件选择器"""
    def SRButtomHandler(self):
        self.srfilepath =self.openFileBrowser()
        self.ui.SRlineEdit.setText(self.srfilepath)

    """创建的文件路径函数"""
    def SCButtonHandler(self):
        self.scfilepath =self.openDirBrowser()
        self.ui.SClineEdit.setText(self.scfilepath)

    def openDirBrowser(self):
        dialog = QtWidgets.QFileDialog()
        #dialog.setFileMode(QFileDialog.FileMode.Directory)
        path = dialog.getExistingDirectory(None, "Select Directory")
        print(path)
        return path

    def openFileBrowser(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        path, _ = dialog.getOpenFileName()
        return path
        print(path)


    def CreateButtonHandler(self):
        self.columns = self.ui.LSlineEdit.text()
        print(self.columns)
        try:
            excel = ExcelHandler(self.srfilepath,self.scfilepath,self.columns,"")
            excel.create_md5_xls()
            MessageBox = QMessageBox()
            MessageBox.information(self.ui,"成功！","转换成功")
        except Exception as e:
            MessageBox = QMessageBox()
            MessageBox.critical(self.ui, "失败", str(e))


if __name__ == '__main__':
    app = QApplication([])
    excel =Excel()
    excel.ui.show()
    app.exec_()