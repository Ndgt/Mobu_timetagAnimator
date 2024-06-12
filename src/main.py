from pyfbsdk import*
from pyfbsdk_additions import*

# for MotionBuilder 2025
try:
    from PySide6 import QtWidgets
    from shiboken6 import wrapInstance, getCppPointer

# for MotionBuilder -2024
except:
    from PySide2 import QtWidgets
    from shiboken2 import wrapInstance, getCppPointer

# get file path for module import 
import sys, os, inspect
CurrentFilePath = inspect.currentframe().f_code.co_filename
sys.path.append(os.path.dirname(CurrentFilePath))

import UIdescription

# declare WidgetHolder class object
class WigHolder(FBWidgetHolder):
    def WidgetCreate(self, pWigParent):
        self.HoldedWidgetObject = UIdescription.HoldedWidget(wrapInstance(pWigParent,
                                                             QtWidgets.QWidget))
        return getCppPointer(self.HoldedWidgetObject)[0]
    

# declare as FBTool 
class WigTool(FBTool):
    def PopulateLayout(self):
        x = FBAddRegionParam(0, FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(0, FBAttachType.kFBAttachTop,"")
        w = FBAddRegionParam(0, FBAttachType.kFBAttachRight,"")
        h = FBAddRegionParam(0, FBAttachType.kFBAttachBottom,"")
        self.AddRegion("mainLayout", "timetagAnimatorWidget", x,y,w,h)
        self.SetControl("mainLayout", self.WigHolderObject)

    def __init__(self,name):
        super().__init__(name)
        self.WigHolderObject = WigHolder()
        self.PopulateLayout()
        self.StartSizeX = 750
        self.StartSizeY = 460
        

toolName = "timetagAnimator"

# Delete The Tool if exists
FBDestroyToolByName(toolName)

tool = WigTool(toolName)
FBAddTool(tool)
ShowTool(tool)