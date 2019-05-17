# Software Engineering II
# Dr.Salamah
# Team 6 - Byte Me

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget

class HookViewPage(QWidget):

    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.setObjectName("HookViewPage")
        self.HookViewLable = QtWidgets.QLabel(self)
        self.HookViewLable.setGeometry(QtCore.QRect(0, 0, 841, 51))
        self.HookViewLable.setStyleSheet("border-style: solid solid none solid;\n"
                                         "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgb(111, 168, 220), stop:1 rgb(159, 197, 232));")
        self.HookViewLable.setObjectName("HookViewLable")
        self.HVAddHookButton = QtWidgets.QPushButton(self)
        self.HVAddHookButton.setGeometry(QtCore.QRect(20, 70, 71, 31))
        self.HVAddHookButton.setStyleSheet("background-color: rgb(244, 244, 244);\n"
                                           "box-shadow:    3px 3px rgb(239, 239, 239);\n"
                                           "font: 12pt \"MS Shell Dlg 2\";")
        self.HVAddHookButton.setCheckable(False)
        self.HVAddHookButton.setChecked(False)
        self.HVAddHookButton.setFlat(False)
        self.HVAddHookButton.setObjectName("HVAddHookButton")
        self.HVEditHookButton = QtWidgets.QPushButton(self)
        self.HVEditHookButton.setGeometry(QtCore.QRect(100, 70, 71, 31))
        self.HVEditHookButton.setStyleSheet("background-color: rgb(244, 244, 244);\n"
                                            "box-shadow:    3px 3px rgb(239, 239, 239);\n"
                                            "font: 12pt \"MS Shell Dlg 2\";")
        self.HVEditHookButton.setCheckable(False)
        self.HVEditHookButton.setChecked(False)
        self.HVEditHookButton.setFlat(False)
        self.HVEditHookButton.setObjectName("HVEditHookButton")
        self.HVDeleteHookButton = QtWidgets.QPushButton(self)
        self.HVDeleteHookButton.setGeometry(QtCore.QRect(180, 70, 71, 31))
        self.HVDeleteHookButton.setStyleSheet("background-color: rgb(244, 244, 244);\n"
                                              "box-shadow:    3px 3px rgb(239, 239, 239);\n"
                                              "font: 12pt \"MS Shell Dlg 2\";")
        self.HVDeleteHookButton.setCheckable(False)
        self.HVDeleteHookButton.setChecked(False)
        self.HVDeleteHookButton.setFlat(False)
        self.HVDeleteHookButton.setObjectName("HVDeleteHookButton")
        self.HVSearchLable = QtWidgets.QLabel(self)
        self.HVSearchLable.setGeometry(QtCore.QRect(490, 80, 71, 21))
        self.HVSearchLable.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.HVSearchLable.setObjectName("HVSearchLable")
        self.HVSearchBox = QtWidgets.QLineEdit(self)
        self.HVSearchBox.setGeometry(QtCore.QRect(580, 69, 241, 31))
        self.HVSearchBox.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.HVSearchBox.setClearButtonEnabled(False)
        self.HVSearchBox.setObjectName("HVSearchBox")
        self.HVHookPropertiesFrame = QtWidgets.QFrame(self)
        self.HVHookPropertiesFrame.setGeometry(QtCore.QRect(20, 120, 801, 711))
        self.HVHookPropertiesFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.HVHookPropertiesFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.HVHookPropertiesFrame.setLineWidth(1)
        self.HVHookPropertiesFrame.setObjectName("HVHookPropertiesFrame")
        self.HookPropertiesLable = QtWidgets.QLabel(self.HVHookPropertiesFrame)
        self.HookPropertiesLable.setGeometry(QtCore.QRect(0, 0, 801, 41))
        self.HookPropertiesLable.setStyleSheet("border-style: solid solid none solid;\n"
                                               "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgb(111, 168, 220), stop:1 rgb(159, 197, 232));")
        self.HookPropertiesLable.setObjectName("HookPropertiesLable")
        # Hook View Table #
        self.tableWidget = QtWidgets.QTableWidget(self.HVHookPropertiesFrame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 781, 650))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideNone)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        header_labels = [' ', 'Hook', 'Description', 'Association to Hook Collection']
        self.tableWidget.setHorizontalHeaderLabels(header_labels)
        self.tableWidget.horizontalHeader().setStyleSheet("QHeaderView {font-size: 11; font-weight: bold; text-align: center;}")
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.retranslatePage()

    def retranslatePage(self):
            _translate = QtCore.QCoreApplication.translate
            self.HookViewLable.setText(_translate("MainWindow",
                                                  "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Hook View</span></p></body></html>"))
            self.HVAddHookButton.setText(_translate("MainWindow", "+Hook"))
            self.HVEditHookButton.setText(_translate("MainWindow", "Edit"))
            self.HVDeleteHookButton.setText(_translate("MainWindow", "Delete"))
            self.HVSearchLable.setText(_translate("MainWindow",
                                                  "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt; font-weight:600;\">Search</span></p></body></html>"))
            self.HVSearchBox.setPlaceholderText(_translate("MainWindow", "Name of Hook"))
            self.HookPropertiesLable.setText(_translate("MainWindow",
                                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Hook Properties</span></p></body></html>"))
            self.tableWidget.setSortingEnabled(True)
            __sortingEnabled = self.tableWidget.isSortingEnabled()
            self.tableWidget.setSortingEnabled(False)
            self.tableWidget.setSortingEnabled(__sortingEnabled)

    def addHook(self, Name, Description, Association):
            rowPosition=self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setCellWidget(rowPosition, 0, QtWidgets.QRadioButton(self.tableWidget))
            self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(Name))
            self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(Description))
            self.tableWidget.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(Association))

    def deleteHook(self):
            rowCount = self.tableWidget.rowCount()
            for row in range(rowCount):
                if self.tableWidget.cellWidget(row,0).isChecked():
                    self.tableWidget.removeRow(row)
                    return