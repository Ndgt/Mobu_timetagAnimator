from pyfbsdk import*
from pyfbsdk_additions import*

try:
    from PySide6 import QtWidgets
except:
    from PySide2 import QtWidgets

from UIdiscriptionUI import Ui_ToolWindow

import makeList
import readvsq
import readlab

class HoldedWidget(QtWidgets.QWidget, Ui_ToolWindow):
    def __init__(self, pWigholder):
        super().__init__(pWigholder)
        self.setupUi(self)
        
        self.vowel = ["a","i","u","e","o"] 
        self.vowelSKcontainModelList = [list(),list(),list(),list(),list()]
        self.shapeList = makeList.ReturnList("Allshapekey")
        
        self.comboBox_1.addItem("select shapekey for phoneme : a")
        self.comboBox_2.addItem("select shapekey for phoneme : i")
        self.comboBox_3.addItem("select shapekey for phoneme : u")
        self.comboBox_4.addItem("select shapekey for phoneme : e")
        self.comboBox_5.addItem("select shapekey for phoneme : o")       
           
        for name in self.shapeList:
            self.comboBox_1.addItem(name)
            self.comboBox_2.addItem(name)
            self.comboBox_3.addItem(name)
            self.comboBox_4.addItem(name)
            self.comboBox_5.addItem(name)

    def SelectFile(self):
        # check if Audio file exists in Story
        self.storyAudiocheck = False
        for track in FBStory().RootFolder.Tracks:
            if track.Type == FBStoryTrackType.kFBStoryTrackAudio:
                if len(track.Clips) > 0:
                    self.storyAudiocheck = True
                    self.startFrame = track.Clips[0].Start.GetFrame()

        if self.storyAudiocheck:
            self.UserSelectedvowelSKList = [self.comboBox_1.currentText(),
                                            self.comboBox_2.currentText(),
                                            self.comboBox_3.currentText(),
                                            self.comboBox_4.currentText(),
                                            self.comboBox_5.currentText()]  
            for i in range(5):
                self.vowelSKcontainModelList[i] = makeList.ReturnList(self.UserSelectedvowelSKList[i]) 
            
            self.popup = FBFilePopup()
            self.popup.Caption = "Select a file"
            self.popup.Style = FBFilePopupStyle.kFBFilePopupOpen   
            self.popup.Filter = "*"
            
            self.check = self.popup.Execute()
            self.fps = FBPlayerControl().GetTransportFpsValue()
            
            if self.check:
                if self.popup.FileName[-4:] == ".vsq":
                    self.result = readvsq.addKeys(self.popup.FileName,
                                                    self.startFrame,
                                                    self.fps,
                                                    self.vowelSKcontainModelList,
                                                    self.UserSelectedvowelSKList)
                    
                elif self.popup.FileName[-4:] == ".lab":
                    self.result = readlab.addKeys(self.popup.FileName,
                                                    self.startFrame,
                                                    self.fps,
                                                    self.vowelSKcontainModelList,
                                                    self.UserSelectedvowelSKList)
                else:
                    FBMessageBox("Caution","Error : Selected file is not vsq or lab file.","OK")
                
                if not self.result == 0:
                    FBMessageBox(self.popup.FileName + "was selected", str(self.result) + " timetags applied successfully in " + str(self.fps) + " fps", "OK")
                    makegroup = FBMessageBox("message", "Make Group for each shapekey ?", "Yes", "No")
                    if makegroup == 1:
                        for i in range(5):
                            group = FBGroup("shapekey : " + self.UserSelectedvowelSKList[i])
                            for j in self.vowelSKcontainModelList[i]:
                                model = FBFindModelByLabelName(j)
                                group.ConnectSrc(model)
                else:
                    FBMessageBox("Caution","Error : Failed to apply keys for some reasons","OK")
        else:
            FBMessageBox("No Audio file found", "Import Audio file into Story", "OK")