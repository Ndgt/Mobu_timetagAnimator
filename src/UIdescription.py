from pyfbsdk import*
from pyfbsdk_additions import*

try:
    from PySide6 import QtWidgets
except:
    from PySide2 import QtWidgets

from ui_timetagAnimator import Ui_toolWindow

import makeList
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

        self.shapeList = makeList.ReturnList("Allshapekey")

        for name in self.shapeList:
            for cbox in self.comboboxes:
                cbox.addItem(name)


        """
        about player control
        """
        self.playcontrol = FBPlayerControl()
        self.startframe = self.playcontrol.LoopStart.GetFrame()
        self.endframe = self.playcontrol.LoopStop.GetFrame()


    def AddDataNotify(self):
        self.charaComboUpdate()

    def DataNotifyRemove(self):
        self.sys.OnConnectionDataNotify.Remove(self.AddDataNotify)

    def charaComboUpdate(self,control,event):
        items = [self.charaComboBox.itemText(i) for i in range(1,self.charaComboBox.count())] 
        for chara in FBSystem().Scene.Characters:
            if not chara is None:
                if not chara.Name in items:
                    self.charaComboBox.addItem(chara.Name)


    # return All shapekey name in character user selected
    def ReturnCharaShape(self) -> list:
        mList = FBModelList()
        returnList = []
        # get current selected character
        chara = FBSystem().Scene.Characters.__getitem__(self.charaComboBox.currentIndex()-1)
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
            for shapekey in self.ReturnCharaShape():
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
            cursor = self.lyricsTextEdit.textCursor()
            cursor.movePosition(cursor.atStart)
            self.lyricsTextEdit.setTextCursor(cursor)
            self.lyricsTextEdit.setFocus()

    def ConvertText(self):
        lyrics_converted = L_Edit.ConvertLyrics(self.lyricsTextEdit.toPlainText(),"hiragana")
        if not type(lyrics_converted) == ModuleNotFoundError:
            self.lyricsTextEdit.clear()

            for line in lyrics_converted.split("\n"):
                self.lyricsTextEdit.append(line)

            # focus on the start
            cursor = self.lyricsTextEdit.textCursor()
            cursor.movePosition(cursor.atStart)
            self.lyricsTextEdit.setTextCursor(cursor)
            self.lyricsTextEdit.setFocus()


    def SplitText(self):
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
            cursor = self.lyricsTextEdit.textCursor()
            cursor.movePosition(cursor.atStart)
            self.lyricsTextEdit.setTextCursor(cursor)
            self.lyricsTextEdit.setFocus()




    
    """
    Player Control functions
    """
    def StartEnd(self):
        if self.playcontrol.IsPlaying:
            self.playcontrol.Stop()
            self.startEndButton.setText("Start Recording")
        else:
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
    Music Import functions
    """