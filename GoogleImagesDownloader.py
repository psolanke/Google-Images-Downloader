import sys
import os
import time
import argparse
import urllib
import json
import logging
import logging.handlers
from MainWindow import Ui_MainWindow
from DownloadUtils import WebDriverUtils, DownloadUtils
from PIL import Image
from PIL.ImageQt import ImageQt
import io
import subprocess

try:
    from PyQt5 import QtGui, QtCore, QWidgets
except ImportError:
    # needed for py3+qt4
    # Ref:
    # http://pyqt.sourceforge.net/Docs/PyQt4/incompatible_apis.html
    # http://stackoverflow.com/questions/21217399/pyqt4-qtcore-qvariant-object-instead-of-a-string
    if sys.version_info.major >= 3:
        import sip
        sip.setapi('QVariant', 2)
    from PyQt4 import QtCore, QtGui


def setup_logger():
    LOG_FILENAME = 'google_image_downloader.log'

    # Set up a specific logger with our desired output level
    parent_logger = logging.getLogger('google_image_downloader')
    parent_logger.setLevel(logging.DEBUG)

    # Add the log message handler to the logger
    fh = logging.handlers.RotatingFileHandler(LOG_FILENAME,
                                              maxBytes=100000, backupCount=5)
    fh.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)

    formatter = logging.Formatter('%(asctime)s - %(name)s -' +
                                  ' %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # add the handlers to the logger
    parent_logger.addHandler(fh)
    parent_logger.addHandler(ch)

    parent_logger.info('Logger Setup Complete')


class GoogleImagesDownloader(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(GoogleImagesDownloader, self).__init__(parent)
        self.webDriverUtils = WebDriverUtils()
        self.downloadUtils = DownloadUtils()
        self.save_dir = os.getcwd()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.delete_button.clicked.connect(self.delete_on_click)
        self.ui.save_button.clicked.connect(self.save_on_click)
        self.ui.next_image_button.clicked.connect(self.next_image_on_click)
        self.ui.previous_image_button.clicked.connect(self.previous_image_on_click)
        self.ui.search_button.clicked.connect(self.search_on_click)
        self.ui.save_dir_button.clicked.connect(self.save_dir_on_click)

        self.add_action('d', self.next_image_on_click)
        self.add_action('a', self.previous_image_on_click)
        self.add_action('s', self.save_on_click)

    def closeEvent(self, event):
        print('On_close')
        self.webDriverUtils.close()

    def add_action(self, shortcut, method_name):
        action = QtGui.QAction(self)
        action.setShortcut(shortcut)
        action.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.addAction(action)
        QtCore.QObject.connect(action, QtCore.SIGNAL("triggered()"), method_name)

    def next_image_on_click(self):
        print('Next Image')
        raw_image = self.downloadUtils.get_next_image()
        while not raw_image:
            raw_image = self.downloadUtils.get_next_image()
        self.update_image_view(raw_image)
        self.update_current_image_index_label()

    def previous_image_on_click(self):
        print('Previous Image')
        raw_image = self.downloadUtils.get_previous_image()
        self.update_image_view(raw_image)
        self.update_current_image_index_label()

    def update_image_view(self, raw_image):
        qimage = ImageQt(Image.open(io.BytesIO(raw_image)))
        pixmap = QtGui.QPixmap.fromImage(qimage).scaled(800, 800, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.ui.image_view.setPixmap(pixmap)

    def save_on_click(self):
        print('Saving Image...')
        saved_filename = self.downloadUtils.save_current_image(self.save_dir)
        self.update_saved_images_count_label()

    def delete_on_click(self):
        print('Deleting Image...')
        self.downloadUtils.delete_current_image()
        self.update_saved_images_count_label()

    def update_saved_images_count_label(self):
        count = self.downloadUtils.get_saved_images_count()
        self.ui.saved_images_count_label.setText(count)

    def search_on_click(self):
        print('Searching')
        search_text = self.ui.search_term_text_box.text().strip()
        new_images_list = self.webDriverUtils.get_image_urls_from_google_images(search_text)
        for url, _ in new_images_list:
            self.ui.loaded_url.addItem(str(url))
        self.downloadUtils.update_url_list(new_images_list)
        self.update_current_image_index_label()
        print(search_text)

    def update_current_image_index_label(self):
        count = self.downloadUtils.get_url_count()
        current_index = self.downloadUtils.get_current_image_index()
        self.ui.current_image_index_label.setText(str(count)+' \ '+str(current_index))

    def save_dir_on_click(self):
        print('changing save dir')
        open_dir = QtGui.QFileDialog.getExistingDirectory(self, "Open Directory",
                                                          self.save_dir,
                                                          QtGui.QFileDialog.ShowDirsOnly
                                                          | QtGui.QFileDialog.DontResolveSymlinks).strip()
        print(open_dir)
        if not open_dir == 0:
            print('New Folder : ' + open_dir)
            self.save_dir = open_dir


if __name__ == '__main__':
    setup_logger()
    app = QtGui.QApplication(sys.argv)
    google_image_downloader = GoogleImagesDownloader()
    google_image_downloader.show()
    sys.exit(app.exec_())
