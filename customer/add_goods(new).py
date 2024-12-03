# -*- coding: utf-8 -*-

# This file is generated from the ui file 'ui/add_goods.ui'
# Created by PyQt5 UI code generator 5.13.2
# Warning! All changes made to this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_add_goods(object):
    def setupUi(self, add_goods):
        # Set the main window's name and size
        add_goods.setObjectName("add_goods")
        add_goods.resize(800, 600)

        # Create a central widget
        self.centralwidget = QtWidgets.QWidget(add_goods)
        self.centralwidget.setObjectName("centralwidget")

        # Create a form layout widget
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(180, 90, 391, 161))
        self.formLayoutWidget.setObjectName("formLayoutWidget")

        # Create a form layout
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        # Label for goods name
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)

        # Input field for goods name
        self.goods_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.goods_name.setFont(font)
        self.goods_name.setObjectName("goods_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.goods_name)

        # Label for goods type
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)

        # Combo box for selecting goods type
        self.goods_type = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.goods_type.setFont(font)
        self.goods_type.setObjectName("goods_type")
        # Adding options for goods type
        for _ in range(20):
            self.goods_type.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.goods_type)

        # Label for goods price
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)

        # Label for goods stock
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_9)

        # Input field for goods price (double)
        self.goods_prices = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.goods_prices.setFont(font)
        self.goods_prices.setMaximum(9999.99)  # Set maximum value
        self.goods_prices.setSingleStep(0.5)    # Set step value
        self.goods_prices.setObjectName("goods_prices")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.goods_prices)

        # Input field for goods stock (integer)
        self.goods_rest = QtWidgets.QSpinBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.goods_rest.setFont(font)
        self.goods_rest.setMaximum(9999)  # Set maximum value
        self.goods_rest.setObjectName("goods_rest")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.goods_rest)

        # Button to add goods
        self.add_bt = QtWidgets.QPushButton(self.centralwidget)
        self.add_bt.setGeometry(QtCore.QRect(290, 350, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.add_bt.setFont(font)
        self.add_bt.setObjectName("add_bt")

        # Command link button to return to the main page
        self.tomain = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.tomain.setGeometry(QtCore.QRect(480, 270, 91, 51))
        self.tomain.setObjectName("tomain")

        # Set the central widget
        add_goods.setCentralWidget(self.centralwidget)

        # Create a menu bar
        self.menubar = QtWidgets.QMenuBar(add_goods)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        add_goods.setMenuBar(self.menubar)

        # Create a status bar
        self.statusbar = QtWidgets.QStatusBar(add_goods)
        self.statusbar.setObjectName("statusbar")
        add_goods.setStatusBar(self.statusbar)

        # Call the translation method
        self.retranslateUi(add_goods)
        # Connect signals and slots
        QtCore.QMetaObject.connectSlotsByName(add_goods)

    def retranslateUi(self, add_goods):
        _translate = QtCore.QCoreApplication.translate
        # Set the window title
        add_goods.setWindowTitle(_translate("add_goods", "Add Goods"))
        # Set the text for labels and buttons
        self.label.setText(_translate("add_goods", "Goods Name"))
        self.label_7.setText(_translate("add_goods", "Goods Type"))
        self.goods_type.setItemText(0, _translate("add_goods", "Baby Products"))
        self.goods_type.setItemText(1, _translate("add_goods", "Digital Products"))
        self.goods_type.setItemText(2, _translate("add_goods", "Men's Clothing"))
        self.goods_type.setItemText(3, _translate("add_goods", "Fresh Produce"))
        self.goods_type.setItemText(4, _translate("add_goods", "Food"))
        self.goods_type.setItemText(5, _translate("add_goods", "Women's Clothing"))
        self.goods_type.setItemText(6, _translate("add_goods", "Footwear"))
        self.goods_type.setItemText(7, _translate("add_goods", "Accessories"))
        self.goods_type.setItemText(8, _translate("add_goods", "General Merchandise"))
        self.goods_type.setItemText(9, _translate("add_goods", "Mobile Phones"))
        self.goods_type.setItemText(10, _translate("add_goods", "Bags"))
        self.goods_type.setItemText(11, _translate("add_goods", "Home Improvement"))
        self.goods_type.setItemText(12, _translate("add_goods", "Underwear"))
        self.goods_type.setItemText(13, _translate("add_goods", "Beauty Products"))
        self.goods_type.setItemText(14, _translate("add_goods", "Corporate Products"))
        self.goods_type.setItemText(15, _translate("add_goods", "Sports"))
        self.goods_type.setItemText(16, _translate("add_goods", "Personal Care"))
        self.goods_type.setItemText(17, _translate("add_goods", "Appliances"))
        self.goods_type.setItemText(18, _translate("add_goods", "Car Products"))
        self.goods_type.setItemText(19, _translate("add_goods", "Health Products"))
        self.label_8.setText(_translate("add_goods", "Price"))
        self.label_9.setText(_translate("add_goods", "Stock"))
        self.add_bt.setText(_translate("add_goods", "Add"))
        self.tomain.setText(_translate("add_goods", "Home"))
