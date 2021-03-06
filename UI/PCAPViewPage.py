# Software Engineering II
# Dr.Salamah
# Team 6 - Byte Me

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget

class PCAPViewPage(QWidget):

    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.setObjectName("PCAPViewPage")
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
        # Filter Frame #
        self.FilterFrame = QtWidgets.QFrame(self)
        self.FilterFrame.setGeometry(QtCore.QRect(10, 140, 821, 71))
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
        self.FAAddButton = QtWidgets.QToolButton(self)
        self.FAAddButton.setGeometry(QtCore.QRect(470, 640, 27, 20))
        self.FAAddButton.setArrowType(QtCore.Qt.RightArrow)
        self.FAAddButton.setObjectName("FAAddButton")
        # Packet Area #
        self.PacketAreaFrame = QtWidgets.QFrame(self)
        self.PacketAreaFrame.setGeometry(QtCore.QRect(10, 220, 821, 311))
        self.PacketAreaFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.PacketAreaFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.PacketAreaFrame.setObjectName("PacketAreaFrame")
        self.PacketAreaLabel = QtWidgets.QLabel(self.PacketAreaFrame)
        self.PacketAreaLabel.setGeometry(QtCore.QRect(10, 10, 101, 21))
        self.PacketAreaLabel.setObjectName("PacketAreaLabel")
        # Packet Area Tabs #
        self.PacketAreaTabs = QtWidgets.QTabWidget(self.PacketAreaFrame)
        self.PacketAreaTabs.setGeometry(QtCore.QRect(10, 40, 721, 261))
        self.PacketAreaTabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.PacketAreaTabs.setObjectName("PacketAreaTabs")
        # Dissected packet Tab #
        self.DissectedTab = QtWidgets.QWidget()
        self.DissectedTab.setObjectName("DissectedTab")
        self.PacketAreaTabs.addTab(self.DissectedTab, "")
        self.DissectedPacketTree = QtWidgets.QTreeWidget(self.DissectedTab)
        self.DissectedPacketTree.setGeometry(QtCore.QRect(0, 0, 715, 275))
        self.DissectedPacketTree.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DissectedPacketTree.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.DissectedPacketTree.setHeaderHidden(True)
        self.DissectedPacketTree.setColumnCount(2)
        # Binary packet Tab #
        self.BinaryTab = QtWidgets.QWidget()
        self.BinaryTab.setObjectName("BinaryTab")
        self.PacketAreaTabs.addTab(self.BinaryTab, "")
        self.BinaryPacketEdit = QtWidgets.QPlainTextEdit(self.BinaryTab)
        self.BinaryPacketEdit.setGeometry(QtCore.QRect(0, 0, 715, 275))
        self.BinaryPacketEdit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BinaryPacketEdit.setFrameShadow(QtWidgets.QFrame.Sunken)
        # Hex packet Tab #
        self.HexTab = QtWidgets.QWidget()
        self.HexTab.setObjectName("HexTab")
        self.PacketAreaTabs.addTab(self.HexTab, "")
        self.HexPacketEdit = QtWidgets.QPlainTextEdit(self.HexTab)
        self.HexPacketEdit.setGeometry(QtCore.QRect(0, 0, 715, 275))
        self.HexPacketEdit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.HexPacketEdit.setFrameShadow(QtWidgets.QFrame.Sunken)
        # Packet clear Button #
        self.PacketAreaClearButton = QtWidgets.QPushButton(self.PacketAreaFrame)
        self.PacketAreaClearButton.setGeometry(QtCore.QRect(740, 270, 71, 25))
        self.PacketAreaClearButton.setObjectName("PacketAreaClearButton")
        self.FASubstractButton = QtWidgets.QToolButton(self)
        self.FASubstractButton.setGeometry(QtCore.QRect(470, 690, 27, 20))
        self.FASubstractButton.setArrowType(QtCore.Qt.LeftArrow)
        self.FASubstractButton.setObjectName("FASubstractButton")
        self.PCAPViewLabel = QtWidgets.QLabel(self)
        self.PCAPViewLabel.setGeometry(QtCore.QRect(0, 0, 841, 51))
        self.PCAPViewLabel.setStyleSheet("border-style: solid solid none solid;\n"
                                                 "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgb(111, 168, 220), stop:1 rgb(159, 197, 232));")
        self.PCAPViewLabel.setObjectName("PCAPViewLabel")
        self.PCAPFrame = QtWidgets.QFrame(self)
        self.PCAPFrame.setGeometry(QtCore.QRect(10, 60, 821, 71))
        self.PCAPFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.PCAPFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.PCAPFrame.setObjectName("PCAPFrame")
        self.PCAPPathLabel = QtWidgets.QLabel(self.PCAPFrame)
        self.PCAPPathLabel.setGeometry(QtCore.QRect(10, 10, 121, 21))
        self.PCAPPathLabel.setObjectName("PCAPPathLabel")
        self.PCAPPathLabel2 = QtWidgets.QLabel(self.PCAPFrame)
        self.PCAPPathLabel2.setGeometry(QtCore.QRect(10, 40, 61, 16))
        self.PCAPPathLabel2.setObjectName("PCAPPathLabel2")
        self.PCAPPathEdit = QtWidgets.QLineEdit(self.PCAPFrame)
        self.PCAPPathEdit.setGeometry(QtCore.QRect(80, 40, 571, 21))
        self.PCAPPathEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.PCAPPathEdit.setObjectName("PCAPPathEdit")
        self.PCAPOpenButton = QtWidgets.QPushButton(self.PCAPFrame)
        self.PCAPOpenButton.setGeometry(QtCore.QRect(660, 40, 71, 25))
        self.PCAPOpenButton.setObjectName("PCAPOpenButton")
        self.PCAPCancelButton = QtWidgets.QPushButton(self.PCAPFrame)
        self.PCAPCancelButton.setGeometry(QtCore.QRect(740, 40, 71, 25))
        self.PCAPCancelButton.setObjectName("PCAPCancelButton")
        self.PacketAreaTabs.setCurrentIndex(0)
        self.retranslatePage()

    def retranslatePage(self):
            _translate = QtCore.QCoreApplication.translate
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
            self.CaptureFiltreLabel.setText(_translate("MainWindow",
                                                         "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">Capture Filter</span></p></body></html>"))
            self.FilterLable.setText(_translate("MainWindow",
                                                  "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Filter</span></p></body></html>"))
            self.FilterExpressionEdit.setPlaceholderText(_translate("MainWindow", "Filter Expression"))
            self.ApplyExpressionButton.setText(_translate("MainWindow", "Apply"))
            self.ClearExpressionButton.setText(_translate("MainWindow", "Clear"))
            self.FieldAreaLabel.setText(_translate("MainWindow",
                                                     "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">Field Area</span></p></body></html>"))
            item = self.FieldAreaTable.horizontalHeaderItem(0)
            item.setText(_translate("MainWindow", "Field Name"))
            item = self.FieldAreaTable.horizontalHeaderItem(1)
            item.setText(_translate("MainWindow", "Value"))
            item = self.FieldAreaTable.horizontalHeaderItem(2)
            item.setText(_translate("MainWindow", "Mask"))
            item = self.FieldAreaTable.horizontalHeaderItem(3)
            item.setText(_translate("MainWindow", "Display Format"))
            self.FASaveButton.setText(_translate("MainWindow", "Save Modification"))
            self.FAForwardButton.setText(_translate("MainWindow", "Forward"))
            self.FADropButton.setText(_translate("MainWindow", "Drop"))
            self.FAAddButton.setText(_translate("MainWindow", "..."))
            self.PacketAreaLabel.setText(_translate("MainWindow",
                                                      "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">Packet Area</span></p></body></html>"))
            self.PacketAreaTabs.setTabText(self.PacketAreaTabs.indexOf(self.DissectedTab),
                                             _translate("MainWindow", "Dissected"))
            self.PacketAreaTabs.setTabText(self.PacketAreaTabs.indexOf(self.BinaryTab),
                                             _translate("MainWindow", "Binary"))
            self.PacketAreaTabs.setTabText(self.PacketAreaTabs.indexOf(self.HexTab),
                                             _translate("MainWindow", "HEX"))
            self.PacketAreaClearButton.setText(_translate("MainWindow", "Clear"))
            self.FASubstractButton.setText(_translate("MainWindow", "..."))
            self.PCAPViewLabel.setText(_translate("MainWindow",
                                                          "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Packet from PCAP View</span></p></body></html>"))
            self.PCAPPathLabel.setText(_translate("MainWindow",
                                                         "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">PCAP File</span></p><p><br/></p></body></html>"))
            self.PCAPPathLabel2.setText(_translate("MainWindow",
                                                  "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">PCAP File</span></p></body></html>"))
            self.PCAPPathEdit.setPlaceholderText(_translate("MainWindow", "PCAP File Path"))
            self.PCAPOpenButton.setText(_translate("MainWindow", "Open"))
            self.PCAPCancelButton.setText(_translate("MainWindow", "Cancel"))

    #def addDissectedPacket(self, Packet):
        # TO DO Complete #
