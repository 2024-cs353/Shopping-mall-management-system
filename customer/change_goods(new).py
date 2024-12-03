# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/change_goods.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_change_goods(object):
    def setupUi(self, change_goods):
        # Set the object name for the main window
        change_goods.setObjectName("change_goods")
        # Resize the main window
        change_goods.resize(800, 600)
        # Create a central widget
        self.centralwidget = QtWidgets.QWidget(change_goods)
        self.centralwidget.setObjectName("centralwidget")
        
        # Create a button to update goods
        self.toupdate = QtWidgets.QPushButton(self.centralwidget)
        self.toupdate.setGeometry(QtCore.QRect(220, 310, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.toupdate.setFont(font)
        self.toupdate.setObjectName("toupdate")
        
        # Create a button to delete goods
        self.delete_bt = QtWidgets.QPushButton(self.centralwidget)
        self.delete_bt.setGeometry(QtCore.QRect(450, 310, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.delete_bt.setFont(font)
        self.delete_bt.setObjectName("delete_bt")
        
        # Create a command link button to return to the main page
        self.tomain = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.tomain.setGeometry(QtCore.QRect(520, 180, 91, 51))
        self.tomain.setObjectName("tomain")
        
        # Create a widget for form layout
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(220, 130, 391, 41))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        
        # Create a form layout
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        
        # Create a label for goods name
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        
        # Create a combo box for selecting goods name
        self.goods_name = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.goods_name.setFont(font)
        self.goods_name.setObjectName("goods_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.goods_name)
        
        # Set the central widget for the main window
        change_goods.setCentralWidget(self.centralwidget)
        
        # Create a menu bar
        self.menubar = QtWidgets.QMenuBar(change_goods)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        change_goods.setMenuBar(self.menubar)
        
        # Create a status bar
        self.statusbar = QtWidgets.QStatusBar(change_goods)
        self.statusbar.setObjectName("statusbar")
        change_goods.setStatusBar(self.statusbar)

        # Call the method to set text for UI elements
        self.retranslateUi(change_goods)
        # Connect slots for the main window
        QtCore.QMetaObject.connectSlotsByName(change_goods)

    def retranslateUi(self, change_goods):
        _translate = QtCore.QCoreApplication.translate
        # Set the window title
        change_goods.setWindowTitle(_translate("change_goods", "修改商品"))
        # Set the text for the update button
        self.toupdate.setText(_translate("change_goods", "修改商品"))
        # Set the text for the delete button
        self.delete_bt.setText(_translate("change_goods", "删除商品"))
        # Set the text for the main page button
        self.tomain.setText(_translate("change_goods", "首页"))
        # Set the text for the goods name label
        self.label.setText(_translate("change_goods", "商品名称"))
