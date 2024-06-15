# -*- coding: utf-8

from pyfbsdk import FBMessageBox

# function to read txt file
def ReadLyrics(filename) -> str:
    try:
        with open(filename, "r", encoding = "utf-8") as file:
            data = file.readlines()
            return_string = ""
            for add_txt in data:
                return_string += add_txt

            return return_string

    except UnicodeDecodeError as err:
        FBMessageBox("Caution", str(err) + "\n" \
                        + "Make sure that the lyrics file saved with UTF-8 codec.", "OK")
        return err


# function to convert QTextEdit strings 
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