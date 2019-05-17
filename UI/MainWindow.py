# Software Engineering II
# Dr.Salamah
# Team 6 - Byte Me

from PyQt5 import QtCore, QtWidgets
from HookCollectionViewPage import HookCollectionViewPage
from HookViewPage import HookViewPage
from LivePacketViewPage import LivePacketViewPage
from PCAPViewPage import PCAPViewPage
from OptionViewFrame import OptionViewFrame

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1118, 870)
        MainWindow.setStyleSheet("")
        self.MainWidget = QtWidgets.QWidget(MainWindow)
        self.MainWidget.setObjectName("MainWidget")

        # Content View #
        self.ContentViewWidget = QtWidgets.QStackedWidget(self.MainWidget)
        self.ContentViewWidget.setGeometry(QtCore.QRect(270, 10, 841, 851))
        self.ContentViewWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.ContentViewWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ContentViewWidget.setLineWidth(1)
        self.ContentViewWidget.setMidLineWidth(0)
        self.ContentViewWidget.setObjectName("ContentViewWidget")

        # Hook Collection View Page #
        self.HookCollectionViewPage = HookCollectionViewPage()
        self.ContentViewWidget.addWidget(self.HookCollectionViewPage)

        # Hook View Page #
        self.HookViewPage = HookViewPage()
        self.ContentViewWidget.addWidget(self.HookViewPage)

        # Live Packet View Page #
        self.LivePacketViewPage = LivePacketViewPage()
        # Add Live packet View Page to Content View #
        self.ContentViewWidget.addWidget(self.LivePacketViewPage)

        # PCAP View Page #
        self.PCAPViewPage = PCAPViewPage()
        # Add PCAP view Page to Content View #
        self.ContentViewWidget.addWidget(self.PCAPViewPage)

        # Option View Frame #
        self.OptionViewFrame = OptionViewFrame(self.MainWidget)
        MainWindow.setCentralWidget(self.MainWidget)

        self.retranslateUi(MainWindow)
        self.ContentViewWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Network Trafic Proxy System"))