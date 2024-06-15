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

'''
# add module search path to the source directory
import sys,os,inspect
CurrentFilePath = inspect.currentframe().f_code.co_filename
CurrentDir = os.path.dirname(CurrentFilePath)
targetPath = os.path.join(CurrentDir,"timetagAnimator_Source")
sys.path.append(targetPath)
'''

from timetagAnimator_Source import UIdescription

# declare WidgetHolder class object
class WigHolder(FBWidgetHolder):
    def WidgetCreate(self, pWigParent):
        self.HoldedWidgetObject = UIdescription.HoldedWidget(wrapInstance(pWigParent,
                                                            QtWidgets.QWidget))
        return getCppPointer(self.HoldedWidgetObject)[0]
    

# declare main tool as FBTool 
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
        self.StartSizeX = 650
        self.StartSizeY = 500
        [self.MinSizeX, 
         self.MinSizeY, 
         self.MaxSizeX, 
         self.MaxSizeY] = [600, 400, 750, 600]
        

toolName = "timetagAnimator"

# Delete The Tool if exists
FBDestroyToolByName(toolName)

tool = WigTool(toolName)
FBAddTool(tool)
ShowTool(tool)