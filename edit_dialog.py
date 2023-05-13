# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(460, 391)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 461, 391))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)

        self.timeUntil = QDateTimeEdit(self.layoutWidget)
        self.timeUntil.setObjectName(u"timeUntil")

        self.gridLayout.addWidget(self.timeUntil, 7, 0, 1, 2)

        self.btnAdd = QPushButton(self.layoutWidget)
        self.btnAdd.setObjectName(u"btnAdd")

        self.gridLayout.addWidget(self.btnAdd, 12, 0, 1, 1)

        self.cmbType = QComboBox(self.layoutWidget)
        self.cmbType.setObjectName(u"cmbType")

        self.gridLayout.addWidget(self.cmbType, 3, 0, 1, 2)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 10, 0, 1, 1)

        self.cmbDeposit = QComboBox(self.layoutWidget)
        self.cmbDeposit.setObjectName(u"cmbDeposit")

        self.gridLayout.addWidget(self.cmbDeposit, 1, 0, 1, 2)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.btnCancel = QPushButton(self.layoutWidget)
        self.btnCancel.setObjectName(u"btnCancel")

        self.gridLayout.addWidget(self.btnCancel, 12, 1, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.txtInjured = QLineEdit(self.layoutWidget)
        self.txtInjured.setObjectName(u"txtInjured")

        self.gridLayout.addWidget(self.txtInjured, 9, 0, 1, 2)

        self.timeSince = QDateTimeEdit(self.layoutWidget)
        self.timeSince.setObjectName(u"timeSince")

        self.gridLayout.addWidget(self.timeSince, 5, 0, 1, 2)

        self.txtComment = QLineEdit(self.layoutWidget)
        self.txtComment.setObjectName(u"txtComment")

        self.gridLayout.addWidget(self.txtComment, 11, 0, 1, 2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041c\u0435\u0441\u0442\u043e\u0440\u043e\u0436\u0434\u0435\u043d\u0438\u0435", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043d\u0435\u0446 \u043f\u0440\u043e\u0438\u0441\u0448\u0435\u0441\u0442\u0432\u0438\u044f", None))
        self.btnAdd.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0422\u0438\u043f \u043f\u0440\u043e\u0438\u0441\u0448\u0435\u0441\u0442\u0432\u0438\u044f", None))
        self.btnCancel.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u0421\u0443\u043c\u043c\u0430 \u0443\u0449\u0435\u0440\u0431\u0430", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0447\u0430\u043b\u043e \u043f\u0440\u043e\u0438\u0441\u0448\u0435\u0441\u0442\u0432\u0438\u044f", None))
    # retranslateUi

