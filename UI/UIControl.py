# Software Engineering II
# Dr.Salamah
# Team 6 - Byte Me

from MainWindow import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from EditHookOverlay import Ui_CreatEditHookOverlay
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

        self.ui.HookCollectionViewPage.HCVAddHookButton.clicked.connect(lambda: self.showAddHookCollectionOverlay())

        self.ui.HookViewPage.HVAddHookButton.clicked.connect(lambda: self.showAddHooknOverlay())
        self.ui.HookViewPage.HVDeleteHookButton.clicked.connect(lambda: self.deleteHook())

    def changeView (self, index):
        self.ui.ContentViewWidget.setCurrentIndex(index)

    def showAddHooknOverlay (self):
        dialog = Ui_CreatEditHookOverlay()
        if dialog.exec_() == QDialog.Accepted:
            result=dialog.result
            # Send result to Hook Handler, depending of the repsonse add to page #
            self.ui.HookViewPage.addHook(result[0], result[1], "0")

    def deleteHook (self):
        hookToDelete = self.ui.HookViewPage.selectedHook()
        # Alert Hook Handler and pass it hookToDlete #
        self.ui.HookViewPage.deleteHook()

    def showAddHookCollectionOverlay (self):
        dialog = QtWidgets.QDialog()
        overlay = EditHookCollectionOverlay.Ui_CreatEditHookCollectionOverlay()
        overlay.setupUi(dialog)
        dialog.exec_()
        dialog.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mySW = UIControl()
    mySW.show()
    sys.exit(app.exec_())