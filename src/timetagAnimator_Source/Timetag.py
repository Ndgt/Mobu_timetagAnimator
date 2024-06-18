'''
Do not forget writing commma ","
'''

from pyfbsdk import*
import re

# characters to leave when hitting timetag
str_leave = [
    # small "a" ~ "o"
    b'\\u3041',
    b'\\u3043',
    b'\\u3045',
    b'\\u3047',
    b'\\u3049',

    # small "ya" ~ "yo"
    b'\\u3083',
    b'\\u3085',
    b'\\u3087',

    # small "tu"
    b'\\u3063',

    # small "wa"
    b'\\u308e',

    # "n / mouth close"
    b'\\u3093',
]

# characters correspond to vowel "a"
str_a = [
    "a",
    b'\\u3041', b'\\u3042',
    b'\\u304b', b'\\u304c',
    b'\\u3055', b'\\u3056',
    b'\\u305f', b'\\u3060',
    b'\\u306a',
    b'\\u306f', b'\\u3070', b'\\u3071',
    b'\\u307e',
    b'\\u3083', b'\\u3084',
    b'\\u3089',
    b'\\u308e', b'\\u308f',
]

# characters correspond to vowel "i"
str_i = [
    "i",
    b'\\u3043', b'\\u3044',
    b'\\u304d', b'\\u304e',
    b'\\u3057', b'\\u3058',
    b'\\u3061', b'\\u3062',
    b'\\u306b',
    b'\\u3072', b'\\u3073', b'\\u3074',
    b'\\u307f',
    b'\\u308a',
    b'\\u3090',
]

# characters correspond to vowel "u"
str_u = [
    "u",
    b'\\u3045', b'\\u3046',
    b'\\u304f', b'\\u3050',
    b'\\u3059', b'\\u305a',
    b'\\u3063', b'\\u3064',
    b'\\u306c',
    b'\\u3075', b'\\u3076', b'\\u3077',
    b'\\u3080',
    b'\\u3085', b'\\u3086',
    b'\\u308b',
    b'\\u3094',
]

# characters correspond to vowel "e"
str_e = [
    "e",
    b'\\u3047', b'\\u3048',
    b'\\u3051', b'\\u3052',
    b'\\u305b', b'\\u305c',
    b'\\u3066', b'\\u3067',
    b'\\u306d',
    b'\\u3078', b'\\u3079', b'\\u307a',
    b'\\u3081',
    b'\\u308c',
    b'\\u3091',
]

# characters correspond to vowel "o"
str_o = [
    "o",
    b'\\u3049', b'\\u304a',
    b'\\u3053', b'\\u3054',
    b'\\u305d', b'\\u305e',
    b'\\u3068', b'\\u3069',
    b'\\u306e',
    b'\\u307b', b'\\u307c', b'\\u307d',
    b'\\u3082',
    b'\\u3087', b'\\u3088',
    b'\\u308d',
    b'\\u3092',
]


hiraSound = [str_a, str_i, str_u, str_e, str_o]

# return corresponding sound
def sound(key : str) -> str:
    for strList in hiraSound:
        if key.encode("unicode-escape") in strList:
            return  strList[0]
    
    else:
        return "error"
    

# default value to each timetag
keyAddValue = {
    "a" : 70, 
    "i" : 60,
    "u" : 100,
    "e" : 80,
    "o" : 100,
}


# add animation key
def KeyInput(model:FBModel, shapekeyList:list, pressframeList:list, releaseframeList:list):
    for i in range(len(shapekeyList)):
        prop = model.PropertyList.Find(shapekeyList[i]) 
        if prop != None:
            if prop.IsAnimated() == False:
                prop.SetAnimated(True)
            pCurve = prop.GetAnimationNode().FCurve
            pCurve.KeyAdd(FBTime(0,0,0,int(pressframeList[i]) - 5), 0,
                          FBInterpolation.kFBInterpolationCubic,
                           FBTangentMode.kFBTangentModeClampProgressive)
            pCurve.KeyAdd(FBTime(0,0,0,int(pressframeList[i])), keyAddValue[prop.Name],
                          FBInterpolation.kFBInterpolationCubic,
                          FBTangentMode.kFBTangentModeClampProgressive)
            pCurve.KeyAdd(FBTime(0,0,0,int(releaseframeList[i])), keyAddValue[prop.Name],
                          FBInterpolation.kFBInterpolationCubic,
                          FBTangentMode.kFBTangentModeClampProgressive)
            pCurve.KeyAdd(FBTime(0,0,0,int(releaseframeList[i] + 5)), 0,
                          FBInterpolation.kFBInterpolationCubic,
                          FBTangentMode.kFBTangentModeClampProgressive)