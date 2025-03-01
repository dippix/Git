from PyQt5 import QtWidgets, QtCore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.btnAddCircle = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddCircle.setGeometry(QtCore.QRect(240, 10, 150, 40))
        self.btnAddCircle.setObjectName("btnAddCircle")
        self.btnAddCircle.setText("Добавить круг")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Генератор окружностей"))
