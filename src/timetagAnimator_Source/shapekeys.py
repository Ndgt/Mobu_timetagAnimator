from pyfbsdk import*

# return All shapekey name in character user selected
def All(chara:FBCharacter) -> list:
    if chara is None:
        return None
    
    else:
        mList = FBModelList()
        returnList = []
        chara.GetSkinModelList(mList)
        for mesh in mList:
            geo = mesh.Geometry
            for i in range(geo.ShapeGetCount()):
                name = geo.ShapeGetName(i)
                if not name in returnList:
                    returnList.append(name)
        return returnList


# return and animate All model which have all shapekey user selected
def Model(chara:FBCharacter, shapekey:str) -> list:
    mList = []
    for mesh in chara.GetSkinModelList():
        prop = mesh.PropertyList.Find(shapekey)
        if prop != None:
            mList.append(mesh)

            # animate the shapekey
            if prop.IsAnimated() == False:
                prop.SetAnimated(True)

    returnList = [shapekey, mList]
    return returnList        