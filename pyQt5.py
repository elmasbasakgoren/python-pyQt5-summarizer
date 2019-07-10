from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

import grid as grid
from sumy.parsers.html import HtmlParser
#from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLineEdit, QGridLayout, QPushButton, QAction, QLineEdit, \
    QMessageBox, QToolTip, QLabel, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

#nltk.download()

LANGUAGE = "english"
SENTENCES_COUNT = 10


class App(QMainWindow, QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'metin ozetleme'
        self.left = 100
        self.top = 100
        self.width = 500
        self.height = 1000
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)

        self.button = QPushButton('add URL', self)
        self.button.move(20, 80)

        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Metin ozetleme', "You typed: " + textboxValue, QMessageBox.Ok,
                             QMessageBox.Ok)

        #textboxValue a URL alıncak.


        url = textboxValue
        parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
        stemmer = Stemmer(LANGUAGE)

        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words(LANGUAGE)

        for sentence in summarizer(parser.document, SENTENCES_COUNT):
         print(sentence)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

  #  url = "https://www.imdb.com/title/tt0266697/plotsummary?ref_=tt_ql_stry_3#synopsis"