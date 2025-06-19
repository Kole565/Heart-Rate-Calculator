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
        MainWindow.resize(667, 536)
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
        __qtablewidgetitem8 = QTableWidgetItem()
        self.zonesTable.setItem(0, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.zonesTable.setItem(1, 2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.zonesTable.setItem(2, 2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.zonesTable.setItem(3, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.zonesTable.setItem(4, 2, __qtablewidgetitem12)
        self.zonesTable.setObjectName(u"zonesTable")
        self.zonesTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.zonesTable.setSortingEnabled(False)
        self.zonesTable.horizontalHeader().setVisible(True)
        self.zonesTable.horizontalHeader().setDefaultSectionSize(100)
        self.zonesTable.horizontalHeader().setStretchLastSection(True)
        self.zonesTable.verticalHeader().setDefaultSectionSize(80)

        self.verticalLayout.addWidget(self.zonesTable)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 667, 19))
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
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Zone 1 (Warmup)", None));
        ___qtablewidgetitem4 = self.zonesTable.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Zone 2 (Fat Burning Zone)", None));
        ___qtablewidgetitem5 = self.zonesTable.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Zone 3 (Intermediate)", None));
        ___qtablewidgetitem6 = self.zonesTable.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Zone 4 (Lactate Threshold)", None));
        ___qtablewidgetitem7 = self.zonesTable.verticalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Zone 5 (VO2 Max)", None));

        __sortingEnabled = self.zonesTable.isSortingEnabled()
        self.zonesTable.setSortingEnabled(False)
        ___qtablewidgetitem8 = self.zonesTable.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Colloquially described as \u201cvery light,\u201d you could probably continuously exercise for 1 - 6 hours in zone one.", None));
        ___qtablewidgetitem9 = self.zonesTable.item(1, 2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Like zone one, you should be able to pretty much churn away in zone two all day long.", None));
        ___qtablewidgetitem10 = self.zonesTable.item(2, 2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Zone three is where you enter subjectively moderate exercise intensities but still stay in the aerobic zone.", None));
        ___qtablewidgetitem11 = self.zonesTable.item(3, 2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"This heart rate zone corresponds to around lactate threshold; the point where the body begins to anaerobically generate ATP and produce more lactate than it can clear out or use.", None));
        ___qtablewidgetitem12 = self.zonesTable.item(4, 2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Zone five training typically involves brief, intermittent, all-out efforts (emphasis on brief).", None));
        self.zonesTable.setSortingEnabled(__sortingEnabled)

        self.menuCalculator.setTitle(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

