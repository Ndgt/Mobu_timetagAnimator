# if vsq file selected
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

    # list to store sounds
    soundlist = list()

    # list to store 4 timetags 
    timetaglist = [list(),list(),list(),list()]

    file = open(filename, "rb")
    data = file.readlines()

    # define target to omit certain bytes
    target1 = b"\x00\xff\x01\x7fDM:"
    target2 = b"\x00\xff\x011DM:"
    target3 = b"\x00\xff/\x00"

    # counter to change read mode
    count = 0

    for i in data:
        # end of vsq file
        if i == target3:
            break

        [idx1, idx2] = [i.find(target1), i.find(target2)]
        if not idx1 == -1:
            omitbyte = i[idx1:idx1+12]
        if not idx2 == -1:
            omitbyte = i[idx2:idx2+12]
        
        # omit certain bytes and decode 
        line = i.replace(omitbyte,b"").decode("utf_8", "ignore").strip()
        
        # extract "Yomi"
        if count == 3 and line.find("[h#") == -1:
            idx = line.find(",1")
            line = line[idx - 2]
            if line == "M":
                line = "u"
            soundlist.append(line)      
            
        # count 3: start of "Yomi" line
        if count == 2 and line == "[h#0001]":
            count = 3
        
        # count 2: end of EventList
        if line == "[ID#0000]":
            count = 2
            
        # extract and calculate timetags
        if count == 1:
            idx = line.find("=")
            line = line[0:idx]
            if not line == "0":
                sframe = int(line)/1.2/1000 * fps
                timetaglist[2].append(int(sframe - (fps/30) -(fps/15)))
                timetaglist[3].append(int(sframe - (fps/30)))
                timetaglist[0].append(int(sframe - (fps/15)))
                timetaglist[1].append(int(sframe))

        # count 1: start of EventList
        if line == "[EventList]":
            count = 1

    # for last Key
    timetaglist[2].append(int(sframe + (fps/30) + (fps/15)))
    timetaglist[3].append(int(sframe + (fps/30)))
    
    result = 0
    for j in range(len(timetaglist[0])):    
        if soundlist[j] in vowel:
            KeyInput(soundlist[j], startframe, timetaglist[0][j],timetaglist[1][j],timetaglist[2][j+1],timetaglist[3][j+1])
            result += 1
    return result