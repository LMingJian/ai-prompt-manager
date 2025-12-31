# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)
from codingQrc import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 768)
        icon = QIcon()
        icon.addFile(u":/logos/resources/bookshelf.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"background-color: #f5f7fa;\n"
"}\n"
"QPushButton {\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #3498db, stop: 1 #2980b9);\n"
"color: white;\n"
"border: none;\n"
"border-radius: 8px;\n"
"padding: 10px 20px;\n"
"font-weight: bold;\n"
"font-size: 12px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #3ca0db, stop: 1 #2c8bc9);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #2980b9, stop: 1 #2573a7);\n"
"}\n"
"QLineEdit {\n"
"padding: 10px;\n"
"border: 2px solid #ddd;\n"
"border-radius: 8px;\n"
"font-size: 12px;\n"
"}\n"
"QLineEdit:focus {\n"
"border-color: #3498db;\n"
"}\n"
"QLabel {\n"
"color: #2c3e50;\n"
"font-weight: bold;\n"
"}\n"
"QCheckBox {\n"
"    spacing: 10px;\n"
"    color: #2c3e50;\n"
"    font-size: 12px;\n"
"    font-weight: 600;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20p"
                        "x;\n"
"    border: 2px solid #bdc3c7;\n"
"    border-radius: 5px;\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"    border-color: #3498db;\n"
"    background-color: #f8f9fa;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3498db, stop: 1 #2980b9);\n"
"    border-color: #2980b9;\n"
"    image: url(:/icons/resources/check.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #3ca0db, stop: 1 #2c8bc9);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #2980b9, stop: 1 #2573a7);\n"
"}\n"
"\n"
"QCheckBox:disabled {\n"
"    color: #95a5a6;\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled {\n"
"    border-color: #ecf0f1;\n"
"    background-color: #f8f9fa;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled {\n"
""
                        "    background-color: #bdc3c7;\n"
"    border-color: #95a5a6;\n"
"}\n"
"\n"
"\n"
"QMessageBox {\n"
"    background-color: #ffffff;\n"
"    padding: 20px;\n"
"    font-family: \"Segoe UI\", \"Microsoft YaHei\", sans-serif;\n"
"}\n"
"\n"
"QMessageBox QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"    font-weight: 500;\n"
"    line-height: 1.5;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.work_group = QHBoxLayout()
        self.work_group.setObjectName(u"work_group")
        self.verticalLayout_database = QVBoxLayout()
        self.verticalLayout_database.setSpacing(0)
        self.verticalLayout_database.setObjectName(u"verticalLayout_database")
        self.cards_header = QLabel(self.centralwidget)
        self.cards_header.setObjectName(u"cards_header")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.cards_header.setFont(font)
        self.cards_header.setStyleSheet(u"color: #2c3e50; margin: 10px 0;")

        self.verticalLayout_database.addWidget(self.cards_header)

        self.scroll_area = QScrollArea(self.centralwidget)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"QScrollArea {\n"
"border: 2px solid #bdc3c7;\n"
"border-radius: 10px;\n"
"background-color: #ffffff;\n"
"}")
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.scroll_area_layout = QWidget()
        self.scroll_area_layout.setObjectName(u"scroll_area_layout")
        self.scroll_area_layout.setGeometry(QRect(0, 0, 628, 416))
        self.scroll_layout = QGridLayout(self.scroll_area_layout)
        self.scroll_layout.setObjectName(u"scroll_layout")
        self.scroll_layout.setContentsMargins(8, 8, 8, 8)
        self.scroll_widget = QWidget(self.scroll_area_layout)
        self.scroll_widget.setObjectName(u"scroll_widget")
        self.cards_layout = QGridLayout(self.scroll_widget)
        self.cards_layout.setObjectName(u"cards_layout")
        self.cards_layout.setContentsMargins(0, 0, 0, 0)

        self.scroll_layout.addWidget(self.scroll_widget, 0, 0, 1, 1)

        self.scroll_area.setWidget(self.scroll_area_layout)

        self.verticalLayout_database.addWidget(self.scroll_area)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 6, 6, 0)
        self.lineEditSearch = QLineEdit(self.centralwidget)
        self.lineEditSearch.setObjectName(u"lineEditSearch")

        self.horizontalLayout.addWidget(self.lineEditSearch)

        self.checkBoxWord = QCheckBox(self.centralwidget)
        self.checkBoxWord.setObjectName(u"checkBoxWord")
        self.checkBoxWord.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBoxWord.setChecked(True)

        self.horizontalLayout.addWidget(self.checkBoxWord)

        self.checkBoxSentence = QCheckBox(self.centralwidget)
        self.checkBoxSentence.setObjectName(u"checkBoxSentence")
        self.checkBoxSentence.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBoxSentence.setChecked(True)

        self.horizontalLayout.addWidget(self.checkBoxSentence)


        self.verticalLayout_database.addLayout(self.horizontalLayout)


        self.work_group.addLayout(self.verticalLayout_database)

        self.verticalLayout_sentence = QVBoxLayout()
        self.verticalLayout_sentence.setSpacing(0)
        self.verticalLayout_sentence.setObjectName(u"verticalLayout_sentence")
        self.sentence_header = QLabel(self.centralwidget)
        self.sentence_header.setObjectName(u"sentence_header")
        self.sentence_header.setFont(font)
        self.sentence_header.setStyleSheet(u"color: #2c3e50; margin: 10px 0;")

        self.verticalLayout_sentence.addWidget(self.sentence_header)

        self.sentence_builder = QTextEdit(self.centralwidget)
        self.sentence_builder.setObjectName(u"sentence_builder")
        self.sentence_builder.setStyleSheet(u"QTextEdit {\n"
"background-color: #ffffff;\n"
"border: 2px dashed #bdc3c7;\n"
"border-radius: 10px;\n"
"padding: 15px;\n"
"font-size: 14px;\n"
"color: #2c3e50;\n"
"}\n"
"QTextEdit:focus {\n"
"border: 2px solid #3498db;\n"
"background-color: #f8f9fa;\n"
"}")

        self.verticalLayout_sentence.addWidget(self.sentence_builder)

        self.sentence_controls_layout = QVBoxLayout()
        self.sentence_controls_layout.setSpacing(6)
        self.sentence_controls_layout.setObjectName(u"sentence_controls_layout")
        self.sentence_controls_layout.setContentsMargins(-1, 6, -1, 0)
        self.label_sentence_note = QLabel(self.centralwidget)
        self.label_sentence_note.setObjectName(u"label_sentence_note")

        self.sentence_controls_layout.addWidget(self.label_sentence_note)

        self.sentence_note_input = QLineEdit(self.centralwidget)
        self.sentence_note_input.setObjectName(u"sentence_note_input")

        self.sentence_controls_layout.addWidget(self.sentence_note_input)

        self.label_sentence_tag = QLabel(self.centralwidget)
        self.label_sentence_tag.setObjectName(u"label_sentence_tag")

        self.sentence_controls_layout.addWidget(self.label_sentence_tag)

        self.sentence_tag_input = QLineEdit(self.centralwidget)
        self.sentence_tag_input.setObjectName(u"sentence_tag_input")

        self.sentence_controls_layout.addWidget(self.sentence_tag_input)

        self.sentence_button_group = QHBoxLayout()
        self.sentence_button_group.setObjectName(u"sentence_button_group")
        self.delete_sentence_btn = QPushButton(self.centralwidget)
        self.delete_sentence_btn.setObjectName(u"delete_sentence_btn")
        self.delete_sentence_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.sentence_button_group.addWidget(self.delete_sentence_btn)

        self.clear_sentence_btn = QPushButton(self.centralwidget)
        self.clear_sentence_btn.setObjectName(u"clear_sentence_btn")
        self.clear_sentence_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.sentence_button_group.addWidget(self.clear_sentence_btn)

        self.analysis_sentence_btn = QPushButton(self.centralwidget)
        self.analysis_sentence_btn.setObjectName(u"analysis_sentence_btn")
        self.analysis_sentence_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.sentence_button_group.addWidget(self.analysis_sentence_btn)

        self.save_sentence_btn = QPushButton(self.centralwidget)
        self.save_sentence_btn.setObjectName(u"save_sentence_btn")
        self.save_sentence_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.sentence_button_group.addWidget(self.save_sentence_btn)


        self.sentence_controls_layout.addLayout(self.sentence_button_group)


        self.verticalLayout_sentence.addLayout(self.sentence_controls_layout)


        self.work_group.addLayout(self.verticalLayout_sentence)

        self.work_group.setStretch(0, 80)
        self.work_group.setStretch(1, 20)

        self.verticalLayout.addLayout(self.work_group)

        self.add_word_group = QGroupBox(self.centralwidget)
        self.add_word_group.setObjectName(u"add_word_group")
        self.add_word_group.setMaximumSize(QSize(16777215, 225))
        self.add_word_group.setStyleSheet(u"QGroupBox {\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"border: 2px solid #3498db;\n"
"border-radius: 10px;\n"
"margin-top: 10px;\n"
"padding-top: 20px;\n"
"}\n"
"QGroupBox::title {\n"
"subline-offset: -15px;\n"
"padding: 0 10px;\n"
"color: #3498db;\n"
"}")
        self.gridLayout = QGridLayout(self.add_word_group)
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.word_input = QLineEdit(self.add_word_group)
        self.word_input.setObjectName(u"word_input")

        self.gridLayout.addWidget(self.word_input, 0, 1, 1, 1)

        self.label_tag = QLabel(self.add_word_group)
        self.label_tag.setObjectName(u"label_tag")

        self.gridLayout.addWidget(self.label_tag, 1, 2, 1, 1)

        self.label_word = QLabel(self.add_word_group)
        self.label_word.setObjectName(u"label_word")

        self.gridLayout.addWidget(self.label_word, 0, 0, 1, 1)

        self.tag_input = QLineEdit(self.add_word_group)
        self.tag_input.setObjectName(u"tag_input")

        self.gridLayout.addWidget(self.tag_input, 1, 3, 1, 1)

        self.label_note = QLabel(self.add_word_group)
        self.label_note.setObjectName(u"label_note")

        self.gridLayout.addWidget(self.label_note, 1, 0, 1, 1)

        self.label_translation = QLabel(self.add_word_group)
        self.label_translation.setObjectName(u"label_translation")

        self.gridLayout.addWidget(self.label_translation, 0, 2, 1, 1)

        self.translation_input = QLineEdit(self.add_word_group)
        self.translation_input.setObjectName(u"translation_input")

        self.gridLayout.addWidget(self.translation_input, 0, 3, 1, 1)

        self.note_input = QLineEdit(self.add_word_group)
        self.note_input.setObjectName(u"note_input")

        self.gridLayout.addWidget(self.note_input, 1, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.delete_word_btn = QPushButton(self.add_word_group)
        self.delete_word_btn.setObjectName(u"delete_word_btn")
        self.delete_word_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.delete_word_btn)

        self.clear_word_btn = QPushButton(self.add_word_group)
        self.clear_word_btn.setObjectName(u"clear_word_btn")
        self.clear_word_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.clear_word_btn)

        self.add_word_btn = QPushButton(self.add_word_group)
        self.add_word_btn.setObjectName(u"add_word_btn")
        self.add_word_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.add_word_btn)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 4)


        self.verticalLayout.addWidget(self.add_word_group)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AI \u8bcd\u5e93\u7ba1\u7406\u5de5\u5177", None))
        self.cards_header.setText(QCoreApplication.translate("MainWindow", u"\U0001f4da \U00006570\U0000636e\U00005e93", None))
        self.lineEditSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u5173\u952e\u5b57\uff0c@\u6807\u7b7e\uff0c\u56de\u8f66\u8fdb\u884c\u641c\u7d22...", None))
        self.checkBoxWord.setText(QCoreApplication.translate("MainWindow", u"\u5355\u8bcd\u5e93", None))
        self.checkBoxSentence.setText(QCoreApplication.translate("MainWindow", u"\u53e5\u5b50\u5e93", None))
        self.sentence_header.setText(QCoreApplication.translate("MainWindow", u"\U0001f4dd \U000053e5\U00005b50\U00006784\U00005efa\U00005668", None))
        self.sentence_builder.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5c06\u5355\u8bcd\u62d6\u62fd\u5230\u8fd9\u91cc\u7ec4\u6210\u53e5\u5b50...", None))
        self.label_sentence_note.setText(QCoreApplication.translate("MainWindow", u"\u53e5\u5b50\u5907\u6ce8:", None))
        self.sentence_note_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u4e3a\u53e5\u5b50\u6dfb\u52a0\u5907\u6ce8...", None))
        self.label_sentence_tag.setText(QCoreApplication.translate("MainWindow", u"\u53e5\u5b50\u6807\u7b7e:", None))
        self.sentence_tag_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u4e3a\u53e5\u5b50\u6dfb\u52a0\u6807\u7b7e\uff0c\u591a\u4e2a\u7528\u9017\u53f7\u5206\u9694...", None))
        self.delete_sentence_btn.setText(QCoreApplication.translate("MainWindow", u"\u274c \u5220\u9664", None))
        self.clear_sentence_btn.setText(QCoreApplication.translate("MainWindow", u"\U0001f5d1 \U00006e05\U00007a7a", None))
        self.analysis_sentence_btn.setText(QCoreApplication.translate("MainWindow", u"\U0001f50e \U00005206\U00006790", None))
        self.save_sentence_btn.setText(QCoreApplication.translate("MainWindow", u"\U0001f4be \U00004fdd\U00005b58", None))
        self.add_word_group.setTitle(QCoreApplication.translate("MainWindow", u"\u2795 \u5355\u8bcd\u7f16\u8f91\u5668", None))
        self.word_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u5355\u8bcd...", None))
        self.label_tag.setText(QCoreApplication.translate("MainWindow", u"\u6807\u7b7e:", None))
        self.label_word.setText(QCoreApplication.translate("MainWindow", u"\u5355\u8bcd:", None))
        self.tag_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u6807\u7b7e\uff0c\u591a\u4e2a\u7528\u9017\u53f7\u5206\u9694...", None))
        self.label_note.setText(QCoreApplication.translate("MainWindow", u"\u5907\u6ce8:", None))
        self.label_translation.setText(QCoreApplication.translate("MainWindow", u"\u7ffb\u8bd1:", None))
        self.translation_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u7ffb\u8bd1...", None))
        self.note_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u5907\u6ce8...", None))
        self.delete_word_btn.setText(QCoreApplication.translate("MainWindow", u"\u274c \u5220\u9664\u5355\u8bcd", None))
        self.clear_word_btn.setText(QCoreApplication.translate("MainWindow", u"\U0001f5d1 \U00006e05\U00007a7a\U00008f93\U00005165", None))
        self.add_word_btn.setText(QCoreApplication.translate("MainWindow", u"\u2728 \u4fdd\u5b58\u5355\u8bcd", None))
    # retranslateUi

