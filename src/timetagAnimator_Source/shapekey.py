from pyfbsdk import*

# return All shapekey name in character user selected
def All(chara:FBCharacter) -> list:
    if chara is None:
        return None
    
    else:
        mList = FBModelList
        returnList = []
        chara.GetSkinModelList(mList)
        for mesh in mList:
            geo = mesh.Geometry
            for i in range(geo.ShapeGetCount()):
                name = geo.ShapeGetName(i)
                if not name in returnList:
                    returnList.append(name)
        return returnList
    
'''
# return All model which have all shapekey user selected
def Model(shapekey:str) -> list:
'''