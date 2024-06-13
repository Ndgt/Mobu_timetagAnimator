from pyfbsdk import*
from pyfbsdk_additions import*

try:
    from PySide6 import QtWidgets
    from PySide6.QtGui import QTextCursor, QMouseEvent
except:
    from PySide2 import QtWidgets
    from PySide2.QtGui import QTextCursor, QKeyEvent

from ui_timetagAnimator import Ui_toolWindow

import L_Edit

class HoldedWidget(QtWidgets.QWidget, Ui_toolWindow):
    def __init__(self, pWigholder):
        super().__init__(pWigholder)
        self.setupUi(self)

        """
        about charaCombobox
        """
        # system event
        self.sys = FBSystem()
        self.app = FBApplication()
        self.sys.OnConnectionDataNotify.Add(self.charaComboUpdate)
        self.app.OnFileExit.Add(self.DataNotifyRemove)
        
        # setup the content 
        self.charaComboBox.addItem("character not selected")
        for chara in self.sys.Scene.Characters:
            self.charaComboBox.addItem(chara.Name)
        # connect signal with charaComboBox
        self.charaComboBox.currentIndexChanged.connect(self.updateComboBoxes)


        """
        about shapekey comboboxes
        """
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

        self.shapeList = self.ReturnCharaShape()

        if not self.shapeList is None:
           for name in self.shapeList:
                for cbox in self.comboboxes:
                    cbox.addItem(name)


        """
        about player control
        """
        self.playcontrol = FBPlayerControl()
        self.startframe = self.playcontrol.LoopStart.GetFrame()
        self.endframe = self.playcontrol.LoopStop.GetFrame()


        self.editorCursor = self.lyricsTextEdit.textCursor()

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


    '''
    Lyrics Edit methods
    '''
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
                for line in lyrics.split("\n"):
                    self.lyricsTextEdit.append(line)
            else:
                FBMessageBox("Caution","Error : Selected file is not text file.","OK")

            # focus on the start
            self.editorCursor.movePosition(QTextCursor.Start)
            self.lyricsTextEdit.setTextCursor(self.editorCursor)


    def ConvertHiragana(self):
        lyrics_converted = L_Edit.ConvertLyrics(self.lyricsTextEdit.toPlainText(),"hiragana")
        if not type(lyrics_converted) == ModuleNotFoundError:
            self.lyricsTextEdit.clear()

            for line in lyrics_converted.split("\n"):
                self.lyricsTextEdit.append(line)

            # focus on the start
            self.editorCursor.movePosition(QTextCursor.Start)
            self.lyricsTextEdit.setTextCursor(self.editorCursor)

    def ConvertAlphabet(self):
        lyrics_converted = L_Edit.ConvertLyrics(self.lyricsTextEdit.toPlainText(),"alphabet")
        if not type(lyrics_converted) == ModuleNotFoundError:
            self.lyricsTextEdit.clear()
            # set vowel list
            vowels = ["a","i","u","e","o"]
            for line in lyrics_converted.split("\n"):
                finalline = " "
                # omit consonant from line
                for char in line:
                    finalline += char
                    # split line with a slash for each vowerl
                    if char in vowels:
                        finalline += "/"                
                self.lyricsTextEdit.append(finalline) 
        
            # focus on the start
            self.editorCursor.movePosition(QTextCursor.Start)
            self.lyricsTextEdit.setTextCursor(self.editorCursor)
    
    """
    Player Control functions
    """
    def PlayStop(self):
        if self.playcontrol.IsPlaying or self.playcontrol.GetEditCurrentTime() == self.playcontrol.LoopStop:
            self.playcontrol.Stop()
            self.startEndButton.setText("Start Recording")

        else:
            # get cursor position at the time
            self.editorCursor = self.lyricsTextEdit.textCursor()

            self.playcontrol.Play()
            self.startEndButton.setText("Recording ...")

    def ChangePlaySpeed(self, spinboxValue:float):
        # if isPlaying, change speed and restart
        if self.playcontrol.IsPlaying:
            self.playcontrol.Stop()
            self.playcontrol.SetPlaySpeed(spinboxValue)
            self.playcontrol.Play()
        else:
            self.playcontrol.SetPlaySpeed(spinboxValue)

    def PlayerSlide(self, sliderValue:int):
        # slider returns int : 0 ~ 99
        specified_frame_double = (self.endframe - self.startframe) * (sliderValue / 100)
        specified_frame = int(specified_frame_double)

        # restart if isPlaying
        if self.playcontrol.IsPlaying:
            # set current frame (FBTime(0,0,0,specified frame))
            self.playcontrol.Goto(FBTime(0,0,0,specified_frame))
            self.playcontrol.Play()
        else:
            self.playcontrol.Goto(FBTime(0,0,0,specified_frame))



    """
    Add Key functions
    """
    def AddKeyIn(self):
        pressed_time = self.sys.LocalTime.GetSecondDouble()
        pressed_frame = pressed_time*(self.playcontrol.GetTransportFpsValue())

        key = self.editorCursor.document().characterAt(self.editorCursor.position())
        
        self.navigateTextEdit.append(key)
        self.navigateTextEdit.insertPlainText("   ")
        self.navigateTextEdit.insertPlainText(f"{pressed_frame:.4f}")
        
        counter = 1
        while True:
            self.editorCursor.movePosition(QTextCursor.Right)
            nextkey = self.editorCursor.document().characterAt(self.editorCursor.position())
            check = nextkey.encode("shift-jis","replace")
            if check == b'?':
                counter += 1
                continue
            else:
                break

    def AddKeyOut(self):
        released_time = self.sys.LocalTime.GetSecondDouble()
        released_frame = released_time*(self.playcontrol.GetTransportFpsValue())
        self.navigateTextEdit.insertPlainText("   ")
        self.navigateTextEdit.insertPlainText(f"{released_frame:.4f}")


    """
    Export Timetag functions
    """
    def ExportTimetagText(self):
        cursor = self.navigateTextEdit.textCursor()
        cursor.select(QTextCursor.Document)
        timetags = cursor.selectedText()
        print(type(timetags))
        print(timetags)
        cursor.movePosition(QTextCursor.End)
        #cursor = self.navigateTextEdit.textCursor()