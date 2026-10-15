import random

from translate import Translator
from random import randint
translator = Translator(to_lang="ja")

def convert(text):
    translation = translator.translate(f"{text}")
    return translation

def convertfile(filename):
    with open(f"{filename}.txt", "r", encoding= "utf-8") as docu:
        randomname = f"newfile{random.randint(0,10)}"
        newfile = open(f"{randomname}.txt","a+")
        for line in docu:
            translated_line = convert(line)
            newfile.write(translated_line + "\n")

