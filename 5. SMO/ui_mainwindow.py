# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(504, 366)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.label_op1 = QtWidgets.QLabel(Form)
        self.label_op1.setGeometry(QtCore.QRect(9, 103, 16, 16))
        self.label_op1.setObjectName("label_op1")
        self.label_op0 = QtWidgets.QLabel(Form)
        self.label_op0.setGeometry(QtCore.QRect(9, 75, 16, 16))
        self.label_op0.setObjectName("label_op0")
        self.label_comp_title = QtWidgets.QLabel(Form)
        self.label_comp_title.setGeometry(QtCore.QRect(17, 231, 147, 16))
        self.label_comp_title.setObjectName("label_comp_title")
        self.label_comp0 = QtWidgets.QLabel(Form)
        self.label_comp0.setGeometry(QtCore.QRect(17, 250, 16, 16))
        self.label_comp0.setObjectName("label_comp0")
        self.label_op2 = QtWidgets.QLabel(Form)
        self.label_op2.setGeometry(QtCore.QRect(9, 131, 16, 16))
        self.label_op2.setObjectName("label_op2")
        self.label_comp1 = QtWidgets.QLabel(Form)
        self.label_comp1.setGeometry(QtCore.QRect(17, 278, 16, 16))
        self.label_comp1.setObjectName("label_comp1")
        self.label_lost_clients_title = QtWidgets.QLabel(Form)
        self.label_lost_clients_title.setGeometry(QtCore.QRect(249, 291, 104, 16))
        self.label_lost_clients_title.setObjectName("label_lost_clients_title")
        self.label_clients_title = QtWidgets.QLabel(Form)
        self.label_clients_title.setGeometry(QtCore.QRect(9, 9, 131, 16))
        self.label_clients_title.setObjectName("label_clients_title")
        self.label_op_title = QtWidgets.QLabel(Form)
        self.label_op_title.setGeometry(QtCore.QRect(9, 56, 138, 16))
        self.label_op_title.setObjectName("label_op_title")
        self.pushButton_model = QtWidgets.QPushButton(Form)
        self.pushButton_model.setGeometry(QtCore.QRect(160, 340, 75, 23))
        self.pushButton_model.setObjectName("pushButton_model")
        self.le_lost_clients = QtWidgets.QLineEdit(Form)
        self.le_lost_clients.setGeometry(QtCore.QRect(360, 290, 133, 20))
        self.le_lost_clients.setReadOnly(True)
        self.le_lost_clients.setObjectName("le_lost_clients")
        self.le_op1_m = QtWidgets.QLineEdit(Form)
        self.le_op1_m.setGeometry(QtCore.QRect(23, 104, 125, 20))
        self.le_op1_m.setObjectName("le_op1_m")
        self.label_op1_pm = QtWidgets.QLabel(Form)
        self.label_op1_pm.setGeometry(QtCore.QRect(154, 104, 24, 16))
        self.label_op1_pm.setObjectName("label_op1_pm")
        self.le_op1_d = QtWidgets.QLineEdit(Form)
        self.le_op1_d.setGeometry(QtCore.QRect(184, 104, 125, 20))
        self.le_op1_d.setObjectName("le_op1_d")
        self.label_op2_pm = QtWidgets.QLabel(Form)
        self.label_op2_pm.setGeometry(QtCore.QRect(154, 132, 24, 16))
        self.label_op2_pm.setObjectName("label_op2_pm")
        self.le_op2_d = QtWidgets.QLineEdit(Form)
        self.le_op2_d.setGeometry(QtCore.QRect(184, 132, 125, 20))
        self.le_op2_d.setObjectName("le_op2_d")
        self.le_op2_m = QtWidgets.QLineEdit(Form)
        self.le_op2_m.setGeometry(QtCore.QRect(23, 132, 125, 20))
        self.le_op2_m.setObjectName("le_op2_m")
        self.label_client_pm = QtWidgets.QLabel(Form)
        self.label_client_pm.setGeometry(QtCore.QRect(154, 29, 24, 16))
        self.label_client_pm.setObjectName("label_client_pm")
        self.le_client_m = QtWidgets.QLineEdit(Form)
        self.le_client_m.setGeometry(QtCore.QRect(23, 29, 125, 20))
        self.le_client_m.setObjectName("le_client_m")
        self.le_client_d = QtWidgets.QLineEdit(Form)
        self.le_client_d.setGeometry(QtCore.QRect(184, 29, 125, 20))
        self.le_client_d.setObjectName("le_client_d")
        self.le_op0_m = QtWidgets.QLineEdit(Form)
        self.le_op0_m.setGeometry(QtCore.QRect(23, 76, 125, 20))
        self.le_op0_m.setObjectName("le_op0_m")
        self.label_op0_pm = QtWidgets.QLabel(Form)
        self.label_op0_pm.setGeometry(QtCore.QRect(154, 76, 24, 16))
        self.label_op0_pm.setObjectName("label_op0_pm")
        self.le_op0_d = QtWidgets.QLineEdit(Form)
        self.le_op0_d.setGeometry(QtCore.QRect(184, 76, 125, 20))
        self.le_op0_d.setObjectName("le_op0_d")
        self.label_client_count_title = QtWidgets.QLabel(Form)
        self.label_client_count_title.setGeometry(QtCore.QRect(260, 250, 115, 16))
        self.label_client_count_title.setObjectName("label_client_count_title")
        self.le_client_count = QtWidgets.QLineEdit(Form)
        self.le_client_count.setGeometry(QtCore.QRect(363, 252, 133, 20))
        self.le_client_count.setObjectName("le_client_count")
        self.le_comp0_m = QtWidgets.QLineEdit(Form)
        self.le_comp0_m.setGeometry(QtCore.QRect(31, 251, 133, 20))
        self.le_comp0_m.setObjectName("le_comp0_m")
        self.le_comp1_m = QtWidgets.QLineEdit(Form)
        self.le_comp1_m.setGeometry(QtCore.QRect(31, 279, 133, 20))
        self.le_comp1_m.setObjectName("le_comp1_m")
        self.lost = QtWidgets.QLineEdit(Form)
        self.lost.setGeometry(QtCore.QRect(363, 322, 133, 20))
        self.lost.setText("")
        self.lost.setObjectName("lost")
        self.label_client_count_title_2 = QtWidgets.QLabel(Form)
        self.label_client_count_title_2.setGeometry(QtCore.QRect(290, 320, 115, 16))
        self.label_client_count_title_2.setObjectName("label_client_count_title_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "лаб"))
        self.label_op1.setText(_translate("Form", "1"))
        self.label_op0.setText(_translate("Form", "0"))
        self.label_comp_title.setText(_translate("Form", "Компьютеры:"))
        self.label_comp0.setText(_translate("Form", "0"))
        self.label_op2.setText(_translate("Form", "2"))
        self.label_comp1.setText(_translate("Form", "1"))
        self.label_lost_clients_title.setText(_translate("Form", "Вероятность отказа"))
        self.label_clients_title.setText(_translate("Form", "Заявки:"))
        self.label_op_title.setText(_translate("Form", "Операторы:"))
        self.pushButton_model.setText(_translate("Form", "старт"))
        self.le_op1_m.setText(_translate("Form", "40"))
        self.label_op1_pm.setText(_translate("Form", "delta"))
        self.le_op1_d.setText(_translate("Form", "10"))
        self.label_op2_pm.setText(_translate("Form", "delta"))
        self.le_op2_d.setText(_translate("Form", "20"))
        self.le_op2_m.setText(_translate("Form", "40"))
        self.label_client_pm.setText(_translate("Form", "delta"))
        self.le_client_m.setText(_translate("Form", "10"))
        self.le_client_d.setText(_translate("Form", "2"))
        self.le_op0_m.setText(_translate("Form", "20"))
        self.label_op0_pm.setText(_translate("Form", "delta"))
        self.le_op0_d.setText(_translate("Form", "5"))
        self.label_client_count_title.setText(_translate("Form", "Всего заявок"))
        self.le_client_count.setText(_translate("Form", "300"))
        self.le_comp0_m.setText(_translate("Form", "15"))
        self.le_comp1_m.setText(_translate("Form", "30"))
        self.label_client_count_title_2.setText(_translate("Form", "Пропущено"))

