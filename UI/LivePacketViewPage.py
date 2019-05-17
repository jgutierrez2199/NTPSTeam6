# Software Engineering II
# Dr.Salamah
# Team 6 - Byte Me

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget

class LivePacketViewPage(QWidget):

    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.setObjectName("LivePacketViewPage")
        self.LivePacketViewLable = QtWidgets.QLabel(self)
        self.LivePacketViewLable.setGeometry(QtCore.QRect(0, 0, 841, 51))
        self.LivePacketViewLable.setStyleSheet("border-style: solid solid none solid;\n"
                                               "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgb(111, 168, 220), stop:1 rgb(159, 197, 232));")
        self.LivePacketViewLable.setObjectName("LivePacketViewLable")
        # Proxy enable/disable box #
        self.ProxyBox = QtWidgets.QComboBox(self)
        self.ProxyBox.setGeometry(QtCore.QRect(140, 60, 91, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ProxyBox.setFont(font)
        self.ProxyBox.setFrame(True)
        self.ProxyBox.setObjectName("ProxyBox")
        self.ProxyBox.addItem("Disable")
        self.ProxyBox.addItem("Enable")
        self.ProxyBehaviorLabel = QtWidgets.QLabel(self)
        self.ProxyBehaviorLabel.setGeometry(QtCore.QRect(10, 60, 121, 16))
        self.ProxyBehaviorLabel.setObjectName("ProxyBehaviorLabel")
        self.IntercepBehaviorLabel = QtWidgets.QLabel(self)
        self.IntercepBehaviorLabel.setGeometry(QtCore.QRect(260, 60, 171, 16))
        self.IntercepBehaviorLabel.setObjectName("IntercepBehaviorLabel")
        # Interception enable/disable box #
        self.InterceptBox = QtWidgets.QComboBox(self)
        self.InterceptBox.setGeometry(QtCore.QRect(440, 60, 91, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.InterceptBox.setFont(font)
        self.InterceptBox.setFrame(True)
        self.InterceptBox.setObjectName("InterceptBox")
        self.InterceptBox.addItem("Disable")
        self.InterceptBox.addItem("Enable")
        self.QueueSizeLabel = QtWidgets.QLabel(self)
        self.QueueSizeLabel.setGeometry(QtCore.QRect(620, 60, 91, 16))
        self.QueueSizeLabel.setObjectName("QueueSizeLabel")
        # Queue size Edit #
        self.QueueSizeEdit = QtWidgets.QLineEdit(self)
        self.QueueSizeEdit.setGeometry(QtCore.QRect(720, 60, 113, 20))
        self.QueueSizeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.QueueSizeEdit.setObjectName("QueueSizeEdit")
        # Filter Frame #
        self.FilterFrame = QtWidgets.QFrame(self)
        self.FilterFrame.setGeometry(QtCore.QRect(10, 90, 821, 80))
        self.FilterFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.FilterFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.FilterFrame.setObjectName("FilterFrame")
        self.CaptureFiltreLabel = QtWidgets.QLabel(self.FilterFrame)
        self.CaptureFiltreLabel.setGeometry(QtCore.QRect(10, 10, 121, 21))
        self.CaptureFiltreLabel.setObjectName("CaptureFiltreLabel")
        self.FilterLable = QtWidgets.QLabel(self.FilterFrame)
        self.FilterLable.setGeometry(QtCore.QRect(20, 40, 54, 14))
        self.FilterLable.setObjectName("FilterLable")
        # Filter Expression edit box #
        self.FilterExpressionEdit = QtWidgets.QLineEdit(self.FilterFrame)
        self.FilterExpressionEdit.setGeometry(QtCore.QRect(80, 40, 571, 21))
        self.FilterExpressionEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.FilterExpressionEdit.setObjectName("FilterExpressionEdit")
        # Apply Filter Button #
        self.ApplyExpressionButton = QtWidgets.QPushButton(self.FilterFrame)
        self.ApplyExpressionButton.setGeometry(QtCore.QRect(660, 40, 71, 25))
        self.ApplyExpressionButton.setObjectName("ApplyExpressionButton")
        # Clear Expression Button #
        self.ClearExpressionButton = QtWidgets.QPushButton(self.FilterFrame)
        self.ClearExpressionButton.setGeometry(QtCore.QRect(740, 40, 71, 25))
        self.ClearExpressionButton.setObjectName("ClearExpressionButton")
        # Packet Area #
        self.PacketAreaFrame = QtWidgets.QFrame(self)
        self.PacketAreaFrame.setGeometry(QtCore.QRect(10, 180, 821, 351))
        self.PacketAreaFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.PacketAreaFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.PacketAreaFrame.setObjectName("PacketAreaFrame")
        self.PacketAreaLabel = QtWidgets.QLabel(self.PacketAreaFrame)
        self.PacketAreaLabel.setGeometry(QtCore.QRect(10, 10, 101, 21))
        self.PacketAreaLabel.setObjectName("PacketAreaLabel")
        # Packet Area Tabs #
        self.PacketAreaTabs = QtWidgets.QTabWidget(self.PacketAreaFrame)
        self.PacketAreaTabs.setGeometry(QtCore.QRect(10, 40, 721, 301))
        self.PacketAreaTabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.PacketAreaTabs.setObjectName("PacketAreaTabs")
        # Dissected packet tab #
        self.DissectedTab = QtWidgets.QWidget()
        self.DissectedTab.setObjectName("DissectedTab")
        self.PacketAreaTabs.addTab(self.DissectedTab, "")
        self.DissectedPacketTree =QtWidgets.QTreeWidget(self.DissectedTab)
        self.DissectedPacketTree.setGeometry(QtCore.QRect(0, 0, 715, 275))
        self.DissectedPacketTree.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DissectedPacketTree.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.DissectedPacketTree.setHeaderHidden(True)
        self.DissectedPacketTree.setColumnCount(2)
        # Binary packet tab #
        self.BinaryTab = QtWidgets.QWidget()
        self.BinaryTab.setObjectName("BinaryTab")
        self.PacketAreaTabs.addTab(self.BinaryTab, "")
        self.BinaryPacketEdit = QtWidgets.QPlainTextEdit(self.BinaryTab)
        self.BinaryPacketEdit.setGeometry(QtCore.QRect(0, 0, 715, 275))
        self.BinaryPacketEdit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BinaryPacketEdit.setFrameShadow(QtWidgets.QFrame.Sunken)
        # Hex packet tab #
        self.HexTab = QtWidgets.QWidget()
        self.HexTab.setObjectName("HexTab")
        self.PacketAreaTabs.addTab(self.HexTab, "")
        self.HexPacketEdit = QtWidgets.QPlainTextEdit(self.HexTab)
        self.HexPacketEdit.setGeometry(QtCore.QRect(0, 0, 715, 275))
        self.HexPacketEdit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.HexPacketEdit.setFrameShadow(QtWidgets.QFrame.Sunken)
        # Packet clear Button #
        self.PacketAreaClearButton = QtWidgets.QPushButton(self.PacketAreaFrame)
        self.PacketAreaClearButton.setGeometry(QtCore.QRect(740, 310, 71, 25))
        self.PacketAreaClearButton.setObjectName("PacketAreaClearButton")
        # Field Area #
        self.FieldAreaFrame = QtWidgets.QFrame(self)
        self.FieldAreaFrame.setGeometry(QtCore.QRect(10, 540, 451, 301))
        self.FieldAreaFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.FieldAreaFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.FieldAreaFrame.setObjectName("FieldAreaFrame")
        self.FieldAreaLabel = QtWidgets.QLabel(self.FieldAreaFrame)
        self.FieldAreaLabel.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.FieldAreaLabel.setObjectName("FieldAreaLabel")
        # Field table #
        self.FieldAreaTable = QtWidgets.QTableWidget(self.FieldAreaFrame)
        self.FieldAreaTable.setGeometry(QtCore.QRect(10, 40, 431, 211))
        self.FieldAreaTable.setShowGrid(False)
        self.FieldAreaTable.setObjectName("FieldAreaTable")
        self.FieldAreaTable.setColumnCount(4)
        header_labels = ['Field Name', 'Value', 'Mask', 'Display Format']
        self.FieldAreaTable.setHorizontalHeaderLabels(header_labels)
        self.FieldAreaTable.horizontalHeader().setStretchLastSection(True)
        self.FieldAreaTable.verticalHeader().setVisible(False)
        self.FieldAreaTable.verticalHeader().setStretchLastSection(False)
        self.FASaveButton = QtWidgets.QPushButton(self.FieldAreaFrame)
        self.FASaveButton.setGeometry(QtCore.QRect(170, 270, 111, 25))
        self.FASaveButton.setObjectName("FASaveButton")
        self.FAForwardButton = QtWidgets.QPushButton(self.FieldAreaFrame)
        self.FAForwardButton.setGeometry(QtCore.QRect(290, 270, 71, 25))
        self.FAForwardButton.setObjectName("FAForwardButton")
        self.FADropButton = QtWidgets.QPushButton(self.FieldAreaFrame)
        self.FADropButton.setGeometry(QtCore.QRect(370, 270, 71, 25))
        self.FADropButton.setObjectName("FADropButton")
        # Fuzzing Area Frame #
        self.FuzzingAreaFrame = QtWidgets.QFrame(self)
        self.FuzzingAreaFrame.setGeometry(QtCore.QRect(500, 540, 331, 301))
        self.FuzzingAreaFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.FuzzingAreaFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.FuzzingAreaFrame.setObjectName("FuzzingAreaFrame")
        self.FuzzingAreaLabel = QtWidgets.QLabel(self.FuzzingAreaFrame)
        self.FuzzingAreaLabel.setGeometry(QtCore.QRect(10, 10, 101, 21))
        self.FuzzingAreaLabel.setObjectName("FuzzingAreaLabel")
        self.FAPacketNameLabel = QtWidgets.QLabel(self.FuzzingAreaFrame)
        self.FAPacketNameLabel.setGeometry(QtCore.QRect(10, 40, 141, 20))
        self.FAPacketNameLabel.setTextFormat(QtCore.Qt.AutoText)
        self.FAPacketNameLabel.setWordWrap(False)
        self.FAPacketNameLabel.setObjectName("FAPacketNameLabel")
        self.FAPacketNameEdit = QtWidgets.QLineEdit(self.FuzzingAreaFrame)
        self.FAPacketNameEdit.setGeometry(QtCore.QRect(150, 40, 171, 20))
        self.FAPacketNameEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.FAPacketNameEdit.setObjectName("FAPacketNameEdit")
        self.FAFieldNameLabel = QtWidgets.QLabel(self.FuzzingAreaFrame)
        self.FAFieldNameLabel.setGeometry(QtCore.QRect(10, 80, 121, 20))
        self.FAFieldNameLabel.setTextFormat(QtCore.Qt.AutoText)
        self.FAFieldNameLabel.setWordWrap(False)
        self.FAFieldNameLabel.setObjectName("FAFieldNameLabel")
        self.FAFieldNameEdit = QtWidgets.QLineEdit(self.FuzzingAreaFrame)
        self.FAFieldNameEdit.setGeometry(QtCore.QRect(150, 80, 171, 20))
        self.FAFieldNameEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.FAFieldNameEdit.setObjectName("FAFieldNameEdit")
        self.FAReturnTypeLabel = QtWidgets.QLabel(self.FuzzingAreaFrame)
        self.FAReturnTypeLabel.setGeometry(QtCore.QRect(10, 120, 141, 20))
        self.FAReturnTypeLabel.setTextFormat(QtCore.Qt.AutoText)
        self.FAReturnTypeLabel.setWordWrap(False)
        self.FAReturnTypeLabel.setObjectName("FAReturnTypeLabel")
        self.FAReturnTypeEdit = QtWidgets.QLineEdit(self.FuzzingAreaFrame)
        self.FAReturnTypeEdit.setGeometry(QtCore.QRect(150, 120, 171, 20))
        self.FAReturnTypeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.FAReturnTypeEdit.setObjectName("FAReturnTypeEdit")
        self.FAMinimumLabel = QtWidgets.QLabel(self.FuzzingAreaFrame)
        self.FAMinimumLabel.setGeometry(QtCore.QRect(80, 160, 61, 20))
        self.FAMinimumLabel.setTextFormat(QtCore.Qt.AutoText)
        self.FAMinimumLabel.setWordWrap(False)
        self.FAMinimumLabel.setObjectName("FAMinimumLabel")
        self.FAMinimumEdit = QtWidgets.QLineEdit(self.FuzzingAreaFrame)
        self.FAMinimumEdit.setGeometry(QtCore.QRect(150, 160, 171, 20))
        self.FAMinimumEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.FAMinimumEdit.setObjectName("FAMinimumEdit")
        self.FAMaximumLabel = QtWidgets.QLabel(self.FuzzingAreaFrame)
        self.FAMaximumLabel.setGeometry(QtCore.QRect(80, 200, 61, 20))
        self.FAMaximumLabel.setTextFormat(QtCore.Qt.AutoText)
        self.FAMaximumLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.FAMaximumLabel.setWordWrap(False)
        self.FAMaximumLabel.setObjectName("FAMaximumLabel")
        self.FAMaximumEdit = QtWidgets.QLineEdit(self.FuzzingAreaFrame)
        self.FAMaximumEdit.setGeometry(QtCore.QRect(150, 200, 171, 20))
        self.FAMaximumEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.FAMaximumEdit.setObjectName("FAMaximumEdit")
        self.FAStopButton = QtWidgets.QPushButton(self.FuzzingAreaFrame)
        self.FAStopButton.setGeometry(QtCore.QRect(250, 270, 71, 25))
        self.FAStopButton.setObjectName("FAStopButton")
        self.FAFuzzButton = QtWidgets.QPushButton(self.FuzzingAreaFrame)
        self.FAFuzzButton.setGeometry(QtCore.QRect(170, 270, 71, 25))
        self.FAFuzzButton.setObjectName("FAFuzzButton")
        self.FAAddButton = QtWidgets.QToolButton(self)
        self.FAAddButton.setGeometry(QtCore.QRect(470, 640, 27, 20))
        self.FAAddButton.setArrowType(QtCore.Qt.RightArrow)
        self.FAAddButton.setObjectName("FAAddButton")
        self.FASubstractButton = QtWidgets.QToolButton(self)
        self.FASubstractButton.setGeometry(QtCore.QRect(470, 690, 27, 20))
        self.FASubstractButton.setArrowType(QtCore.Qt.LeftArrow)
        self.FASubstractButton.setObjectName("FASubstractButton")
        self.PacketAreaTabs.setCurrentIndex(0)
        self.retranslatePage()

    def retranslatePage(self):
            _translate = QtCore.QCoreApplication.translate
            self.LivePacketViewLable.setText(_translate("MainWindow",
                                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Live Packet View</span></p></body></html>"))
            self.ProxyBox.setItemText(0, _translate("MainWindow", "Disabled"))
            self.ProxyBox.setItemText(1, _translate("MainWindow", "Enabled"))
            self.ProxyBehaviorLabel.setText(_translate("MainWindow",
                                                       "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Proxy Behavior</span></p></body></html>"))
            self.IntercepBehaviorLabel.setText(_translate("MainWindow",
                                                          "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Interception Behavior</span></p></body></html>"))
            self.InterceptBox.setItemText(0, _translate("MainWindow", "Disabled"))
            self.InterceptBox.setItemText(1, _translate("MainWindow", "Enabled"))
            self.QueueSizeLabel.setText(_translate("MainWindow",
                                                   "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Queue Size</span></p></body></html>"))
            self.QueueSizeEdit.setPlaceholderText(_translate("MainWindow", "Queue Size"))
            self.CaptureFiltreLabel.setText(_translate("MainWindow",
                                                       "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">Capture Filter</span></p></body></html>"))
            self.FilterLable.setText(_translate("MainWindow",
                                                "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Filter</span></p></body></html>"))
            self.FilterExpressionEdit.setPlaceholderText(_translate("MainWindow", "Filter Expression"))
            self.ApplyExpressionButton.setText(_translate("MainWindow", "Apply"))
            self.ClearExpressionButton.setText(_translate("MainWindow", "Clear"))
            self.PacketAreaLabel.setText(_translate("MainWindow",
                                                    "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">Packet Area</span></p></body></html>"))
            self.PacketAreaTabs.setTabText(self.PacketAreaTabs.indexOf(self.DissectedTab),
                                           _translate("MainWindow", "Dissected"))
            self.PacketAreaTabs.setTabText(self.PacketAreaTabs.indexOf(self.BinaryTab),
                                           _translate("MainWindow", "Binary"))
            self.PacketAreaTabs.setTabText(self.PacketAreaTabs.indexOf(self.HexTab), _translate("MainWindow", "HEX"))
            self.PacketAreaClearButton.setText(_translate("MainWindow", "Clear"))
            self.FieldAreaLabel.setText(_translate("MainWindow",
                                                   "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">Field Area</span></p></body></html>"))
            self.FASaveButton.setText(_translate("MainWindow", "Save Modification"))
            self.FAForwardButton.setText(_translate("MainWindow", "Forward"))
            self.FADropButton.setText(_translate("MainWindow", "Drop"))
            self.FuzzingAreaLabel.setText(_translate("MainWindow",
                                                     "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">Fuzzing Area</span></p></body></html>"))
            self.FAPacketNameLabel.setText(_translate("MainWindow",
                                                      "<html><head/><body><p><span style=\" font-weight:600;\">Selected Packet Name</span></p></body></html>"))
            self.FAPacketNameEdit.setPlaceholderText(_translate("MainWindow", "Selected Packet Name"))
            self.FAFieldNameLabel.setText(_translate("MainWindow",
                                                     "<html><head/><body><p><span style=\" font-weight:600;\">Selected Field Name</span></p></body></html>"))
            self.FAFieldNameEdit.setPlaceholderText(_translate("MainWindow", "Selected Field Name"))
            self.FAReturnTypeLabel.setText(_translate("MainWindow",
                                                      "<html><head/><body><p><span style=\" font-weight:600;\">Expected Retrun Type</span></p></body></html>"))
            self.FAReturnTypeEdit.setPlaceholderText(_translate("MainWindow", "Return Type"))
            self.FAMinimumLabel.setText(_translate("MainWindow",
                                                   "<html><head/><body><p><span style=\" font-weight:600;\">Minimum</span></p></body></html>"))
            self.FAMinimumEdit.setPlaceholderText(_translate("MainWindow", "Minimum"))
            self.FAMaximumLabel.setText(_translate("MainWindow",
                                                   "<html><head/><body><p><span style=\" font-weight:600;\">Maximum</span></p></body></html>"))
            self.FAMaximumEdit.setPlaceholderText(_translate("MainWindow", "Maximum"))
            self.FAStopButton.setText(_translate("MainWindow", "Stop"))
            self.FAFuzzButton.setText(_translate("MainWindow", "Fuzz"))
            self.FAAddButton.setText(_translate("MainWindow", "..."))
            self.FASubstractButton.setText(_translate("MainWindow", "..."))

    #def addDissectedPacket(self, Packet):
        # TO DO Complete #
