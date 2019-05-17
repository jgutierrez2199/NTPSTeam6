# Software Engineering II
# Dr.Salamah
# Team 6 - Byte Me

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CreatEditHookOverlay(object):
    def setupUi(self, CreatEditHookOverlay):
        CreatEditHookOverlay.setObjectName("CreatEditHookOverlay")
        CreatEditHookOverlay.resize(565, 191)
        CreatEditHookOverlay.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame = QtWidgets.QFrame(CreatEditHookOverlay)
        self.frame.setGeometry(QtCore.QRect(10, 10, 551, 211))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.CancelButton = QtWidgets.QPushButton(self.frame)
        self.CancelButton.setGeometry(QtCore.QRect(400, 130, 81, 30))
        self.CancelButton.setObjectName("CancelButton")
        self.CancelButton.clicked.connect(
            QtCore.QCoreApplication.instance().quit)

        self.SaveButton = QtWidgets.QPushButton(self.frame)
        self.SaveButton.setGeometry(QtCore.QRect(310, 130, 81, 30))
        self.SaveButton.setObjectName("SaveButton")
        self.SaveButton.clicked.connect(
            QtCore.QCoreApplication.instance().quit)
            
        self.EditDescription = QtWidgets.QTextEdit(self.frame)
        self.EditDescription.setGeometry(QtCore.QRect(170, 70, 311, 41))
        self.EditDescription.setObjectName("EditDescription")
        self.HookName = QtWidgets.QLabel(self.frame)
        self.HookName.setGeometry(QtCore.QRect(39, 40, 121, 21))
        self.HookName.setObjectName("HookName")
        self.EdiHookName = QtWidgets.QTextEdit(self.frame)
        self.EdiHookName.setGeometry(QtCore.QRect(170, 30, 311, 31))
        self.EdiHookName.setDocumentTitle("")
        self.EdiHookName.setObjectName("EdiHookName")
        self.Description = QtWidgets.QLabel(self.frame)
        self.Description.setGeometry(QtCore.QRect(59, 80, 101, 21))
        self.Description.setObjectName("Description")

        self.retranslateUi(CreatEditHookOverlay)
        QtCore.QMetaObject.connectSlotsByName(CreatEditHookOverlay)

    def retranslateUi(self, CreatEditHookOverlay):
        _translate = QtCore.QCoreApplication.translate
        CreatEditHookOverlay.setWindowTitle(_translate("CreatEditHookOverlay", "Create/Edit Hook"))
        self.CancelButton.setText(_translate("CreatEditHookOverlay", "Cancel"))
        self.SaveButton.setText(_translate("CreatEditHookOverlay", "Save"))
        self.EditDescription.setPlaceholderText(_translate("CreatEditHookOverlay", "                             Description"))
        self.HookName.setText(_translate("CreatEditHookOverlay", "Fuzzed PCAP Name"))
        self.EdiHookName.setPlaceholderText(_translate("CreatEditHookOverlay", "                         Fuzzed PCAP Name"))
        self.Description.setText(_translate("CreatEditHookOverlay", "Description"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreatEditHookOverlay = QtWidgets.QDialog()
    ui = Ui_CreatEditHookOverlay()
    ui.setupUi(CreatEditHookOverlay)
    CreatEditHookOverlay.show()
    sys.exit(app.exec_())

