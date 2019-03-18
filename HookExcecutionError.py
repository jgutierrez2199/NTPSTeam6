# Software Engineering II
# Dr.Salamah
# Team 6 - Byte Me

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HookExecutionErrorOverlay(object):
    def setupUi(self, HookExecutionSequenceErrorOverlay):
        HookExecutionSequenceErrorOverlay.setObjectName("HookExecutionSequenceErrorOverlay")
        HookExecutionSequenceErrorOverlay.resize(708, 202)
        HookExecutionSequenceErrorOverlay.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame = QtWidgets.QFrame(HookExecutionSequenceErrorOverlay)
        self.frame.setGeometry(QtCore.QRect(10, 10, 691, 181))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(100, 90, 491, 21))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(130, 60, 481, 21))
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

        self.retranslateUi(HookExecutionSequenceErrorOverlay)
        QtCore.QMetaObject.connectSlotsByName(HookExecutionSequenceErrorOverlay)

    def retranslateUi(self, HookExecutionSequenceErrorOverlay):
        _translate = QtCore.QCoreApplication.translate
        HookExecutionSequenceErrorOverlay.setWindowTitle(_translate("HookExecutionSequenceErrorOverlay", "Hook Execution Sequence Error"))
        self.label_3.setText(_translate("HookExecutionSequenceErrorOverlay", "sequencing for the rest of hooks within this hook colection?"))
        self.label_2.setText(_translate("HookExecutionSequenceErrorOverlay", "like to override the sequence number and update the"))
        self.label.setText(_translate("HookExecutionSequenceErrorOverlay", "There is another Hook with that sequence number. Would you"))
        self.NoButton.setText(_translate("HookExecutionSequenceErrorOverlay", "No"))
        self.YesButton.setText(_translate("HookExecutionSequenceErrorOverlay", "Yes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HookExecutionSequenceErrorOverlay = QtWidgets.QDialog()
    ui = Ui_HookExecutionSequenceErrorOverlay()
    ui.setupUi(HookExecutionSequenceErrorOverlay)
    HookExecutionSequenceErrorOverlay.show()
    sys.exit(app.exec_())

