
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

# ########
class ZaherWebBrowser(object):
    def __init__(self, *args, **kwargs):
        super(ZaherWebBrowser, self).__init__(*args, **kwargs)

    self.window = QtWidgets()
    self.window.setWindowTitle("متصفح زاهر")
    #
    self.layout = QVBoxLayout()
    self.horizontal = QHBoxLayout()
    #
    self.url_bar =QTextEdit()
    self.url_bar = setMaximumHeight(30)
    self.url_bar = setPlaceholderText("الرجاء ادخال الرابط")
    #
    # QIcon("icons/go.png"),    
    self.go_btn = QPushButton(" إبحث ", self.window)
    self.go_btn = setMinimumHeight(30)
    #
    # QIcon("icons/back.png"),
    self.back_btn = QPushButton(" للخلف ", self.window)
    self.back_btn = setMinimumHeight(30)
    #
    # QIcon("icons/go.png"),
    self.forward_btn = QPushButton(" للأمام ", self.window)
    self.forward_btn = setMinimumHeight(30)
    #
    self.horizontal.addWidget(self.url_bar)
    self.horizontal.addWidget(self.go_btn)
    self.horizontal.addWidget(self.back_btn)
    self.horizontal.addWidget(self.forward_btn)
    #
    self.browser = QWebEngineView()
    self.layout.addLayout(self.horizontal)
    self.layout.addWidget(self.browser)
    self.browser.setUrl(QUrl("http://www.google.com"))
    #
    self.window.setLayout(self.layout)
    self.window.show()
    #


app = QApplication([])
window = ZaherWebBrowser()
app.exec_()
