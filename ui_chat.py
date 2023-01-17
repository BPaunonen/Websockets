# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_chat.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(665, 533)
        self.listWidget = QListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(90, 70, 481, 341))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 40, 121, 31))
        font = QFont()
        font.setFamilies([u"Helvetica"])
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.button_SEND = QPushButton(Form)
        self.button_SEND.setObjectName(u"button_SEND")
        self.button_SEND.setGeometry(QRect(220, 460, 113, 32))
        self.button_QUIT = QPushButton(Form)
        self.button_QUIT.setObjectName(u"button_QUIT")
        self.button_QUIT.setGeometry(QRect(330, 460, 113, 32))
        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(90, 420, 481, 31))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"PyQT Chat", None))
        self.button_SEND.setText(QCoreApplication.translate("Form", u"Send", None))
        self.button_QUIT.setText(QCoreApplication.translate("Form", u"Quit", None))
    # retranslateUi

