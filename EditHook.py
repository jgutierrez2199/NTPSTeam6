# Software Engineering II
# Dr.Salamah
# Team 6 - Byte Me

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CreatEditHookOverlay(object):
    def setupUi(self, CreatEditHookOverlay):
        CreatEditHookOverlay.setObjectName("CreatEditHookOverlay")
        CreatEditHookOverlay.resize(568, 232)
        CreatEditHookOverlay.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame = QtWidgets.QFrame(CreatEditHookOverlay)
        self.frame.setGeometry(QtCore.QRect(10, 10, 551, 211))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.CancelButton = QtWidgets.QPushButton(self.frame)
        self.CancelButton.setGeometry(QtCore.QRect(400, 160, 81, 30))
        self.CancelButton.setObjectName("CancelButton")
        self.CancelButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.HookPath = QtWidgets.QLabel(self.frame)
        self.HookPath.setGeometry(QtCore.QRect(69, 130, 91, 21))
        self.HookPath.setObjectName("HookPath")
        self.BrowseButton = QtWidgets.QPushButton(self.frame)
        self.BrowseButton.setGeometry(QtCore.QRect(400, 120, 81, 30))
        self.BrowseButton.setObjectName("BrowseButton")
        #self.BrowseButton.clicked.connect(self.file_open())


        self.SaveButton = QtWidgets.QPushButton(self.frame)
        self.SaveButton.setGeometry(QtCore.QRect(310, 160, 81, 30))
        self.SaveButton.setObjectName("SaveButton")
        self.SaveButton.clicked.connect(
            QtCore.QCoreApplication.instance().quit)
        self.EditDescription = QtWidgets.QTextEdit(self.frame)
        self.EditDescription.setGeometry(QtCore.QRect(170, 70, 311, 41))
        self.EditDescription.setObjectName("EditDescription")
        self.HookName = QtWidgets.QLabel(self.frame)
        self.HookName.setGeometry(QtCore.QRect(59, 40, 101, 21))
        self.HookName.setObjectName("HookName")
        self.EdiHookName = QtWidgets.QTextEdit(self.frame)
        self.EdiHookName.setGeometry(QtCore.QRect(170, 30, 311, 31))
        self.EdiHookName.setDocumentTitle("")
        self.EdiHookName.setObjectName("EdiHookName")
        self.Description = QtWidgets.QLabel(self.frame)
        self.Description.setGeometry(QtCore.QRect(59, 80, 101, 21))
        self.Description.setObjectName("Description")
        self.EditHookPath = QtWidgets.QTextEdit(self.frame)
        self.EditHookPath.setGeometry(QtCore.QRect(170, 120, 221, 31))
        self.EditHookPath.setObjectName("EditHookPath")
        

        self.retranslateUi(CreatEditHookOverlay)
        QtCore.QMetaObject.connectSlotsByName(CreatEditHookOverlay)

    def retranslateUi(self, CreatEditHookOverlay):
        _translate = QtCore.QCoreApplication.translate
        CreatEditHookOverlay.setWindowTitle(_translate("CreatEditHookOverlay", "Create/Edit Hook"))
        self.CancelButton.setText(_translate("CreatEditHookOverlay", "Cancel"))
        self.HookPath.setText(_translate("CreatEditHookOverlay", "Hook Path"))
        self.BrowseButton.setText(_translate("CreatEditHookOverlay", "Browse"))
        self.SaveButton.setText(_translate("CreatEditHookOverlay", "Save"))
        self.EditDescription.setPlaceholderText(_translate("CreatEditHookOverlay", "                    Hook Description"))
        self.HookName.setText(_translate("CreatEditHookOverlay", "Hook Name"))
        self.EdiHookName.setPlaceholderText(_translate("CreatEditHookOverlay", "                         Hook Name"))
        self.Description.setText(_translate("CreatEditHookOverlay", "Description"))
        self.EditHookPath.setPlaceholderText(_translate("CreatEditHookOverlay", "               Hook Path"))

    def file_open(self):
        pass
        # options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        # name, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "", "All Files (*);;Python Files (*.py)", options=options)
        # self.HookPath.setText(name)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    CreatEditHookOverlay = QtWidgets.QDialog()
    ui = Ui_CreatEditHookOverlay()
    ui.setupUi(CreatEditHookOverlay)
    CreatEditHookOverlay.show()
    sys.exit(app.exec_())

