# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QTabWidget,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_toolWindow(object):
    def setupUi(self, toolWindow):
        if not toolWindow.objectName():
            toolWindow.setObjectName(u"toolWindow")
        toolWindow.resize(750, 475)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(toolWindow.sizePolicy().hasHeightForWidth())
        toolWindow.setSizePolicy(sizePolicy)
        toolWindow.setMinimumSize(QSize(700, 450))
        toolWindow.setMaximumSize(QSize(16777215, 600))
        self.verticalLayout_13 = QVBoxLayout(toolWindow)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 15)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.lyricsTab = QTabWidget(toolWindow)
        self.lyricsTab.setObjectName(u"lyricsTab")
        self.lyricsTab.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lyricsTab.sizePolicy().hasHeightForWidth())
        self.lyricsTab.setSizePolicy(sizePolicy1)
        self.lyricsTab.setMinimumSize(QSize(350, 0))
        self.lyricsTab.setMaximumSize(QSize(1000, 16777215))
        self.lyricsTab.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lyricsTab.setAutoFillBackground(False)
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_3 = QVBoxLayout(self.tab_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.navigateTextEdit = QTextEdit(self.tab_5)
        self.navigateTextEdit.setObjectName(u"navigateTextEdit")
        font = QFont()
        font.setPointSize(11)
        self.navigateTextEdit.setFont(font)

        self.verticalLayout_3.addWidget(self.navigateTextEdit)

        self.lyricsTab.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_17 = QVBoxLayout(self.tab_6)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.chooseLyricsButton = QPushButton(self.tab_6)
        self.chooseLyricsButton.setObjectName(u"chooseLyricsButton")

        self.horizontalLayout_14.addWidget(self.chooseLyricsButton)

        self.toHiraganaButton = QPushButton(self.tab_6)
        self.toHiraganaButton.setObjectName(u"toHiraganaButton")

        self.horizontalLayout_14.addWidget(self.toHiraganaButton)

        self.toAlphabetButton = QPushButton(self.tab_6)
        self.toAlphabetButton.setObjectName(u"toAlphabetButton")

        self.horizontalLayout_14.addWidget(self.toAlphabetButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_3)


        self.verticalLayout_18.addLayout(self.horizontalLayout_14)

        self.lyricsTextEdit = QTextEdit(self.tab_6)
        self.lyricsTextEdit.setObjectName(u"lyricsTextEdit")
        self.lyricsTextEdit.setFont(font)

        self.verticalLayout_18.addWidget(self.lyricsTextEdit)


        self.verticalLayout_17.addLayout(self.verticalLayout_18)

        self.lyricsTab.addTab(self.tab_6, "")

        self.verticalLayout_15.addWidget(self.lyricsTab)

        self.playerControlGroup = QGroupBox(toolWindow)
        self.playerControlGroup.setObjectName(u"playerControlGroup")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.playerControlGroup.sizePolicy().hasHeightForWidth())
        self.playerControlGroup.setSizePolicy(sizePolicy2)
        self.playerControlGroup.setMinimumSize(QSize(0, 0))
        self.playerControlGroup.setMaximumSize(QSize(400, 16777215))
        self.playerControlGroup.setSizeIncrement(QSize(0, 0))
        self.playerControlGroup.setFlat(False)
        self.playerControlGroup.setCheckable(False)
        self.horizontalLayout_9 = QHBoxLayout(self.playerControlGroup)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.playerSlider = QSlider(self.playerControlGroup)
        self.playerSlider.setObjectName(u"playerSlider")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.playerSlider.sizePolicy().hasHeightForWidth())
        self.playerSlider.setSizePolicy(sizePolicy3)
        self.playerSlider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_12.addWidget(self.playerSlider)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.startEndButton = QPushButton(self.playerControlGroup)
        self.startEndButton.setObjectName(u"startEndButton")
        sizePolicy.setHeightForWidth(self.startEndButton.sizePolicy().hasHeightForWidth())
        self.startEndButton.setSizePolicy(sizePolicy)

        self.verticalLayout_6.addWidget(self.startEndButton)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.speedLabel = QLabel(self.playerControlGroup)
        self.speedLabel.setObjectName(u"speedLabel")
        sizePolicy1.setHeightForWidth(self.speedLabel.sizePolicy().hasHeightForWidth())
        self.speedLabel.setSizePolicy(sizePolicy1)
        self.speedLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.speedLabel)

        self.speedSpinBox = QDoubleSpinBox(self.playerControlGroup)
        self.speedSpinBox.setObjectName(u"speedSpinBox")
        sizePolicy3.setHeightForWidth(self.speedSpinBox.sizePolicy().hasHeightForWidth())
        self.speedSpinBox.setSizePolicy(sizePolicy3)
        self.speedSpinBox.setMaximumSize(QSize(85, 16777215))
        self.speedSpinBox.setMinimum(0.100000000000000)
        self.speedSpinBox.setMaximum(2.000000000000000)
        self.speedSpinBox.setSingleStep(0.100000000000000)
        self.speedSpinBox.setValue(1.000000000000000)

        self.horizontalLayout_11.addWidget(self.speedSpinBox)


        self.verticalLayout_6.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_12.addLayout(self.verticalLayout_6)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_12)


        self.verticalLayout_15.addWidget(self.playerControlGroup)


        self.horizontalLayout_8.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.selectCharacterGroup = QGroupBox(toolWindow)
        self.selectCharacterGroup.setObjectName(u"selectCharacterGroup")
        sizePolicy2.setHeightForWidth(self.selectCharacterGroup.sizePolicy().hasHeightForWidth())
        self.selectCharacterGroup.setSizePolicy(sizePolicy2)
        self.selectCharacterGroup.setMinimumSize(QSize(300, 0))
        self.selectCharacterGroup.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_12 = QVBoxLayout(self.selectCharacterGroup)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.characterLabel = QLabel(self.selectCharacterGroup)
        self.characterLabel.setObjectName(u"characterLabel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.characterLabel.sizePolicy().hasHeightForWidth())
        self.characterLabel.setSizePolicy(sizePolicy4)
        self.characterLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.characterLabel)

        self.charaComboBox = QComboBox(self.selectCharacterGroup)
        self.charaComboBox.setObjectName(u"charaComboBox")
        sizePolicy3.setHeightForWidth(self.charaComboBox.sizePolicy().hasHeightForWidth())
        self.charaComboBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.charaComboBox)


        self.verticalLayout_12.addLayout(self.horizontalLayout_5)


        self.verticalLayout_14.addWidget(self.selectCharacterGroup)

        self.selectShapekeysGroup = QGroupBox(toolWindow)
        self.selectShapekeysGroup.setObjectName(u"selectShapekeysGroup")
        sizePolicy1.setHeightForWidth(self.selectShapekeysGroup.sizePolicy().hasHeightForWidth())
        self.selectShapekeysGroup.setSizePolicy(sizePolicy1)
        self.selectShapekeysGroup.setMinimumSize(QSize(300, 0))
        self.selectShapekeysGroup.setMaximumSize(QSize(300, 16777215))
        self.selectShapekeysGroup.setFlat(False)
        self.horizontalLayout_4 = QHBoxLayout(self.selectShapekeysGroup)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.shapekeyTab = QTabWidget(self.selectShapekeysGroup)
        self.shapekeyTab.setObjectName(u"shapekeyTab")
        self.shapekeyTab.setMaximumSize(QSize(16777215, 250))
        self.shapekeyTab.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.shapekeyTab.setStyleSheet(u"Tab2\n"
"")
        self.shapekeyTab.setTabPosition(QTabWidget.TabPosition.North)
        self.shapekeyTab.setMovable(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_3 = QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.skLabel_a = QLabel(self.tab)
        self.skLabel_a.setObjectName(u"skLabel_a")
        sizePolicy1.setHeightForWidth(self.skLabel_a.sizePolicy().hasHeightForWidth())
        self.skLabel_a.setSizePolicy(sizePolicy1)
        self.skLabel_a.setMinimumSize(QSize(25, 0))
        self.skLabel_a.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.skLabel_a)

        self.skLabel_i = QLabel(self.tab)
        self.skLabel_i.setObjectName(u"skLabel_i")
        self.skLabel_i.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.skLabel_i)

        self.skLabel_u = QLabel(self.tab)
        self.skLabel_u.setObjectName(u"skLabel_u")
        self.skLabel_u.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.skLabel_u)

        self.skLabel_e = QLabel(self.tab)
        self.skLabel_e.setObjectName(u"skLabel_e")
        self.skLabel_e.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.skLabel_e)

        self.skLabel_o = QLabel(self.tab)
        self.skLabel_o.setObjectName(u"skLabel_o")
        self.skLabel_o.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.skLabel_o)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.comboBox_1 = QComboBox(self.tab)
        self.comboBox_1.setObjectName(u"comboBox_1")
        sizePolicy3.setHeightForWidth(self.comboBox_1.sizePolicy().hasHeightForWidth())
        self.comboBox_1.setSizePolicy(sizePolicy3)
        self.comboBox_1.setMinimumSize(QSize(0, 25))

        self.verticalLayout_4.addWidget(self.comboBox_1)

        self.comboBox_2 = QComboBox(self.tab)
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy3.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy3)
        self.comboBox_2.setMinimumSize(QSize(0, 25))

        self.verticalLayout_4.addWidget(self.comboBox_2)

        self.comboBox_3 = QComboBox(self.tab)
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy3.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy3)
        self.comboBox_3.setMinimumSize(QSize(0, 25))

        self.verticalLayout_4.addWidget(self.comboBox_3)

        self.comboBox_4 = QComboBox(self.tab)
        self.comboBox_4.setObjectName(u"comboBox_4")
        sizePolicy3.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy3)
        self.comboBox_4.setMinimumSize(QSize(0, 25))

        self.verticalLayout_4.addWidget(self.comboBox_4)

        self.comboBox_5 = QComboBox(self.tab)
        self.comboBox_5.setObjectName(u"comboBox_5")
        sizePolicy3.setHeightForWidth(self.comboBox_5.sizePolicy().hasHeightForWidth())
        self.comboBox_5.setSizePolicy(sizePolicy3)
        self.comboBox_5.setMinimumSize(QSize(0, 25))

        self.verticalLayout_4.addWidget(self.comboBox_5)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout_11.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_11)

        self.shapekeyTab.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalLayout_9 = QVBoxLayout(self.tab_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.sk_Label_other_1 = QLabel(self.tab_2)
        self.sk_Label_other_1.setObjectName(u"sk_Label_other_1")
        self.sk_Label_other_1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_7.addWidget(self.sk_Label_other_1)

        self.sk_Label_other_2 = QLabel(self.tab_2)
        self.sk_Label_other_2.setObjectName(u"sk_Label_other_2")
        self.sk_Label_other_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_7.addWidget(self.sk_Label_other_2)

        self.sk_Label_other_3 = QLabel(self.tab_2)
        self.sk_Label_other_3.setObjectName(u"sk_Label_other_3")
        self.sk_Label_other_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_7.addWidget(self.sk_Label_other_3)


        self.horizontalLayout.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.comboBox_6 = QComboBox(self.tab_2)
        self.comboBox_6.setObjectName(u"comboBox_6")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.comboBox_6.sizePolicy().hasHeightForWidth())
        self.comboBox_6.setSizePolicy(sizePolicy5)
        self.comboBox_6.setMinimumSize(QSize(0, 25))

        self.verticalLayout_8.addWidget(self.comboBox_6)

        self.comboBox_7 = QComboBox(self.tab_2)
        self.comboBox_7.setObjectName(u"comboBox_7")
        sizePolicy5.setHeightForWidth(self.comboBox_7.sizePolicy().hasHeightForWidth())
        self.comboBox_7.setSizePolicy(sizePolicy5)
        self.comboBox_7.setMinimumSize(QSize(0, 25))

        self.verticalLayout_8.addWidget(self.comboBox_7)

        self.comboBox_8 = QComboBox(self.tab_2)
        self.comboBox_8.setObjectName(u"comboBox_8")
        sizePolicy5.setHeightForWidth(self.comboBox_8.sizePolicy().hasHeightForWidth())
        self.comboBox_8.setSizePolicy(sizePolicy5)
        self.comboBox_8.setMinimumSize(QSize(0, 25))

        self.verticalLayout_8.addWidget(self.comboBox_8)


        self.horizontalLayout.addLayout(self.verticalLayout_8)


        self.verticalLayout_10.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer)


        self.verticalLayout_9.addLayout(self.verticalLayout_10)

        self.shapekeyTab.addTab(self.tab_2, "")

        self.horizontalLayout_4.addWidget(self.shapekeyTab)


        self.verticalLayout_14.addWidget(self.selectShapekeysGroup)


        self.verticalLayout_16.addLayout(self.verticalLayout_14)

        self.recordingGroup = QGroupBox(toolWindow)
        self.recordingGroup.setObjectName(u"recordingGroup")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.recordingGroup.sizePolicy().hasHeightForWidth())
        self.recordingGroup.setSizePolicy(sizePolicy6)
        self.recordingGroup.setMinimumSize(QSize(250, 110))
        self.recordingGroup.setMaximumSize(QSize(300, 130))
        self.horizontalLayout_10 = QHBoxLayout(self.recordingGroup)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.addKeyButton = QPushButton(self.recordingGroup)
        self.addKeyButton.setObjectName(u"addKeyButton")
        sizePolicy4.setHeightForWidth(self.addKeyButton.sizePolicy().hasHeightForWidth())
        self.addKeyButton.setSizePolicy(sizePolicy4)
        self.addKeyButton.setMaximumSize(QSize(16777215, 50))
        self.addKeyButton.setStyleSheet(u"QPushButton {\u3000\n"
"\u3000\u3000background-color: rgb(255, 234, 199);\n"
"}")
        self.addKeyButton.setAutoDefault(False)
        self.addKeyButton.setFlat(False)

        self.verticalLayout_5.addWidget(self.addKeyButton)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.applyKeyframesButton = QPushButton(self.recordingGroup)
        self.applyKeyframesButton.setObjectName(u"applyKeyframesButton")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.applyKeyframesButton.sizePolicy().hasHeightForWidth())
        self.applyKeyframesButton.setSizePolicy(sizePolicy7)
        self.applyKeyframesButton.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_2.addWidget(self.applyKeyframesButton)

        self.exportAsTextButton = QPushButton(self.recordingGroup)
        self.exportAsTextButton.setObjectName(u"exportAsTextButton")
        sizePolicy7.setHeightForWidth(self.exportAsTextButton.sizePolicy().hasHeightForWidth())
        self.exportAsTextButton.setSizePolicy(sizePolicy7)
        self.exportAsTextButton.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_2.addWidget(self.exportAsTextButton)


        self.horizontalLayout_7.addLayout(self.verticalLayout_2)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_7)


        self.verticalLayout_16.addWidget(self.recordingGroup)


        self.horizontalLayout_8.addLayout(self.verticalLayout_16)


        self.verticalLayout_13.addLayout(self.horizontalLayout_8)


        self.retranslateUi(toolWindow)
        self.startEndButton.clicked.connect(toolWindow.PlayStop)
        self.speedSpinBox.valueChanged.connect(toolWindow.ChangePlaySpeed)
        self.chooseLyricsButton.clicked.connect(toolWindow.ChooseLyrics)
        self.toHiraganaButton.clicked.connect(toolWindow.ConvertHiragana)
        self.toAlphabetButton.clicked.connect(toolWindow.ConvertAlphabet)
        self.addKeyButton.pressed.connect(toolWindow.AddKeyIn)
        self.addKeyButton.released.connect(toolWindow.AddKeyOut)

        self.lyricsTab.setCurrentIndex(0)
        self.shapekeyTab.setCurrentIndex(0)
        self.addKeyButton.setDefault(False)


        QMetaObject.connectSlotsByName(toolWindow)
    # setupUi

    def retranslateUi(self, toolWindow):
        toolWindow.setWindowTitle(QCoreApplication.translate("toolWindow", u"Form", None))
        self.lyricsTab.setTabText(self.lyricsTab.indexOf(self.tab_5), QCoreApplication.translate("toolWindow", u"Navigate Key Input", None))
        self.chooseLyricsButton.setText(QCoreApplication.translate("toolWindow", u" Choose Lyrics File ", None))
        self.toHiraganaButton.setText(QCoreApplication.translate("toolWindow", u" To Hiragana", None))
        self.toAlphabetButton.setText(QCoreApplication.translate("toolWindow", u"To Alphabet", None))
        self.lyricsTab.setTabText(self.lyricsTab.indexOf(self.tab_6), QCoreApplication.translate("toolWindow", u"Edit Lyrics Text", None))
        self.playerControlGroup.setTitle(QCoreApplication.translate("toolWindow", u"Player Control", None))
        self.startEndButton.setText(QCoreApplication.translate("toolWindow", u"Play / Stop", None))
        self.speedLabel.setText(QCoreApplication.translate("toolWindow", u"Speed :", None))
        self.selectCharacterGroup.setTitle(QCoreApplication.translate("toolWindow", u" Select Character ", None))
        self.characterLabel.setText(QCoreApplication.translate("toolWindow", u"Character : ", None))
        self.selectShapekeysGroup.setTitle(QCoreApplication.translate("toolWindow", u" Select Shapekeys ", None))
        self.skLabel_a.setText(QCoreApplication.translate("toolWindow", u"a :", None))
        self.skLabel_i.setText(QCoreApplication.translate("toolWindow", u"i :", None))
        self.skLabel_u.setText(QCoreApplication.translate("toolWindow", u"u : ", None))
        self.skLabel_e.setText(QCoreApplication.translate("toolWindow", u"e : ", None))
        self.skLabel_o.setText(QCoreApplication.translate("toolWindow", u"o : ", None))
        self.shapekeyTab.setTabText(self.shapekeyTab.indexOf(self.tab), QCoreApplication.translate("toolWindow", u"LipSync", None))
        self.sk_Label_other_1.setText(QCoreApplication.translate("toolWindow", u"Shape 1 :", None))
        self.sk_Label_other_2.setText(QCoreApplication.translate("toolWindow", u"Shape 2 :", None))
        self.sk_Label_other_3.setText(QCoreApplication.translate("toolWindow", u"Shape 3 :", None))
        self.shapekeyTab.setTabText(self.shapekeyTab.indexOf(self.tab_2), QCoreApplication.translate("toolWindow", u"Other Shape", None))
        self.recordingGroup.setTitle(QCoreApplication.translate("toolWindow", u" Recording ", None))
        self.addKeyButton.setText(QCoreApplication.translate("toolWindow", u"Add Key", None))
#if QT_CONFIG(shortcut)
        self.addKeyButton.setShortcut(QCoreApplication.translate("toolWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.applyKeyframesButton.setText(QCoreApplication.translate("toolWindow", u"Apply to Face", None))
        self.exportAsTextButton.setText(QCoreApplication.translate("toolWindow", u"Export as .txt", None))
    # retranslateUi

