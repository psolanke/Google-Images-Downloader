import sys
import os
import time
import argparse
import urllib
import json
import logging
import logging.handlers
from MainWindow import Ui_MainWindow
from webDriverUtils import WebDriverUtils

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

os.system("echo 'executing'")
os.system('Xvf :10 -ac &')
os.system('export DISPLAY=:10')

class GoogleImagesDownloader(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        super(GoogleImagesDownloader, self).__init__(parent)
        self.webDriverUtils = WebDriverUtils()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.save_button.clicked.connect(self.save_on_click)
        self.ui.next_image_button.clicked.connect(self.next_image_on_click)
        self.ui.previous_image_button.clicked.connect(self.previous_image_on_click)
        self.ui.search_button.clicked.connect(self.search_on_click)
        self.ui.save_dir_button.clicked.connect(self.save_dir_on_click)

        self.add_action('d', self.next_image_on_click)
        self.add_action('a', self.previous_image_on_click)
        self.add_action('s', self.save_on_click)

    def add_action(self, shortcut, method_name):
        action = QtGui.QAction(self) 
        action.setShortcut(shortcut) 
        action.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.addAction(action)
        QtCore.QObject.connect(action, QtCore.SIGNAL("triggered()"), method_name)

    def next_image_on_click(self):
        print('Next Image')

    def previous_image_on_click(self):
        print('Previous Image')

    def save_on_click(self):
        print('Save Image')

    def search_on_click(self):
        print('Searching')
        search_text = self.ui.search_term_text_box.text().strip()
        num_samples = self.ui.num_images_text_box.text().strip()
        actual_images = self.webDriverUtils.get_image_urls_from_google_images(int(num_samples), search_text)
        for url in actual_images:
            self.ui.loaded_url.addItem(str(url))
        print(search_text)
        print(num_samples)

    def save_dir_on_click(self):
        print('changing save dir')
        open_dir = QtGui.QFileDialog.getExistingDirectory(self, "Open Directory",
                                                 os.getcwd(),
                                                 QtGui.QFileDialog.ShowDirsOnly
                                                 | QtGui.QFileDialog.DontResolveSymlinks).strip()
        print(open_dir)
        if not len(open_dir) == 0:
            print('New Folder : ' + open_dir)
            self.save_dir = open_dir
    

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    calculator = GoogleImagesDownloader()
    calculator.show()
    sys.exit(app.exec_())