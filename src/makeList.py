import pyfbsdk
from pyfbsdk import*
from pyfbsdk_additions import*

"""
ReturnList(option) : 
 function to return List depending on option below.
 1. Allshapekey -> return List of all shapekey which will be used for user selection in UI
 2. shapename -> return List of models which has specified shapekey 
"""

def ReturnList(option): # Allshapekey/shapename
    OutputList = list()
    
    def ExamineAllObjects(model):
        if len(model.Children) > 0:
            for child in model.Children:
                if type(child) == pyfbsdk.FBModel:
                    geo = child.Geometry
                    for i in range(geo.ShapeGetCount()):
                        name = geo.ShapeGetName(i)
                        
                        # for SKListForUserSelect
                        if option == "Allshapekey": 
                            if not name in OutputList:
                                OutputList.append(name)
                
                        # for vowelSKcontainModelList
                        if name == option:
                            OutputList.append(child.Name)
                            break

                ExamineAllObjects(child)
    
    ExamineAllObjects(FBSystem().Scene.RootModel)        
    return OutputList