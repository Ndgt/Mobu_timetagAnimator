# if lab file selected
#

from pyfbsdk import*

def addKeys(filename, startframe, fps, mlist, slist):
    # holder for error log
    result = 0
    vowel = ["a", "i", "u", "e", "o"]

    def KeyInput(sound, startframe, s0frame,sframe,eframe,e0frame):
        i = vowel.index(sound)
        for modelName in mlist[i]:
            model = FBFindModelByLabelName(modelName)

            SKprop = model.PropertyList.Find(slist[i])
            if SKprop.IsAnimated() == False:
                SKprop.SetAnimated(True)
            pCurve = SKprop.GetAnimationNode().FCurve
            pCurve.KeyAdd(FBTime(0,0,0,startframe + s0frame),0,FBInterpolation.kFBInterpolationCubic,FBTangentMode.kFBTangentModeClampProgressive)
            pCurve.KeyAdd(FBTime(0,0,0,startframe + sframe),100,FBInterpolation.kFBInterpolationCubic,FBTangentMode.kFBTangentModeClampProgressive)
            pCurve.KeyAdd(FBTime(0,0,0,startframe + eframe),100,FBInterpolation.kFBInterpolationCubic,FBTangentMode.kFBTangentModeClampProgressive)
            pCurve.KeyAdd(FBTime(0,0,0,startframe + e0frame),0,FBInterpolation.kFBInterpolationCubic,FBTangentMode.kFBTangentModeClampProgressive)

    file = open(filename, "r", encoding = "UTF-8-sig")
    timetags = file.readlines()

    for data in timetags:
        timetaglist = data.strip("\n").split(" ")
        sound = timetaglist[2]
        
        if sound in vowel:          
            sframe = int(timetaglist[0])/10000000*fps
            s0frame = sframe - (fps/15)
            e0frame = int(timetaglist[1])/10000000*fps
            eframe = e0frame - (fps/15)
            
            KeyInput(sound ,startframe, int(s0frame),int(sframe),int(eframe),int(e0frame))
            result += 1
    return result