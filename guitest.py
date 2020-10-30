from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit

def CalcHandler():
    info = textEdit.toPlainText();
    print("统计按钮被点击了！！"+info)

app = QApplication([])
#图形界面底层管理

window = QMainWindow()
window.resize(500, 400) #控制窗口大小
window.move(300, 310) #在显示器的位置
window.setWindowTitle('薪资统计')

textEdit = QPlainTextEdit(window) #文本编辑框
textEdit.setPlaceholderText("请输入薪资表")
textEdit.move(10,25) #相对于父窗口的位置
textEdit.resize(300,350)

button = QPushButton('统计', window)
button.move(380,80)
#sigal slot
button.clicked.connect(CalcHandler)

window.show()

app.exec_()