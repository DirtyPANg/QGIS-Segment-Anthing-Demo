from PyQt5 import QtWidgets, QtCore

import sys
class Ui_SegmentScreenDialogBase(object):
    def setupUi(self, SegmentScreenDialogBase):
        SegmentScreenDialogBase.setObjectName("SegmentScreenDialogBase")
        SegmentScreenDialogBase.resize(529, 337)
        self.gridLayout = QtWidgets.QGridLayout(SegmentScreenDialogBase)
        self.gridLayout.setObjectName("gridLayout")

        self.RunBottom = QtWidgets.QPushButton(SegmentScreenDialogBase)
        self.RunBottom.setObjectName("RunBottom")
        self.gridLayout.addWidget(self.RunBottom, 3, 3, 1, 1)

        self.label = QtWidgets.QLabel(SegmentScreenDialogBase)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)

        self.comboBox = QtWidgets.QComboBox(SegmentScreenDialogBase)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 2, 1, 1)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 3, 2)

        self.label_2 = QtWidgets.QLabel()
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.ram_gb = QtWidgets.QSpinBox()
        self.ram_gb.setMinimum(8)
        self.ram_gb.setSingleStep(4)
        self.ram_gb.setObjectName("ram_gb")
        self.verticalLayout.addWidget(self.ram_gb)

        self.label_3 = QtWidgets.QLabel()
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        self.feature_name = QtWidgets.QTextEdit()
        self.feature_name.setObjectName("feature_name")
        self.verticalLayout.addWidget(self.feature_name)

        QtCore.QMetaObject.connectSlotsByName(SegmentScreenDialogBase)
        
        self.retranslateUi(SegmentScreenDialogBase)

    def retranslateUi(self, SegmentScreenDialogBase):
        _translate = QtCore.QCoreApplication.translate
        SegmentScreenDialogBase.setWindowTitle(_translate("SegmentScreenDialogBase", "Segment Screen Dialog Base"))
        self.RunBottom.setText(_translate("SegmentScreenDialogBase", "Run"))
        self.label.setText(_translate("SegmentScreenDialogBase", "Label"))
        self.label_2.setText(_translate("SegmentScreenDialogBase", "Label 2"))
        self.label_3.setText(_translate("SegmentScreenDialogBase", "Label 3"))
        # add other widgets' text if needed...
