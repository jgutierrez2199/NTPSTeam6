# Software Engineering II
# Dr.Salamah
# Team 6 - Byte Me

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HookCollectionExecutionSequenceErrorOverlay(object):
    def setupUi(self, HookCollectionExecutionSequenceErrorOverlay):
        HookCollectionExecutionSequenceErrorOverlay.setObjectName("HookCollectionExecutionSequenceErrorOverlay")
        HookCollectionExecutionSequenceErrorOverlay.resize(708, 202)
        HookCollectionExecutionSequenceErrorOverlay.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame = QtWidgets.QFrame(HookCollectionExecutionSequenceErrorOverlay)
        self.frame.setGeometry(QtCore.QRect(10, 10, 691, 181))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(160, 90, 371, 21))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(110, 60, 481, 21))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(90, 30, 521, 21))
        self.label.setObjectName("label")
        self.NoButton = QtWidgets.QPushButton(self.frame)
        self.NoButton.setGeometry(QtCore.QRect(530, 140, 91, 30))
        self.NoButton.setObjectName("NoButton")
        self.YesButton = QtWidgets.QPushButton(self.frame)
        self.YesButton.setGeometry(QtCore.QRect(430, 140, 91, 30))
        self.YesButton.setObjectName("YesButton")

        self.retranslateUi(HookCollectionExecutionSequenceErrorOverlay)
        QtCore.QMetaObject.connectSlotsByName(HookCollectionExecutionSequenceErrorOverlay)

    def retranslateUi(self, HookCollectionExecutionSequenceErrorOverlay):
        _translate = QtCore.QCoreApplication.translate
        HookCollectionExecutionSequenceErrorOverlay.setWindowTitle(_translate("HookCollectionExecutionSequenceErrorOverlay", "Hook Collection Execution Sequence Error"))
        self.label_3.setText(_translate("HookCollectionExecutionSequenceErrorOverlay", "sequencing for the rest of hook collections?"))
        self.label_2.setText(_translate("HookCollectionExecutionSequenceErrorOverlay", "you like to override the sequence number and update the"))
        self.label.setText(_translate("HookCollectionExecutionSequenceErrorOverlay", "There is another collection with that sequence number. Would"))
        self.NoButton.setText(_translate("HookCollectionExecutionSequenceErrorOverlay", "No"))
        self.YesButton.setText(_translate("HookCollectionExecutionSequenceErrorOverlay", "Yes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HookCollectionExecutionSequenceErrorOverlay = QtWidgets.QDialog()
    ui = Ui_HookCollectionExecutionSequenceErrorOverlay()
    ui.setupUi(HookCollectionExecutionSequenceErrorOverlay)
    HookCollectionExecutionSequenceErrorOverlay.show()
    sys.exit(app.exec_())

