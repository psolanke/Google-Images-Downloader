# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

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
        self.gridLayout.addWidget(self.next_image_button, 2, 3, 1, 1)
        self.previous_image_button = QtGui.QCommandLinkButton(self.centralwidget)
        self.previous_image_button.setMinimumSize(QtCore.QSize(40, 40))
        self.previous_image_button.setMaximumSize(QtCore.QSize(50, 50))
        self.previous_image_button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.previous_image_button.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("previous"))
        self.previous_image_button.setIcon(icon)
        self.previous_image_button.setObjectName(_fromUtf8("previous_image_button"))
        self.gridLayout.addWidget(self.previous_image_button, 2, 0, 1, 1)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.loaded_url = QtGui.QListWidget(self.frame)
        self.loaded_url.setObjectName(_fromUtf8("loaded_url"))
        self.gridLayout_2.addWidget(self.loaded_url, 8, 0, 1, 2)
        self.saved_url = QtGui.QListWidget(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saved_url.sizePolicy().hasHeightForWidth())
        self.saved_url.setSizePolicy(sizePolicy)
        self.saved_url.setObjectName(_fromUtf8("saved_url"))
        self.gridLayout_2.addWidget(self.saved_url, 7, 0, 1, 2)
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.save_button = QtGui.QPushButton(self.frame_2)
        self.save_button.setObjectName(_fromUtf8("save_button"))
        self.horizontalLayout.addWidget(self.save_button)
        self.delete_button = QtGui.QPushButton(self.frame_2)
        self.delete_button.setObjectName(_fromUtf8("delete_button"))
        self.horizontalLayout.addWidget(self.delete_button)
        self.save_dir_button = QtGui.QPushButton(self.frame_2)
        self.save_dir_button.setObjectName(_fromUtf8("save_dir_button"))
        self.horizontalLayout.addWidget(self.save_dir_button)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 2)
        self.frame_3 = QtGui.QFrame(self.frame)
        self.frame_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.frame_3)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.search_term_text_box = QtGui.QLineEdit(self.frame_3)
        self.search_term_text_box.setObjectName(_fromUtf8("search_term_text_box"))
        self.horizontalLayout_2.addWidget(self.search_term_text_box)
        self.search_button = QtGui.QPushButton(self.frame_3)
        self.search_button.setObjectName(_fromUtf8("search_button"))
        self.horizontalLayout_2.addWidget(self.search_button)
        self.gridLayout_2.addWidget(self.frame_3, 1, 0, 1, 2)
        self.frame_5 = QtGui.QFrame(self.frame)
        self.frame_5.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(self.frame_5)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.saved_images_count_label = QtGui.QLabel(self.frame_5)
        self.saved_images_count_label.setObjectName(_fromUtf8("saved_images_count_label"))
        self.horizontalLayout_3.addWidget(self.saved_images_count_label)
        self.save_all_button = QtGui.QPushButton(self.frame_5)
        self.save_all_button.setObjectName(_fromUtf8("save_all_button"))
        self.horizontalLayout_3.addWidget(self.save_all_button)
        self.gridLayout_2.addWidget(self.frame_5, 2, 0, 1, 2)
        self.gridLayout.addWidget(self.frame, 2, 4, 1, 1)
        self.frame_4 = QtGui.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame_4)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.image_view = QtGui.QLabel(self.frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_view.sizePolicy().hasHeightForWidth())
        self.image_view.setSizePolicy(sizePolicy)
        self.image_view.setMinimumSize(QtCore.QSize(500, 300))
        self.image_view.setMaximumSize(QtCore.QSize(1200, 1000))
        self.image_view.setText(_fromUtf8(""))
        self.image_view.setObjectName(_fromUtf8("image_view"))
        self.verticalLayout.addWidget(self.image_view)
        self.current_image_index_label = QtGui.QLabel(self.frame_4)
        self.current_image_index_label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.current_image_index_label.setAlignment(QtCore.Qt.AlignCenter)
        self.current_image_index_label.setObjectName(_fromUtf8("current_image_index_label"))
        self.verticalLayout.addWidget(self.current_image_index_label)
        self.gridLayout.addWidget(self.frame_4, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Google Image Downloader", None))
        self.save_button.setText(_translate("MainWindow", "Save", None))
        self.delete_button.setText(_translate("MainWindow", "Delete", None))
        self.save_dir_button.setText(_translate("MainWindow", "Change Save Dir", None))
        self.label_2.setText(_translate("MainWindow", "Search Term ", None))
        self.search_button.setText(_translate("MainWindow", "Search", None))
        self.label.setText(_translate("MainWindow", "No. of saved images :", None))
        self.saved_images_count_label.setText(_translate("MainWindow", "0", None))
        self.save_all_button.setText(_translate("MainWindow", "Save all", None))
        self.current_image_index_label.setText(_translate("MainWindow", "0/0", None))
        image_profile = QtGui.QImage('start.jpg') #QImage object
        image_profile = image_profile.scaled(800,800, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        leftPixelMap = QtGui.QPixmap(QtGui.QPixmap.fromImage(image_profile))
        self.image_view.setPixmap(leftPixelMap)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

