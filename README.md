# README

## No.1

注意，UI 文件中存在表情，在 Windows 环境下，由于系统默认编码不是 UTF-8 所以会导致使用 pyside6-uic 直接转换时，生成的 Python 文件会有异常。

因此，需要先在终端中切换编码为 UTF-8，然后才能进行转换。

```commandline
chcp 65001
pyside6-uic.exe main.ui -o main_ui.py
```

## No.2

Qt Designer 的组件 QSplitter（分类器）需要选中需要分离的那两个组件，然后通过布局选中”使用拆分器水平拆分“进行使用。

## No.3

按钮组件在鼠标悬浮时的手势设置可以在 Qt Designer 对应组件中的 QWidget cursor 进行设置，而不需设置 QCSS。

## No.4

以下两种初始化方法都是一样的效果，其中第一种是 Python2 的兼容写法，第二种是简化写法。

```python
# Python2 兼容
def __init__(self, word_data):
    super(WordCard, self).__init__()
    self.ui = Ui_WordCard()
    self.ui.setupUi(self)

# Python3 简化
def __init__(self, word_data):
    super().__init__()
    self.ui = Ui_WordCard()
    self.ui.setupUi(self)
```

## No.5

QMimeData 是 Qt 框架中用于在拖放操作和剪贴板功能中传递数据的核心类。

QMimeData() 用于创建一个空的 QMimeData 对象，该对象可存储多种格式的数据（如文本、图像、URL 等），并确保数据在不同组件或应用间安全传输。

```python
drag = QDrag(self)
mime_data = QMimeData()
mime_data.setText(words)
drag.setMimeData(mime_data)
drag.exec(Qt.MoveAction)
```

## No.6

嵌套的布局需要使用迭代进行删除，否则无法删除嵌套布局下的子控件。

```python
def clean_cards(self, widget):
    while widget.count():
        child = widget.takeAt(0)
        if child.widget():
            child.widget().deleteLater()
        elif child.layout():
            self.clean_cards(child)
```

## No.7

水平布局可以通过 layoutStretch 控制布局所占据空间的比例，比如（80, 20）

## No.8

lineEdit 回车输入信号为 returnpass
