# Software Engineering II
# Dr.Salamah
# Team 6 - Byte Me

from MainWindow import Ui_MainWindow
from PyQt5 import QtWidgets
import HookExecutionSequenceErrorOverlay, EditHookCollectionOverlay

class UIControl(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(UIControl, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.OptionViewFrame.OVHookCollectionButton.clicked.connect(lambda: self.changeView(0))
        self.ui.OptionViewFrame.OVHookButton.clicked.connect(lambda: self.changeView(1))
        self.ui.OptionViewFrame.OVLivePacketButton.clicked.connect(lambda: self.changeView(2))
        self.ui.OptionViewFrame.OVPacketPCAPButton.clicked.connect(lambda: self.changeView(3))

        self.ui.HookViewPage.HVEditHookButton.clicked.connect(lambda: self.showDialog())
        # Example ADD Hook #
        self.ui.HookViewPage.HVAddHookButton.clicked.connect(lambda: self.ui.HookViewPage.addHook("Hook 1", "Hook 1 description", "1"))
        # Example Delete Hook #
        self.ui.HookViewPage.HVDeleteHookButton.clicked.connect(lambda: self.ui.HookViewPage.deleteHook())

    def changeView (self, index):
        self.ui.ContentViewWidget.setCurrentIndex(index)

    def showDialog (self):
        dialog = QtWidgets.QDialog()
        ui = EditHookCollectionOverlay.Ui_Dialog()
        ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mySW = UIControl()
    mySW.show()
    sys.exit(app.exec_())