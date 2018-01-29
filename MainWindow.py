# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys
import os
import logging
import logging.handlers

try:
    from PyQt5 import QtGui, QtCore, QtWidgets
except ImportError:
    # needed for py3+qt4
    # Ref:
    # http://pyqt.sourceforge.net/Docs/PyQt4/incompatible_apis.html
    # http://stackoverflow.com/questions/21217399/pyqt4-qtcore-qvariant-object-instead-of-a-string
    if sys.version_info.major >= 3:
        import sip
        sip.setapi('QVariant', 2)
    from PyQt4 import QtCore, QtGui


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

def setup_logger():
    LOG_FILENAME = 'google_image_downloader.log'

    # Set up a specific logger with our desired output level
    parent_logger = logging.getLogger('google_image_downloader')
    parent_logger.setLevel(logging.DEBUG)

    # Add the log message handler to the logger
    fh = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=100000, backupCount=5)
    fh.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # add the handlers to the logger
    parent_logger.addHandler(fh)
    parent_logger.addHandler(ch)

    parent_logger.info('Logger Setup Complete')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1016, 600)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.next_image_button = QtGui.QCommandLinkButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_image_button.sizePolicy().hasHeightForWidth())
        self.next_image_button.setSizePolicy(sizePolicy)
        self.next_image_button.setMinimumSize(QtCore.QSize(40, 40))
        self.next_image_button.setMaximumSize(QtCore.QSize(50, 50))
        self.next_image_button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.next_image_button.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("next"))
        self.next_image_button.setIcon(icon)
        self.next_image_button.setCheckable(False)
        self.next_image_button.setChecked(False)
        self.next_image_button.setObjectName(_fromUtf8("next_image_button"))
        self.gridLayout.addWidget(self.next_image_button, 2, 2, 1, 1)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.search_term_text_box = QtGui.QLineEdit(self.frame)
        self.search_term_text_box.setObjectName(_fromUtf8("search_term_text_box"))
        self.gridLayout_2.addWidget(self.search_term_text_box, 2, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 1, 1, 1, 1)
        self.delete_button = QtGui.QPushButton(self.frame)
        self.delete_button.setObjectName(_fromUtf8("delete_button"))
        self.gridLayout_2.addWidget(self.delete_button, 0, 1, 1, 1)
        self.num_images_text_box = QtGui.QLineEdit(self.frame)
        self.num_images_text_box.setObjectName(_fromUtf8("num_images_text_box"))
        self.gridLayout_2.addWidget(self.num_images_text_box, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.saved_url = QtGui.QListWidget(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saved_url.sizePolicy().hasHeightForWidth())
        self.saved_url.setSizePolicy(sizePolicy)
        self.saved_url.setObjectName(_fromUtf8("saved_url"))
        self.gridLayout_2.addWidget(self.saved_url, 5, 0, 1, 2)
        self.loaded_url = QtGui.QListWidget(self.frame)
        self.loaded_url.setObjectName(_fromUtf8("loaded_url"))
        self.gridLayout_2.addWidget(self.loaded_url, 6, 0, 1, 2)
        self.save_button = QtGui.QPushButton(self.frame)
        self.save_button.setObjectName(_fromUtf8("save_button"))
        self.gridLayout_2.addWidget(self.save_button, 0, 0, 1, 1)
        self.search_button = QtGui.QPushButton(self.frame)
        self.search_button.setObjectName(_fromUtf8("search_button"))
        self.gridLayout_2.addWidget(self.search_button, 3, 0, 1, 2)
        self.save_dir_button = QtGui.QPushButton(self.frame)
        self.save_dir_button.setObjectName(_fromUtf8("save_dir_button"))
        self.gridLayout_2.addWidget(self.save_dir_button, 4, 0, 1, 2)
        self.gridLayout.addWidget(self.frame, 2, 3, 1, 1)
        self.previous_image_button = QtGui.QCommandLinkButton(self.centralwidget)
        self.previous_image_button.setMinimumSize(QtCore.QSize(40, 40))
        self.previous_image_button.setMaximumSize(QtCore.QSize(50, 50))
        self.previous_image_button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.previous_image_button.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("previous"))
        self.previous_image_button.setIcon(icon)
        self.previous_image_button.setObjectName(_fromUtf8("previous_image_button"))
        self.gridLayout.addWidget(self.previous_image_button, 2, 0, 1, 1)
        self.image_view = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_view.sizePolicy().hasHeightForWidth())
        self.image_view.setSizePolicy(sizePolicy)
        self.image_view.setMinimumSize(QtCore.QSize(500, 300))
        self.image_view.setMaximumSize(QtCore.QSize(1200, 1000))
        self.image_view.setText(_fromUtf8(""))
        self.image_view.setObjectName(_fromUtf8("image_view"))
        self.gridLayout.addWidget(self.image_view, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.MainWindow = MainWindow
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self):
        self.MainWindow.setWindowTitle(_translate("MainWindow", "Google Image Downloader", None))
        self.label_3.setText(_translate("MainWindow", "Number of Images :", None))
        self.delete_button.setText(_translate("MainWindow", "Delete", None))
        self.label_2.setText(_translate("MainWindow", "Search Term :", None))
        self.save_button.setText(_translate("MainWindow", "Save", None))
        self.search_button.setText(_translate("MainWindow", "Search", None))
        self.save_dir_button.setText(_translate("MainWindow", "Change Save Dir", None))
        image_profile = QtGui.QImage('start.jpg') #QImage object
        image_profile = image_profile.scaled(800,800, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        leftPixelMap = QtGui.QPixmap(QtGui.QPixmap.fromImage(image_profile))
        self.image_view.setPixmap(leftPixelMap)
        

if __name__ == "__main__":
    setup_logger()
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    getText(ui)
    MainWindow.show()
    sys.exit(app.exec_())

