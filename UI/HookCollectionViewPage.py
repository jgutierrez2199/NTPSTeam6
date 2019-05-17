# Software Engineering II
# Dr.Salamah
# Team 6 - Byte Me

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget

class HookCollectionViewPage(QWidget):

    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.setObjectName("HookCollectionViewPage")
        self.HookCollectionLabel = QtWidgets.QLabel(self)
        self.HookCollectionLabel.setGeometry(QtCore.QRect(0, 0, 841, 51))
        self.HookCollectionLabel.setStyleSheet("border-style: solid solid none solid;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgb(111, 168, 220), stop:1 rgb(159, 197, 232));")
        self.HookCollectionLabel.setObjectName("HookCollectionLabel")
        self.HCVAddHookButton = QtWidgets.QPushButton(self)
        self.HCVAddHookButton.setGeometry(QtCore.QRect(20, 70, 151, 31))
        self.HCVAddHookButton.setStyleSheet("background-color: rgb(244, 244, 244);\n"
"box-shadow:    3px 3px rgb(239, 239, 239);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.HCVAddHookButton.setCheckable(False)
        self.HCVAddHookButton.setChecked(False)
        self.HCVAddHookButton.setFlat(False)
        self.HCVAddHookButton.setObjectName("HCVAddHookButton")
        self.HCVSearchBox = QtWidgets.QLineEdit(self)
        self.HCVSearchBox.setGeometry(QtCore.QRect(580, 69, 241, 31))
        self.HCVSearchBox.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.HCVSearchBox.setClearButtonEnabled(False)
        self.HCVSearchBox.setObjectName("HCVSearchBox")
        self.HCVDeleteHookButton = QtWidgets.QPushButton(self)
        self.HCVDeleteHookButton.setGeometry(QtCore.QRect(260, 70, 71, 31))
        self.HCVDeleteHookButton.setStyleSheet("background-color: rgb(244, 244, 244);\n"
"box-shadow:    3px 3px rgb(239, 239, 239);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.HCVDeleteHookButton.setCheckable(False)
        self.HCVDeleteHookButton.setChecked(False)
        self.HCVDeleteHookButton.setFlat(False)
        self.HCVDeleteHookButton.setObjectName("HCVDeleteHookButton")
        self.HCVEditHookButton = QtWidgets.QPushButton(self)
        self.HCVEditHookButton.setGeometry(QtCore.QRect(180, 70, 71, 31))
        self.HCVEditHookButton.setStyleSheet("background-color: rgb(244, 244, 244);\n"
"box-shadow:    3px 3px rgb(239, 239, 239);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.HCVEditHookButton.setCheckable(False)
        self.HCVEditHookButton.setChecked(False)
        self.HCVEditHookButton.setFlat(False)
        self.HCVEditHookButton.setObjectName("HCVEditHookButton")
        self.HCVSearchLable = QtWidgets.QLabel(self)
        self.HCVSearchLable.setGeometry(QtCore.QRect(490, 80, 71, 21))
        self.HCVSearchLable.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.HCVSearchLable.setObjectName("HCVSearchLable")
        self.HVHookPropertiesWidget_2 = QtWidgets.QWidget(self)
        self.HVHookPropertiesWidget_2.setGeometry(QtCore.QRect(20, 120, 801, 711))
        self.HVHookPropertiesWidget_2.setObjectName("HVHookPropertiesWidget_2")
        self.HookCollectionPropertiesLable = QtWidgets.QLabel(self.HVHookPropertiesWidget_2)
        self.HookCollectionPropertiesLable.setGeometry(QtCore.QRect(0, 0, 801, 41))
        self.HookCollectionPropertiesLable.setStyleSheet("border-style: solid solid none solid;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgb(111, 168, 220), stop:1 rgb(159, 197, 232));")
        self.HookCollectionPropertiesLable.setObjectName("HookCollectionPropertiesLable")
        self.HVHookCollectionPropertiesFrame = QtWidgets.QFrame(self)
        self.HVHookCollectionPropertiesFrame.setGeometry(QtCore.QRect(20, 120, 801, 711))
        self.HVHookCollectionPropertiesFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.HVHookCollectionPropertiesFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.HVHookCollectionPropertiesFrame.setLineWidth(1)
        self.HVHookCollectionPropertiesFrame.setObjectName("HVHookCollectionPropertiesFrame")
        # Hook View Table #
        self.tableWidget = QtWidgets.QTableWidget(self.HVHookCollectionPropertiesFrame)
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
        self.tableWidget.setColumnCount(5)
        header_labels = [' ', 'Hook Collection', 'No. of Hooks', 'Hook Collection Status', 'Hook Collection Execution Sequence']
        self.tableWidget.setHorizontalHeaderLabels(header_labels)
        self.tableWidget.horizontalHeader().setStyleSheet(
                "QHeaderView {font-size: 11; font-weight: bold; text-align: center;}")
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.retranslatePage()

    def retranslatePage(self):
            _translate = QtCore.QCoreApplication.translate
            self.HookCollectionLabel.setText(_translate("MainWindow",
                                                                          "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Hook Collection View</span></p></body></html>"))
            self.HCVAddHookButton.setText(_translate("MainWindow", "+Hook Collection"))
            self.HCVSearchBox.setPlaceholderText(_translate("MainWindow", "Name of Hook Collection"))
            self.HCVDeleteHookButton.setText(_translate("MainWindow", "Delete"))
            self.HCVEditHookButton.setText(_translate("MainWindow", "Edit"))
            self.HCVSearchLable.setText(_translate("MainWindow",
                                                                     "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt; font-weight:600;\">Search</span></p></body></html>"))
            self.HookCollectionPropertiesLable.setText(_translate("MainWindow",
                                                                                    "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Hook Collection Properties</span></p></body></html>"))
            self.tableWidget.setSortingEnabled(True)
            __sortingEnabled = self.tableWidget.isSortingEnabled()
            self.tableWidget.setSortingEnabled(False)
            self.tableWidget.setSortingEnabled(__sortingEnabled)

    def selectedHookCollection(self):
            rowCount = self.tableWidget.rowCount()
            for row in range(rowCount):
                if self.tableWidget.cellWidget(row,0).isChecked():
                    return self.tableWidget.item(row,1).text()

    def addHookCollection(self,Name,Number,Status,Sequence):
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setCellWidget(rowPosition, 0, QtWidgets.QRadioButton(self.tableWidget))
            self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(Name))
            self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(Number))
            self.tableWidget.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(Status))
            self.tableWidget.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(Sequence))