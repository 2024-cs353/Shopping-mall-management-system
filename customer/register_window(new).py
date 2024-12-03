# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_register_window(object):
    def setupUi(self, register_window):
        # Set the object name for the main window
        register_window.setObjectName("register_window")
        # Resize the main window
        register_window.resize(850, 658)
        # Create a central widget for the main window
        self.centralwidget = QtWidgets.QWidget(register_window)
        self.centralwidget.setObjectName("centralwidget")
        
        # Create a registration button
        self.reg_bt = QtWidgets.QPushButton(self.centralwidget)
        self.reg_bt.setGeometry(QtCore.QRect(310, 450, 161, 61))  # Set position and size
        font = QtGui.QFont()
        font.setPointSize(16)  # Set font size
        self.reg_bt.setFont(font)
        self.reg_bt.setObjectName("reg_bt")
        
        # Create a command link button to navigate to login
        self.tologin = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.tologin.setGeometry(QtCore.QRect(510, 380, 91, 51))  # Set position and size
        self.tologin.setObjectName("tologin")
        
        # Create a widget for the form layout
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(209, 110, 391, 251))  # Set position and size
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        
        # Create a form layout
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)  # Set margins
        self.formLayout.setObjectName("formLayout")
        
        # Create a label for username
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)  # Set font size
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        
        # Create a line edit for username input
        self.username = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)  # Set font size
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.username)
        
        # Create a label for password
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)  # Set font size
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        
        # Create a line edit for password input
        self.pass1 = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)  # Set font size
        self.pass1.setFont(font)
        self.pass1.setEchoMode(QtWidgets.QLineEdit.Password)  # Set to password mode
        self.pass1.setObjectName("pass1")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pass1)
        
        # Create a label for confirming password
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)  # Set font size
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        
        # Create a line edit for confirming password
        self.pass2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)  # Set font size
        self.pass2.setFont(font)
        self.pass2.setEchoMode(QtWidgets.QLineEdit.Password)  # Set to password mode
        self.pass2.setObjectName("pass2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pass2)
        
        # Create a label for shop name
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)  # Set font size
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_9)
        
        # Create a line edit for shop name input
        self.shop_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)  # Set font size
        self.shop_name.setFont(font)
        self.shop_name.setObjectName("shop_name")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.shop_name)
        
        # Create a label for phone number
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)  # Set font size
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_10)
        
        # Create a line edit for phone number input
        self.phone = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)  # Set font size
        self.phone.setFont(font)
        self.phone.setObjectName("phone")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.phone)
        
        # Create a label for address
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)  # Set font size
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_11)
        
        # Create a combo box for address selection
        self.addr = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)  # Set font size
        self.addr.setFont(font)
        self.addr.setObjectName("addr")
        # Add items to the combo box
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.addr.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.addr)
        
        # Set the central widget for the main window
        register_window.setCentralWidget(self.centralwidget)
        
        # Create a menu bar for the main window
        self.menubar = QtWidgets.QMenuBar(register_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 26))  # Set position and size
        self.menubar.setObjectName("menubar")
        register_window.setMenuBar(self.menubar)
        
        # Create a status bar for the main window
        self.statusbar = QtWidgets.QStatusBar(register_window)
        self.statusbar.setObjectName("statusbar")
        register_window.setStatusBar(self.statusbar)

        # Call the function to set text for the UI elements
        self.retranslateUi(register_window)
        # Connect slots for the main window
        QtCore.QMetaObject.connectSlotsByName(register_window)

    def retranslateUi(self, register_window):
        _translate = QtCore.QCoreApplication.translate
        # Set the window title
        register_window.setWindowTitle(_translate("register_window", "购物商城商家端"))
        # Set text for buttons and labels
        self.reg_bt.setText(_translate("register_window", "注册"))
        self.tologin.setText(_translate("register_window", "登录"))
        self.label.setText(_translate("register_window", "用户名"))
        self.label_7.setText(_translate("register_window", "密码"))
        self.label_8.setText(_translate("register_window", "确认密码"))
        self.label_9.setText(_translate("register_window", "店铺名"))
        self.label_10.setText(_translate("register_window", "服务电话"))
        self.label_11.setText(_translate("register_window", "所在地"))
        
        # Set items for the address combo box
        self.addr.setItemText(0, _translate("register_window", "北京市"))
        self.addr.setItemText(1, _translate("register_window", "天津市"))
        self.addr.setItemText(2, _translate("register_window", "上海市"))
        self.addr.setItemText(3, _translate("register_window", "重庆市"))
        self.addr.setItemText(4, _translate("register_window", "河北省"))
        self.addr.setItemText(5, _translate("register_window", "山西省"))
        self.addr.setItemText(6, _translate("register_window", "辽宁省"))
        self.addr.setItemText(7, _translate("register_window", "吉林省"))
        self.addr.setItemText(8, _translate("register_window", "黑龙江省"))
        self.addr.setItemText(9, _translate("register_window", "江苏省"))
        self.addr.setItemText(10, _translate("register_window", "浙江省"))
        self.addr.setItemText(11, _translate("register_window", "安徽省"))
        self.addr.setItemText(12, _translate("register_window", "福建省"))
        self.addr.setItemText(13, _translate("register_window", "江西省"))
        self.addr.setItemText(14, _translate("register_window", "山东省"))
        self.addr.setItemText(15, _translate("register_window", "河南省"))
        self.addr.setItemText(16, _translate("register_window", "湖北省"))
        self.addr.setItemText(17, _translate("register_window", "湖南省"))
        self.addr.setItemText(18, _translate("register_window", "广东省"))
        self.addr.setItemText(19, _translate("register_window", "海南省"))
        self.addr.setItemText(20, _translate("register_window", "四川省"))
        self.addr.setItemText(21, _translate("register_window", "贵州省"))
        self.addr.setItemText(22, _translate("register_window", "云南省"))
        self.addr.setItemText(23, _translate("register_window", "陕西省"))
        self.addr.setItemText(24, _translate("register_window", "甘肃省"))
        self.addr.setItemText(25, _translate("register_window", "青海省"))
        self.addr.setItemText(26, _translate("register_window", "台湾省"))
        self.addr.setItemText(27, _translate("register_window", "内蒙古自治区"))
        self.addr.setItemText(28, _translate("register_window", "广西壮族自治区"))
        self.addr.setItemText(29, _translate("register_window", "西藏自治区"))
        self.addr.setItemText(30, _translate("register_window", "宁夏回族自治区"))
        self.addr.setItemText(31, _translate("register_window", "新疆维吾尔自治区"))
        self.addr.setItemText(32, _translate("register_window", "香港特别行政区"))
        self.addr.setItemText(33, _translate("register_window", "澳门特别行政区"))
