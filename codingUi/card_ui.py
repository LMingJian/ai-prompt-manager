# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'card.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QWidget)

class Ui_WordCard(object):
    def setupUi(self, WordCard):
        if not WordCard.objectName():
            WordCard.setObjectName(u"WordCard")
        WordCard.resize(120, 39)
        WordCard.setMinimumSize(QSize(0, 39))
        WordCard.setMaximumSize(QSize(16777215, 39))
        WordCard.setStyleSheet(u"QLabel {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,\n"
"                      stop: 0 #ffffff, stop: 1 #f0f9ff);\n"
"    border: 1px solid #000000;\n"
"}\n"
"QLabel:hover {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,\n"
"                      stop: 0 #f8f9fa, stop: 1 #e6f7ff);\n"
"    border: 2px solid #000000;\n"
"}")
        WordCard.setFrameShape(QFrame.Shape.StyledPanel)
        WordCard.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(WordCard)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.word_label = QLabel(WordCard)
        self.word_label.setObjectName(u"word_label")
        font = QFont()
        font.setBold(True)
        self.word_label.setFont(font)
        self.word_label.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.word_label.setScaledContents(True)
        self.word_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.word_label.setMargin(10)

        self.horizontalLayout.addWidget(self.word_label)


        self.retranslateUi(WordCard)

        QMetaObject.connectSlotsByName(WordCard)
    # setupUi

    def retranslateUi(self, WordCard):
        self.word_label.setText(QCoreApplication.translate("WordCard", u"Word | \u5355\u8bcd", None))
        pass
    # retranslateUi

