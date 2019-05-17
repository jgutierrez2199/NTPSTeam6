# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Escritorio\Desktop\Python UI\PythonUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import HookExecutionSequenceErrorOverlay

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1118, 870)
        MainWindow.setStyleSheet("")
        self.MainWidget = QtWidgets.QWidget(MainWindow)
        self.MainWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MainWidget.setObjectName("MainWidget")
        self.ContentViewWidget = QtWidgets.QStackedWidget(self.MainWidget)
        self.ContentViewWidget.setGeometry(QtCore.QRect(269, 10, 841, 851))
        self.ContentViewWidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgb(231, 231, 231), stop:1 rgba(255, 255, 255, 255));")
        self.ContentViewWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.ContentViewWidget.setLineWidth(1)
        self.ContentViewWidget.setMidLineWidth(0)
        self.ContentViewWidget.setObjectName("ContentViewWidget")
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.page1Lable = QtWidgets.QLabel(self.page1)
        self.page1Lable.setGeometry(QtCore.QRect(0, 0, 841, 51))
        self.page1Lable.setStyleSheet("border-style: solid solid none solid;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgb(111, 168, 220), stop:1 rgb(159, 197, 232));")
        self.page1Lable.setObjectName("page1Lable")
        self.ContentViewWidget.addWidget(self.page1)
        self.HookViewPage = QtWidgets.QWidget()
        self.HookViewPage.setObjectName("HookViewPage")
        self.HookViewLable = QtWidgets.QLabel(self.HookViewPage)
        self.HookViewLable.setGeometry(QtCore.QRect(0, 0, 841, 51))
        self.HookViewLable.setStyleSheet("border-style: solid solid none solid;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgb(111, 168, 220), stop:1 rgb(159, 197, 232));")
        self.HookViewLable.setObjectName("HookViewLable")
        self.HVAddHookButton = QtWidgets.QPushButton(self.HookViewPage)
        self.HVAddHookButton.setGeometry(QtCore.QRect(20, 70, 71, 31))
        self.HVAddHookButton.setStyleSheet("background-color: rgb(244, 244, 244);\n"
"box-shadow:    3px 3px rgb(239, 239, 239);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.HVAddHookButton.setCheckable(False)
        self.HVAddHookButton.setChecked(False)
        self.HVAddHookButton.setFlat(False)
        self.HVAddHookButton.setObjectName("HVAddHookButton")
        self.HVEditHookButton = QtWidgets.QPushButton(self.HookViewPage)
        self.HVEditHookButton.setGeometry(QtCore.QRect(100, 70, 71, 31))
        self.HVEditHookButton.setStyleSheet("background-color: rgb(244, 244, 244);\n"
"box-shadow:    3px 3px rgb(239, 239, 239);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.HVEditHookButton.setCheckable(False)
        self.HVEditHookButton.setChecked(False)
        self.HVEditHookButton.setFlat(False)
        self.HVEditHookButton.setObjectName("HVEditHookButton")
        self.HVDeleteHookButton = QtWidgets.QPushButton(self.HookViewPage)
        self.HVDeleteHookButton.setGeometry(QtCore.QRect(180, 70, 71, 31))
        self.HVDeleteHookButton.setStyleSheet("background-color: rgb(244, 244, 244);\n"
"box-shadow:    3px 3px rgb(239, 239, 239);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.HVDeleteHookButton.setCheckable(False)
        self.HVDeleteHookButton.setChecked(False)
        self.HVDeleteHookButton.setFlat(False)
        self.HVDeleteHookButton.setObjectName("HVDeleteHookButton")
        self.HVSearchLable = QtWidgets.QLabel(self.HookViewPage)
        self.HVSearchLable.setGeometry(QtCore.QRect(490, 80, 71, 21))
        self.HVSearchLable.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.HVSearchLable.setObjectName("HVSearchLable")
        self.HVSearchBox = QtWidgets.QLineEdit(self.HookViewPage)
        self.HVSearchBox.setGeometry(QtCore.QRect(580, 69, 241, 31))
        self.HVSearchBox.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.HVSearchBox.setClearButtonEnabled(False)
        self.HVSearchBox.setObjectName("HVSearchBox")
        self.HVHookPropertiesWidget = QtWidgets.QWidget(self.HookViewPage)
        self.HVHookPropertiesWidget.setGeometry(QtCore.QRect(20, 120, 801, 711))
        self.HVHookPropertiesWidget.setObjectName("HVHookPropertiesWidget")
        self.HookPropertiesLable = QtWidgets.QLabel(self.HVHookPropertiesWidget)
        self.HookPropertiesLable.setGeometry(QtCore.QRect(0, 0, 801, 41))
        self.HookPropertiesLable.setStyleSheet("border-style: solid solid none solid;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgb(111, 168, 220), stop:1 rgb(159, 197, 232));")
        self.HookPropertiesLable.setObjectName("HookPropertiesLable")
        self.HPTableView = QtWidgets.QTableView(self.HVHookPropertiesWidget)
        self.HPTableView.setGeometry(QtCore.QRect(50, 60, 741, 201))
        self.HPTableView.setSortingEnabled(True)
        self.HPTableView.setObjectName("HPTableView")
        self.HPRadioButton1 = QtWidgets.QRadioButton(self.HVHookPropertiesWidget)
        self.HPRadioButton1.setGeometry(QtCore.QRect(20, 100, 16, 18))
        self.HPRadioButton1.setText("")
        self.HPRadioButton1.setObjectName("HPRadioButton1")
        self.ContentViewWidget.addWidget(self.HookViewPage)
        self.OptionViewWidget = QtWidgets.QWidget(self.MainWidget)
        self.OptionViewWidget.setGeometry(QtCore.QRect(10, 10, 251, 851))
        self.OptionViewWidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgb(231, 231, 231), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid rgb(0, 0, 0);")
        self.OptionViewWidget.setObjectName("OptionViewWidget")
        self.OptionViewLable = QtWidgets.QLabel(self.OptionViewWidget)
        self.OptionViewLable.setGeometry(QtCore.QRect(0, 0, 251, 51))
        self.OptionViewLable.setStyleSheet("border-style: solid solid none solid;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgb(111, 168, 220), stop:1 rgb(159, 197, 232));")
        self.OptionViewLable.setObjectName("OptionViewLable")
        self.OVHookCollectionButton = QtWidgets.QPushButton(self.OptionViewWidget)
        self.OVHookCollectionButton.setGeometry(QtCore.QRect(10, 120, 231, 51))
        self.OVHookCollectionButton.setStyleSheet("background-color: rgb(255, 255, 255, 0.1);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.OVHookCollectionButton.setCheckable(True)
        self.OVHookCollectionButton.setChecked(False)
        self.OVHookCollectionButton.setFlat(False)
        self.OVHookCollectionButton.setObjectName("OVHookCollectionButton")
        self.OVLivePacketButton = QtWidgets.QPushButton(self.OptionViewWidget)
        self.OVLivePacketButton.setGeometry(QtCore.QRect(10, 180, 231, 51))
        self.OVLivePacketButton.setStyleSheet("background-color: rgb(255, 255, 255, 0.1);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.OVLivePacketButton.setCheckable(True)
        self.OVLivePacketButton.setChecked(False)
        self.OVLivePacketButton.setFlat(False)
        self.OVLivePacketButton.setObjectName("OVLivePacketButton")
        self.OVPacketPCAPButton = QtWidgets.QPushButton(self.OptionViewWidget)
        self.OVPacketPCAPButton.setGeometry(QtCore.QRect(10, 240, 231, 51))
        self.OVPacketPCAPButton.setStyleSheet("background-color: rgb(255, 255, 255, 0.1);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.OVPacketPCAPButton.setCheckable(True)
        self.OVPacketPCAPButton.setChecked(False)
        self.OVPacketPCAPButton.setFlat(False)
        self.OVPacketPCAPButton.setObjectName("OVPacketPCAPButton")
        self.OVHookButton = QtWidgets.QPushButton(self.OptionViewWidget)
        self.OVHookButton.setGeometry(QtCore.QRect(10, 60, 231, 51))
        self.OVHookButton.setStyleSheet("background-color: rgb(255, 255, 255, 0.1);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.OVHookButton.setCheckable(True)
        self.OVHookButton.setChecked(False)
        self.OVHookButton.setFlat(False)
        self.OVHookButton.setObjectName("OVHookButton")
        MainWindow.setCentralWidget(self.MainWidget)

        self.retranslateUi(MainWindow)
        self.ContentViewWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Network Trafic Proxy System"))
        self.page1Lable.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Content View</span></p></body></html>"))
        self.HookViewLable.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Hook View</span></p></body></html>"))
        self.HVAddHookButton.setText(_translate("MainWindow", "+Hook"))
        self.HVEditHookButton.setText(_translate("MainWindow", "Edit"))
        self.HVDeleteHookButton.setText(_translate("MainWindow", "Delete"))
        self.HVSearchLable.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt; font-weight:600;\">Search</span></p></body></html>"))
        self.HVSearchBox.setPlaceholderText(_translate("MainWindow", "Name of Hook"))
        self.HookPropertiesLable.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Hook Properties</span></p></body></html>"))
        self.OptionViewLable.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Option View</span></p></body></html>"))
        self.OVHookCollectionButton.setText(_translate("MainWindow", "Hook Collection"))
        self.OVLivePacketButton.setText(_translate("MainWindow", "Live Packet"))
        self.OVPacketPCAPButton.setText(_translate("MainWindow", "Packet from PCAP"))
        self.OVHookButton.setText(_translate("MainWindow", "Hook"))


class ControlMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.OVHookCollectionButton.clicked.connect(lambda: self.ui.ContentViewWidget.setCurrentIndex(0))
        self.ui.OVHookButton.clicked.connect(lambda: self.ui.ContentViewWidget.setCurrentIndex(1))
        self.ui.HVEditHookButton.clicked.connect(lambda: self.showDialog(self))

    def showDialog(self):
        dialog = QtWidgets.QDialog()
        ui = HookExecutionSequenceErrorOverlay.Ui_Dialog()
        ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())

