import json
import os
import sys
import time

from PySide6.QtWidgets import (QMainWindow, QHBoxLayout,
                               QMessageBox, QFrame,
                               QApplication, QSpacerItem, QSizePolicy)
from PySide6.QtCore import Qt, QMimeData, QThread, Signal, QObject, QPoint, Slot
from PySide6.QtGui import QDrag, QFontMetrics

from codingUi.card_ui import Ui_WordCard
from codingUi.main_ui import Ui_MainWindow

DATA_FILE = "database.json"


class DataManager(QObject):
    data_loaded = Signal(dict)
    data_saved = Signal(dict)
    data_searched = Signal(dict)
    error_occurred = Signal(str)

    def __init__(self):
        super().__init__()

    @Slot()
    def load_data(self):
        try:
            if not os.path.exists(DATA_FILE):
                data = {"words": {}, "sentences": {}}
                with open(DATA_FILE, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
                self.data_loaded.emit(data)
            else:
                with open(DATA_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                self.data_loaded.emit(data)
        except Exception as e:
            self.error_occurred.emit(f"加载数据失败: {str(e)}")

    @Slot(dict)
    def save_data(self, data):
        try:
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            self.data_saved.emit(data)
        except Exception as e:
            self.error_occurred.emit(f"保存数据失败: {str(e)}")

    @Slot(str, dict)
    def search_data(self, query, data):
        results = {
            "words": {},
            "sentences": {}
        }

        # 拆分查询词
        tag_search = False
        if query.startswith('@'):
            tag_search = True
            keyword = query[1:]
        else:
            keyword = query

        if not keyword:
            self.data_searched.emit(data)

        # 遍历 words 和 sentences 进行匹配
        if tag_search:
            for key, value in data.get("words", {}).items():
                tags = value.get("tags", "")
                if keyword in tags:
                    results["words"][key] = value
            for key, value in data.get("sentences", {}).items():
                tags = value.get("tags", "")
                if keyword in tags:
                    results["sentences"][key] = value
        else:
            for key, value in data.get("words", {}).items():
                word = value.get("word", "") + value.get("translation", "")
                if keyword in word:
                    results["words"][key] = value
            for key, value in data.get("sentences", {}).items():
                sentence = value.get("sentence", "") + value.get("translation", "")
                if keyword in sentence:
                    results["sentences"][key] = value

        self.data_searched.emit(results)

class WordCard(QFrame):
    data = Signal(dict)

    def __init__(self, data, max_width=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_WordCard()
        self.ui.setupUi(self)

        # 加载数据
        self.word_data = data
        self.text = f'{self.word_data["word"]} | {self.word_data["translation"]}'
        self.dragStartPosition = QPoint()

        # 设置宽度
        font_metrics = QFontMetrics(self.ui.word_label.font())
        font_width = font_metrics.horizontalAdvance(self.text) + 30
        self.width = font_width if font_width <= max_width else max_width
        self.setMaximumWidth(self.width)

        # 更新数据
        self.ui.word_label.setText(self.text)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:  # noqa
            self.data.emit(self.word_data)
            self.dragStartPosition = event.position().toPoint()

    def mouseMoveEvent(self, event):
        # 区分拖拽和点击事件
        if not (event.buttons() & Qt.LeftButton):  # noqa
            return
        if (event.position().toPoint() - self.dragStartPosition).manhattanLength() < QApplication.startDragDistance():
            return

        drag = QDrag(self)
        # 构建数据中转
        mime_data = QMimeData()
        mime_data.setText(self.word_data["word"] + ', ')
        drag.setMimeData(mime_data)
        drag.exec(Qt.MoveAction)  # noqa


class SentenceCard(QFrame):
    data = Signal(dict)

    def __init__(self, data, max_width=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_WordCard()
        self.ui.setupUi(self)

        # 加载数据
        self.sentence_data = data
        self.text = f'📝 {self.sentence_data["sentence"]}'
        self.dragStartPosition = QPoint()

        # 设置宽度
        font_metrics = QFontMetrics(self.ui.word_label.font())
        font_width = font_metrics.horizontalAdvance(self.text) + 30
        self.width = font_width if font_width <= max_width else max_width
        self.setMaximumWidth(self.width)
        self.ui.word_label.setAlignment(Qt.AlignLeft)  # noqa

        # 更新数据
        self.ui.word_label.setText(self.text)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:  # noqa
            self.data.emit(self.sentence_data)
            self.dragStartPosition = event.position().toPoint()

    def mouseMoveEvent(self, event):
        # 区分拖拽和点击事件
        if not (event.buttons() & Qt.LeftButton):  # noqa
            return
        if (event.position().toPoint() - self.dragStartPosition).manhattanLength() < QApplication.startDragDistance():
            return

        drag = QDrag(self)
        # 构建数据中转
        mime_data = QMimeData()
        mime_data.setText(self.sentence_data["sentence"] + ', ')
        drag.setMimeData(mime_data)
        drag.exec(Qt.MoveAction)  # noqa


class MainWindow(QMainWindow):
    data_load = Signal()
    data_save = Signal(dict)
    data_search = Signal(str, dict)
    data_show = Signal(dict)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 初始化数据
        self.data = {"words": {}, "sentences": {}}
        self.current_mode = {"words": True, "sentences": True}

        # 初始化数据管理器和工作线程
        self.data_manager = DataManager()
        self.worker_thread = QThread()
        self.data_manager.moveToThread(self.worker_thread)
        self.worker_thread.start()

        # 绑定数据处理事件
        self.data_load.connect(self.data_manager.load_data)
        self.data_save.connect(self.data_manager.save_data)
        self.data_search.connect(self.data_manager.search_data)
        self.data_manager.data_loaded.connect(self.refresh_data)
        self.data_manager.data_saved.connect(self.refresh_data)
        self.data_manager.data_searched.connect(self.refresh_search_data)
        self.data_manager.error_occurred.connect(self.send_message)
        self.ui.checkBoxWord.clicked.connect(self.refresh_model_word)
        self.ui.checkBoxSentence.clicked.connect(self.refresh_model_sentence)
        self.data_show.connect(self.refresh_cards)
        self.ui.clear_word_btn.clicked.connect(self.clear_word)
        self.ui.clear_sentence_btn.clicked.connect(self.clear_sentence)
        self.ui.add_word_btn.clicked.connect(self.add_word)
        self.ui.save_sentence_btn.clicked.connect(self.add_sentence)
        self.ui.delete_word_btn.clicked.connect(self.delete_word)
        self.ui.delete_sentence_btn.clicked.connect(self.delete_sentence)
        self.ui.analysis_sentence_btn.clicked.connect(self.analysis_sentence_save)
        self.ui.lineEditSearch.returnPressed.connect(self.search_data)

        # 加载数据
        self.data_load.emit()

    def search_data(self):
        query = self.ui.lineEditSearch.text()
        if query == "":
            self.data_load.emit()
            return
        self.data_search.emit(query, self.data)

    def refresh_data(self, data):
        self.data = data
        self.data_show.emit(self.data)

    def refresh_search_data(self, data):
        self.data_show.emit(data)

    def refresh_model_word(self, checked):
        self.current_mode["words"] = checked
        self.data_show.emit(self.data)

    def refresh_model_sentence(self, checked):
        self.current_mode["sentences"] = checked
        self.data_show.emit(self.data)

    def refresh_cards(self, data):
        """刷新卡片显示"""
        # 清理
        self.clean_cards(self.ui.cards_layout)
        scroll_width = self.ui.scroll_area.width()
        # 展示
        if all(self.current_mode.values()):
            current_row = self.add_card(WordCard, self.refresh_word, data["words"], scroll_width)
            current_row = self.add_card(SentenceCard, self.refresh_sentence, data["sentences"], scroll_width, current_row+1)
            vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)  # noqa
            self.ui.cards_layout.addItem(vertical_spacer, current_row+1, 0)
        elif self.current_mode["words"]:
            current_row = self.add_card(WordCard, self.refresh_word, data["words"], scroll_width)
            vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)  # noqa
            self.ui.cards_layout.addItem(vertical_spacer, current_row + 1, 0)
        elif self.current_mode["sentences"]:
            current_row = self.add_card(SentenceCard, self.refresh_sentence, data["sentences"], scroll_width)
            vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)  # noqa
            self.ui.cards_layout.addItem(vertical_spacer, current_row + 1, 0)
        else:
            self.clean_cards(self.ui.cards_layout)

    def add_card(self, card_model, callback, data, scroll_width, row = 0):
        current_width = scroll_width
        current_layout = 0
        horizontal_layouts = [QHBoxLayout()]
        self.ui.cards_layout.addLayout(horizontal_layouts[current_layout], row, 0)
        for key, value in data.items():
            card = card_model(value, scroll_width - 50)
            card.data.connect(callback)
            current_width -= (card.width + 6)
            if current_width > 0:
                horizontal_layouts[current_layout].addWidget(card)
            else:
                horizontal_layouts[current_layout].addSpacerItem(
                    QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))  # noqa
                current_layout += 1
                row += 1
                current_width = scroll_width - (card.width + 6)
                horizontal_layouts.append(QHBoxLayout())
                self.ui.cards_layout.addLayout(horizontal_layouts[current_layout], row, 0)
                horizontal_layouts[current_layout].addWidget(card)
        horizontal_layouts[current_layout].addSpacerItem(
            QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))  # noqa
        return row

    def clean_cards(self, widget):
        while widget.count():
            child = widget.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
            elif child.layout():
                self.clean_cards(child)

    def send_message(self, message):
        QMessageBox.information(self, "Message", message)

    def refresh_word(self, data):
        self.ui.word_input.setText(data["word"])
        self.ui.translation_input.setText(data["translation"])
        self.ui.note_input.setText(data["note"])
        self.ui.tag_input.setText(','.join(data["tags"]))

    def refresh_sentence(self, data):
        self.ui.sentence_builder.setText(data["sentence"])
        self.ui.sentence_note_input.setText(data["note"])
        self.ui.sentence_tag_input.setText(','.join(data["tags"]))

    def clear_word(self):
        self.ui.word_input.clear()
        self.ui.translation_input.clear()
        self.ui.note_input.clear()
        self.ui.tag_input.clear()

    def clear_sentence(self):
        self.ui.sentence_builder.clear()
        self.ui.sentence_note_input.clear()
        self.ui.sentence_tag_input.clear()

    def add_word(self):
        """添加单词"""
        word = self.ui.word_input.text().strip()
        translation = self.ui.translation_input.text().strip()
        note = self.ui.note_input.text().strip()
        tags = [t.strip() for t in self.ui.tag_input.text().split(",") if t.strip()]

        if not word:
            QMessageBox.warning(self, "警告", "请输入单词")
            return

        new_word = {
            "word": word,
            "translation": translation,
            "note": note,
            "tags": tags,
            "id": time.time()
        }

        self.data["words"][word] = new_word
        self.data_save.emit(self.data)

        # 清空输入框
        self.ui.word_input.clear()
        self.ui.translation_input.clear()
        self.ui.note_input.clear()
        self.ui.tag_input.clear()

    def add_sentence(self):
        """添加单词"""
        sentence = self.ui.sentence_builder.toPlainText().strip()
        note = self.ui.sentence_note_input.text().strip()
        tags = [t.strip() for t in self.ui.sentence_tag_input.text().split(",") if t.strip()]

        if not sentence:
            QMessageBox.warning(self, "警告", "请输入句子")
            return

        new_sentence = {
            "sentence": sentence,
            "translation": "",
            "note": note,
            "tags": tags,
            "id": time.time()
        }

        self.data["sentences"][sentence] = new_sentence
        self.data_save.emit(self.data)

        # 清空输入框
        self.ui.sentence_builder.clear()
        self.ui.sentence_note_input.clear()
        self.ui.sentence_tag_input.clear()

    def delete_word(self):
        reply = QMessageBox.question(
            self,
            "确认操作",
            "确定要继续执行吗？",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply != QMessageBox.StandardButton.Yes:
            return

        word = self.ui.word_input.text().strip()
        if not word:
            QMessageBox.warning(self, "警告", "请输入单词")
            return
        if word in self.data["words"]:
            self.data["words"].pop(word, None)
            self.data_save.emit(self.data)
        else:
            QMessageBox.warning(self, "警告", "该单词不存在")

        # 清空输入框
        self.ui.word_input.clear()
        self.ui.translation_input.clear()
        self.ui.note_input.clear()
        self.ui.tag_input.clear()

    def delete_sentence(self):
        reply = QMessageBox.question(
            self,
            "确认操作",
            "确定要继续执行吗？",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply != QMessageBox.StandardButton.Yes:
            return

        sentence = self.ui.sentence_builder.toPlainText().strip()
        if not sentence:
            QMessageBox.warning(self, "警告", "请输入句子")
            return
        if sentence in self.data["sentences"]:
            self.data["sentences"].pop(sentence, None)
            self.data_save.emit(self.data)
        else:
            QMessageBox.warning(self, "警告", "该句子不存在")

        # 清空输入框
        self.ui.sentence_builder.clear()
        self.ui.sentence_note_input.clear()
        self.ui.sentence_tag_input.clear()

    def analysis_sentence_save(self):
        sentence = self.ui.sentence_builder.toPlainText().strip()
        if not sentence:
            QMessageBox.warning(self, "警告", "请输入句子")
            return
        words = [t.strip() for t in sentence.split(",") if t.strip()]

        # 以单词储存
        for each in words:
            each = each.replace("(", "").replace(")", "")
            if each in self.data["words"]:
                continue
            new_word = {
                "word": each,
                "translation": "",
                "note": "",
                "tags": "",
                "id": time.time()
            }
            self.data["words"][each] = new_word

        # 保存到文件
        self.data_save.emit(self.data)

        # 清空输入框
        self.ui.sentence_builder.clear()
        self.ui.sentence_note_input.clear()
        self.ui.sentence_tag_input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
