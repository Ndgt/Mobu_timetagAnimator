# -*- coding: utf-8

from pyfbsdk import FBMessageBox

# function to read txt file
def ReadLyrics(filename) -> str:
    f = open(filename, "r")
    data = f.readlines()
    return_string = ""
    for add_txt in data:
            return_string += add_txt
    f.close()
    return return_string


# function to convert QTextEdit strings 
# option: hiragana / alphabet
def ConvertLyrics(editortext:str) -> str:
    try:
        from pykakasi import kakasi
        kks = kakasi()
        return_hiragana_string = ""
        return_alphabet_string = ""

        str_converted = kks.convert(editortext)
        for item in str_converted:
            return_hiragana_string += item['hira']
        
        return return_hiragana_string

    except ImportError as err:
        FBMessageBox("Caution", "Error : module \"pykakasi\" is not installed \n Run \"mobupy -m pip install pykakasi\" in the Terminal as Administrator.", "OK")
        return err