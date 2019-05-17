# Software Engineering II
# Dr.Salamah
# Team 6 - Byte Me

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QFileDialog

class Ui_CreatEditHookOverlay(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.resize(568, 232)
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(10, 10, 551, 211))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.CancelButton = QtWidgets.QPushButton(self.frame)
        self.CancelButton.setGeometry(QtCore.QRect(400, 160, 81, 30))
        self.CancelButton.setObjectName("CancelButton")
        self.HookPath = QtWidgets.QLabel(self.frame)
        self.HookPath.setGeometry(QtCore.QRect(69, 130, 91, 21))
        self.HookPath.setObjectName("HookPath")
        self.BrowseButton = QtWidgets.QPushButton(self.frame)
        self.BrowseButton.setGeometry(QtCore.QRect(400, 120, 81, 30))
        self.BrowseButton.setObjectName("BrowseButton")
        self.SaveButton = QtWidgets.QPushButton(self.frame)
        self.SaveButton.setGeometry(QtCore.QRect(310, 160, 81, 30))
        self.SaveButton.setObjectName("SaveButton")
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
        self.SaveButton.clicked.connect(lambda: self.onSave())
        self.CancelButton.clicked.connect(lambda: self.onCancel())
        self.BrowseButton.clicked.connect(lambda: self.openFileNameDialog())
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.result=[]

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

    def onSave(self):
        self.result = (self.EdiHookName.toPlainText(),self.EditDescription.toPlainText(),self.EditHookPath.toPlainText())
        self.accept()

    def onCancel(self):
        self.close()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*);;Python Files (*.py)", options=options)
        self.EditHookPath.setPlainText(fileName)