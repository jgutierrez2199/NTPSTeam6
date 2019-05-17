# Software Engineering II
# Dr.Salamah
# Team 6 - Byte Me

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFrame, QWidget

class OptionViewFrame(QFrame):

    def __init__(self,parent=QWidget):
        QFrame.__init__(self,parent)
        self.setGeometry(QtCore.QRect(10, 10, 251, 851))
        self.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setObjectName("OptionViewFrame")
        self.OptionViewLable = QtWidgets.QLabel(self)
        self.OptionViewLable.setGeometry(QtCore.QRect(0, 0, 251, 51))
        self.OptionViewLable.setStyleSheet("border-style: solid solid none solid;\n"
                                           "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgb(111, 168, 220), stop:1 rgb(159, 197, 232));")
        self.OptionViewLable.setObjectName("OptionViewLable")
        self.OVHookCollectionButton = QtWidgets.QPushButton(self)
        self.OVHookCollectionButton.setGeometry(QtCore.QRect(10, 120, 231, 51))
        self.OVHookCollectionButton.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.OVHookCollectionButton.setCheckable(True)
        self.OVHookCollectionButton.setChecked(False)
        self.OVHookCollectionButton.setFlat(True)
        self.OVHookCollectionButton.setObjectName("OVHookCollectionButton")
        self.OVLivePacketButton = QtWidgets.QPushButton(self)
        self.OVLivePacketButton.setGeometry(QtCore.QRect(10, 180, 231, 51))
        self.OVLivePacketButton.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.OVLivePacketButton.setCheckable(True)
        self.OVLivePacketButton.setChecked(False)
        self.OVLivePacketButton.setAutoDefault(False)
        self.OVLivePacketButton.setDefault(False)
        self.OVLivePacketButton.setFlat(True)
        self.OVLivePacketButton.setObjectName("OVLivePacketButton")
        self.OVPacketPCAPButton = QtWidgets.QPushButton(self)
        self.OVPacketPCAPButton.setGeometry(QtCore.QRect(10, 240, 231, 51))
        self.OVPacketPCAPButton.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.OVPacketPCAPButton.setCheckable(True)
        self.OVPacketPCAPButton.setChecked(False)
        self.OVPacketPCAPButton.setFlat(True)
        self.OVPacketPCAPButton.setObjectName("OVPacketPCAPButton")
        self.OVHookButton = QtWidgets.QPushButton(self)
        self.OVHookButton.setGeometry(QtCore.QRect(10, 60, 231, 51))
        self.OVHookButton.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
                                        "")
        self.OVHookButton.setCheckable(True)
        self.OVHookButton.setChecked(False)
        self.OVHookButton.setFlat(True)
        self.OVHookButton.setObjectName("OVHookButton")
        self.OVButtonGroup = QtWidgets.QButtonGroup(self)
        self.OVButtonGroup.addButton(self.OVHookCollectionButton)
        self.OVButtonGroup.addButton(self.OVHookButton)
        self.OVButtonGroup.addButton(self.OVLivePacketButton)
        self.OVButtonGroup.addButton(self.OVPacketPCAPButton)
        self.retranslatePage()

    def retranslatePage(self):
            _translate = QtCore.QCoreApplication.translate
            self.OptionViewLable.setText(_translate("MainWindow",
                                                    "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Option View</span></p></body></html>"))
            self.OVHookCollectionButton.setText(_translate("MainWindow", "Hook Collection"))
            self.OVLivePacketButton.setText(_translate("MainWindow", "Live Packet"))
            self.OVPacketPCAPButton.setText(_translate("MainWindow", "Packet from PCAP"))
            self.OVHookButton.setText(_translate("MainWindow", "Hook"))