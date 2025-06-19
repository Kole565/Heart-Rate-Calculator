# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(370, 315)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.ageInput = QLineEdit(self.centralwidget)
        self.ageInput.setObjectName(u"ageInput")
        self.ageInput.setMaxLength(3)

        self.horizontalLayout.addWidget(self.ageInput)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.resthrInput = QLineEdit(self.centralwidget)
        self.resthrInput.setObjectName(u"resthrInput")
        self.resthrInput.setMaxLength(3)

        self.horizontalLayout_2.addWidget(self.resthrInput)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.zonesTable = QTableWidget(self.centralwidget)
        if (self.zonesTable.columnCount() < 3):
            self.zonesTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.zonesTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.zonesTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.zonesTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.zonesTable.rowCount() < 5):
            self.zonesTable.setRowCount(5)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.zonesTable.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.zonesTable.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.zonesTable.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.zonesTable.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.zonesTable.setVerticalHeaderItem(4, __qtablewidgetitem7)
        self.zonesTable.setObjectName(u"zonesTable")
        self.zonesTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.verticalLayout.addWidget(self.zonesTable)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 370, 19))
        self.menuCalculator = QMenu(self.menubar)
        self.menuCalculator.setObjectName(u"menuCalculator")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuCalculator.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Enter age:", None))
        self.ageInput.setInputMask("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Enter rest heart rate:", None))
        self.resthrInput.setInputMask("")
        ___qtablewidgetitem = self.zonesTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Lower bound", None));
        ___qtablewidgetitem1 = self.zonesTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Upper bound", None));
        ___qtablewidgetitem2 = self.zonesTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem3 = self.zonesTable.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Zone 1", None));
        ___qtablewidgetitem4 = self.zonesTable.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Zone 2", None));
        ___qtablewidgetitem5 = self.zonesTable.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Zone 3", None));
        ___qtablewidgetitem6 = self.zonesTable.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Zone 4", None));
        ___qtablewidgetitem7 = self.zonesTable.verticalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Zone 5", None));
        self.menuCalculator.setTitle(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

