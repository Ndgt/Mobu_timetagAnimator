from pyfbsdk import*
from pyfbsdk_additions import*

# for MotionuBuilder 2025
try:
    from PySide6 import QtWidgets
    from PySide6.QtGui import QTextCursor

# for MotionBuilder -2024
except:
    from PySide2 import QtWidgets
    from PySide2.QtGui import QTextCursor

from ui_timetagAnimator import Ui_toolWindow
import L_Edit
import re

# the class of Qt widget which main FBTool holds 
class HoldedWidget(QtWidgets.QWidget, Ui_toolWindow):
    def __init__(self, pWigholder):
        super().__init__(pWigholder)
        self.setupUi(self)

        """ about charaCombobox """
        # for system event notification when importing new file
        self.sys = FBSystem()
        self.app = FBApplication()
        self.sys.OnConnectionDataNotify.Add(self.charaComboUpdate)
        self.app.OnFileExit.Add(self.DataNotifyRemove)
        
        # setup the character combobox
        self.charaComboBox.addItem("character not selected")
        for chara in self.sys.Scene.Characters:
            self.charaComboBox.addItem(chara.Name)
        # connect signal
        self.charaComboBox.currentIndexChanged.connect(self.updateComboBoxes)


        """ about shapekey comboboxes """
        # setup the shapekey comboboxes
        self.comboboxes = [self.comboBox_1,
                           self.comboBox_2,
                           self.comboBox_3,
                           self.comboBox_4,
                           self.comboBox_5,
                           self.comboBox_6,
                           self.comboBox_7,
                           self.comboBox_8]
        for cbox in self.comboboxes:
            cbox.addItem("shapekey not selected")

        # add shapekey name in case some character already exist
        self.shapeList = self.ReturnCharaShape()
        if not self.shapeList is None:
           for name in self.shapeList:
                for cbox in self.comboboxes:
                    cbox.addItem(name)


        """ about player control """
        self.nowplayng = False # parameter to know Player condition
        self.playcontrol = FBPlayerControl()


        """ about TextEditor """
        # initialize cursor instances
        self.editorCursor = self.lyricsTextEdit.textCursor()
        self.navigatorCursor = self.navigateTextEdit.textCursor()

        """ about timetag """
        self.pattern = r'^[\u3040-\u309F]+$'


    """ functions about character combobox """
    def AddDataNotify(self):
        self.charaComboUpdate()

    def DataNotifyRemove(self):
        self.sys.OnConnectionDataNotify.Remove(self.AddDataNotify)

    def charaComboUpdate(self,control,event):
        items = []
        for i in range(1,self.charaComboBox.count()):
            items.append(self.charaComboBox.itemText(i))
        for chara in self.sys.Scene.Characters:
            if not chara is None:
                if not chara.Name in items:
                    self.charaComboBox.addItem(chara.Name)

    # return All shapekey name in character user selected
    def ReturnCharaShape(self) -> list:
        mList = FBModelList()
        returnList = []
        # get current selected character
        if self.charaComboBox.count() > 1:
            chara = self.sys.Scene.Characters.__getitem__(self.charaComboBox.currentIndex()-1)
        
            # get all meshes related to the character
            chara.GetSkinModelList(mList)
            for mesh in mList:
                geo = mesh.Geometry
                for i in range(geo.ShapeGetCount()):
                    name = geo.ShapeGetName(i)
                    if not name in returnList:
                        returnList.append(name)
            return returnList

    # update character combobox when user select new item
    def updateComboBoxes(self):
        for cbox in self.comboboxes:
            cbox.clear()
            cbox.addItem("shapekey not selected")
            slist = self.ReturnCharaShape()
            if not slist is None:
                for shapekey in slist:
                    cbox.addItem(shapekey)

    
    ''' functions about Lyrics Editting '''
    def ChooseLyrics(self):
        # display popup to select a file
        self.lpopup = FBFilePopup()
        self.lpopup.Caption = "Select a file"
        self.lpopup.Style = FBFilePopupStyle.kFBFilePopupOpen
        self.lpopup.Filter = "*"
        self.lcheck = self.lpopup.Execute()

        if self.lcheck:
            # check if the file is text file
            if self.lpopup.FileName[-4:] == ".txt":
                lyrics = L_Edit.ReadLyrics(self.lpopup.FileName)
                if type(lyrics) != UnicodeDecodeError:
                    for line in lyrics.split("\n"):
                        self.lyricsTextEdit.append(line)

                    # focus on the start
                    self.editorCursor.movePosition(QTextCursor.Start)
                    self.lyricsTextEdit.setTextCursor(self.editorCursor)    

            else:
                FBMessageBox("Caution","Error : Selected file is not text file.","OK")


    def ConvertHiragana(self):
        cursor = self.lyricsTextEdit.textCursor()
        cursor.select(QTextCursor.Document)
        lyrics = cursor.selectedText()
        
        self.lyricsTextEdit.clear()

        for line in lyrics.split("\n"):
            lyrics_converted = L_Edit.ConvertLyrics(line)
            self.lyricsTextEdit.append(lyrics_converted)
        
        self.editorCursor.movePosition(QTextCursor.Start)
        self.lyricsTextEdit.setTextCursor(self.editorCursor)

    
    """ functions about Player Control """
    def PlayStop(self):
        # Stop
        if self.nowplayng:
            self.playcontrol.Stop()
            self.nowplayng = False
            self.startEndButton.setText("Start Recording")
            startframe = self.playcontrol.LoopStart.GetFrame()
            endframe = self.playcontrol.LoopStop.GetFrame()
            currentframe = self.sys.LocalTime.GetFrame()

            # assume that startframe and endframe already setted
            self.playerSlider.setSliderPosition(int(100*currentframe/(endframe-startframe)))

        # Play
        else:
            # get cursor position at the time
            self.editorCursor = self.lyricsTextEdit.textCursor()

            self.playcontrol.Play()
            self.nowplayng = True
            self.startEndButton.setText("Recording ...")

    def ChangePlaySpeed(self, spinboxValue:float):
        # if isPlaying, change speed and restart
        if self.nowplayng:
            self.playcontrol.Stop()
            self.playcontrol.SetPlaySpeed(spinboxValue)
            self.playcontrol.Play()
            self.nowplayng = True
        else:
            self.playcontrol.SetPlaySpeed(spinboxValue)

    def PlayerSlide(self, sliderValue:int):
        # slider returns int : 0 ~ 100
        startframe = self.playcontrol.LoopStart.GetFrame()
        endframe = self.playcontrol.LoopStop.GetFrame()
        specified_frame_double = (endframe - startframe) * (sliderValue / 100)
        specified_frame = int(specified_frame_double)

        # restart if isPlaying
        if self.nowplayng:
            # set current frame (FBTime(0,0,0,specified frame))
            self.playcontrol.Goto(FBTime(0,0,0,specified_frame))
            self.playcontrol.Play()
            self.nowplayng = True
        else:
            self.playcontrol.Goto(FBTime(0,0,0,specified_frame))


    """ functions about Timetag """
    def AddKeyIn(self):
        # get click timing and lyrics character
        pressed_time = self.sys.LocalTime.GetSecondDouble()
        pressed_frame = pressed_time*(self.playcontrol.GetTransportFpsValue())
        key = self.editorCursor.document().characterAt(self.editorCursor.position())
        
        displaytext = key + "   "
        self.navigateTextEdit.ensureCursorVisible()
        self.navigateTextEdit.insertPlainText(displaytext)
        self.navigateTextEdit.insertPlainText(f"{pressed_frame:.4f}")
        
        # examine next lyrics character
        while True:
            # move cursor and store next character
            self.editorCursor.movePosition(QTextCursor.Right)
            nextkey = self.editorCursor.document().characterAt(self.editorCursor.position())
            
            # check if the next character is Hiragana
            if re.match(self.pattern, nextkey):
                break
            else:
                continue

    def AddKeyOut(self):
        released_time = self.sys.LocalTime.GetSecondDouble()
        released_frame = released_time*(self.playcontrol.GetTransportFpsValue())
        self.navigateTextEdit.insertPlainText("   ")
        self.navigateTextEdit.insertPlainText(f"{released_frame:.4f}")
        self.navigateTextEdit.insertPlainText("\n")

    # export timetag as .txt file
    def ExportTimetagText(self):
        cursor = self.navigateTextEdit.textCursor()
        cursor.select(QTextCursor.Document)
        timetags = cursor.selectedText()
        print(timetags)
        cursor.movePosition(QTextCursor.End)
        #cursor = self.navigateTextEdit.textCursor()