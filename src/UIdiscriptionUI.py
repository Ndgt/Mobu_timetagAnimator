# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

try:
    from PySide6 import QtCore
    from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,QMetaObject,
                                QObject, QPoint, QRect,QSize, QTime, QUrl, Qt)
    from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,QFont,QFontDatabase,
                               QGradient, QIcon,QImage, QKeySequence, QLinearGradient,
                               QPainter, QPalette, QPixmap, QRadialGradient, QTransform)
    from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
                                   QLayout, QPushButton, QSizePolicy, QVBoxLayout,QWidget)
    
except:
    from PySide2 import QtCore
    from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,QMetaObject,
                                QObject, QPoint, QRect,QSize, QTime, QUrl, Qt)
    from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,QFont,QFontDatabase,
                               QGradient, QIcon,QImage, QKeySequence, QLinearGradient,
                               QPainter, QPalette, QPixmap, QRadialGradient, QTransform)
    from PySide2.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
                                   QLayout, QPushButton, QSizePolicy, QVBoxLayout,QWidget)


class Ui_ToolWindow(object):
    def setupUi(self, ToolWindow):
        if not ToolWindow.objectName():
            ToolWindow.setObjectName(u"ToolWindow")
        ToolWindow.resize(628, 304)
        self.horizontalLayout_2 = QHBoxLayout(ToolWindow)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 0, 15, 10)
        self.label = QLabel(ToolWindow)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label.setMargin(10)

        self.verticalLayout_2.addWidget(self.label)

        self.selectButton = QPushButton(ToolWindow)
        self.selectButton.setObjectName(u"selectButton")
        self.selectButton.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectButton.sizePolicy().hasHeightForWidth())
        self.selectButton.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        self.selectButton.setFont(font)

        self.verticalLayout_2.addWidget(self.selectButton)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout.setContentsMargins(20, 10, 20, 10)
        self.comboBox_1 = QComboBox(ToolWindow)
        self.comboBox_1.setObjectName(u"comboBox_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox_1.sizePolicy().hasHeightForWidth())
        self.comboBox_1.setSizePolicy(sizePolicy1)
        self.comboBox_1.view().setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.verticalLayout.addWidget(self.comboBox_1)

        self.comboBox_2 = QComboBox(ToolWindow)
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy1.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy1)
        self.comboBox_2.view().setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.verticalLayout.addWidget(self.comboBox_2)

        self.comboBox_3 = QComboBox(ToolWindow)
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy1.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy1)
        self.comboBox_3.view().setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.verticalLayout.addWidget(self.comboBox_3)

        self.comboBox_4 = QComboBox(ToolWindow)
        self.comboBox_4.setObjectName(u"comboBox_4")
        sizePolicy1.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy1)
        self.comboBox_4.view().setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.verticalLayout.addWidget(self.comboBox_4)

        self.comboBox_5 = QComboBox(ToolWindow)
        self.comboBox_5.setObjectName(u"comboBox_5")
        sizePolicy1.setHeightForWidth(self.comboBox_5.sizePolicy().hasHeightForWidth())
        self.comboBox_5.setSizePolicy(sizePolicy1)
        self.comboBox_5.view().setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.verticalLayout.addWidget(self.comboBox_5)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(ToolWindow)

        self.selectButton.connect(QtCore.SIGNAL("clicked()"), ToolWindow.SelectFile)
        QMetaObject.connectSlotsByName(ToolWindow)
    # setupUi

    def retranslateUi(self, ToolWindow):
        ToolWindow.setWindowTitle(QCoreApplication.translate("ToolWindow", u"Form", None))
        self.label.setText(QCoreApplication.translate("ToolWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">timetagAnimator</span></p><p><br/>Select shapekeys in your model from dropdownlist</p><p>equivalent to phonemes &quot;a&quot;, &quot;i&quot;, &quot;u&quot;, &quot;e&quot;, &quot;o&quot; .</p><p>Then press the button below to add keyframes </p><p>from .vsq / .lab file.</p><p>After automatically keyframes are apllyied,</p><p>You can make Mesh group for each shape key.</p></body></html>", None))
        self.selectButton.setText(QCoreApplication.translate("ToolWindow", u"select .vsq / .lab file", None))
    # retranslateUi

