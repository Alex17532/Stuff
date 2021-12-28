import sys
import ssl
import os
import zlib
ssl._create_default_https_context = ssl._create_unverified_context
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget
from pytube import YouTube

class homeScreen(QDialog):
    def __init__(self):
        super(homeScreen, self).__init__()
        loadUi("/Users/alexanderlongfellow/Desktop/Code/Python/Downloader/main.ui", self)

        self.download_btn.clicked.connect(self.download)
        

    def download(self):
        link = self.link.text()
        video = YouTube(link)
        stream = video.streams.get_by_itag(21)
        stream.download()
        self.console.setText("Success!")
        self.link.setText("")

app = QApplication(sys.argv)
home = homeScreen()
widget = QStackedWidget()
widget.addWidget(home)
widget.setFixedHeight(400)
widget.setFixedWidth(700)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")