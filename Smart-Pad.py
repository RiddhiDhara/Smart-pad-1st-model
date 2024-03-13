#>>>>>>>>>>>>>>>importing the package  
import language_tool_python 
#>>>>>>>>>>>>>>>DPI SETTING
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)
#>>>>>>>>>>>>>>>DICTIONARY
from PyDictionary import PyDictionary
dict = PyDictionary()
#>>>>>>>>>>>>>>>GOOGLE TRANSLATOR
from googletrans import Translator
#>>>>>>>>>>>>>>>SPEECH RECOGNITION
import speech_recognition as s_r
import os
#>>>>>>>>>>>>>>>TKINTER
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.ttk import *
from tkinter import *
import tkinter.messagebox
# ======================================================-> defining function
def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
    if not filepath:
        return
    txt1_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt1_edit.insert(tk.END, text)
    window.title(f"ENHANCED-TEXT-EDITOR [OPEN WINDOW] :-) - {filepath}")
# ------------------
def save_file():
    filepath = asksaveasfilename(
        defaultextension= "txt",
        filetypes = [("Text Files", "*.txt"), ("All Files", "*.*")]
        )
    if not filepath:
            return
    with open(filepath, "w") as output_file:
        text1 = txt1_edit.get(1.0, tk.END)
        text2 = txt1_edit.get(1.0, tk.END)
        output_file.write(text1)
    window.title(f"ENHANCED-TEXT-EDITOR [SAVE WINDOW] :-) - {filepath}")
# ------------------
def info_About_me():
   tkinter.messagebox.showinfo("INTRODUCTION :-]", "NAME : RIDDHI DHARA \nCOLLEGE : JISCE \nPROJECT TOPIC : PYTHON PROGRAMMING \nPROJECT NAME : ENHANCED-TEXT-EDITOR \nUNIVERSITY ROLL : 123211003113 \nCOLLEGE-ID : JIS/2021/0929 \n")
#-------------------
def info_translate():
   tkinter.messagebox.showinfo("LANGUAGE TRANSLATION :->", "OPTION AVAILABLE:========>>> \n1) ENGLISH :- translate to ENGLISH \n2) BENGALI :- translate to BENGALI \n3) HINDI :- translate to HINDI \n")
#-------------------
def clear_screen_1():
    txt1_edit.delete("1.0", "end")
#-------------------
def clear_screen_2():
    txt2_edit.delete("1.0", "end")
#-------------------
def voice_input():
        r = s_r.Recognizer()
        my_mic = s_r.Microphone(device_index=2)
        with my_mic as source:
            audio = r.listen(source)
        try:
            recorded_text = (r.recognize_google(audio), "\n")
            txt1_edit.insert(tk.END, recorded_text)
        except:
            txt2_edit.delete("1.0", "end")
            txt2_edit.insert(tk.END, "Sorry! TIME OUT :-(")
        
#------------------
def translate_to(text):
        lang_input = text
        lang_translate(lang_input)
#-----------------
def lang_translate(take_language):
        txt2_edit.delete("1.0", "end")
        sentence = txt1_edit.get(1.0, tk.END)
        translator = Translator()
        translation = translator.translate(sentence, dest=take_language)
        if translation.src == translation.dest:
            txt2_edit.insert(tk.END, "SOURCE language & TRANSLATED language is SAME!!!  :-|")
            txt2_edit.insert(tk.END, "\n")
        else:
            txt2_edit.insert(tk.END, translation)
            txt2_edit.insert(tk.END, "\n")
#------------------
def find_meaning():
        txt2_edit.delete("1.0", "end")
        selection = txt1_edit.get(tk.SEL_FIRST, tk.SEL_LAST)
        meaning = dict.meaning(selection)
        txt2_edit.insert(tk.END, selection + ":-------------------------------" + "\n")
        try:
            txt2_edit.insert(tk.END, meaning)
            txt2_edit.insert(tk.END, "\n")
        except:
            txt2_edit.insert(tk.END, "Sorry! DEFINITION not found :-(")
# -----------------
def correction():
    
        my_tool = language_tool_python.LanguageTool('en-US')  
        my_text = txt1_edit.get(1.0, tk.END) # given text    
        my_matches = my_tool.check(my_text)  # getting the matches
        myMistakes = []  # defining some variables 
        myCorrections = []  
        startPositions = []  
        endPositions = []  
        for rules in my_matches :                                          # using the for-loop  
            if len(rules.replacements) > 0 :
                startPositions.append(rules.offset)  
                endPositions.append(rules.errorLength + rules.offset)  
                myMistakes.append(my_text[rules.offset : rules.errorLength + rules.offset])  
                myCorrections.append(rules.replacements[0])  
        my_NewText = list(my_text)   # creating new object  
        for n in range(len(startPositions)):  # rewriting the correct passage  
            for i in range(len(my_text)):  
                my_NewText[startPositions[n]] = myCorrections[n]  
                if (i > startPositions[n] and i < endPositions[n]):  
                    my_NewText[i] = ""  
        my_NewText = "".join(my_NewText)
        try:   
            txt1_edit.delete("1.0", "end")
            txt1_edit.insert(tk.END, my_NewText)
            txt2_edit.delete("1.0", "end")
            txt2_edit.insert(tk.END, "Disclaimer: [Correction] may not give the Appropriate result" + "\n-----------------------------------------------------------------\n")
            txt2_edit.insert(tk.END, "CORRECTION:-" + "\n")
            txt2_edit.insert(tk.END, list(zip(myMistakes, myCorrections)))
            
        except:
            txt2_edit.insert(tk.END, "NO Correction needed!!!")
# -----------------
def MIC_INDEX_Window():
     
    newWindow = Toplevel(window)
    newWindow.title("DEVICE-INDEX :-] ")
    newWindow.rowconfigure(0, minsize=1000, weight=1)
    newWindow.columnconfigure(1, minsize=1000, weight=1)
    v=Scrollbar(newWindow, orient='vertical')
    v.pack(side=RIGHT, fill='y')
    txt=Text(newWindow, font=("Georgia, 10"), yscrollcommand=v.set)
    # ...............................................
    r = s_r.Microphone.list_microphone_names()
    j = 0
    for i in r:
        a = r[j]
        print(str(j) + ")->" + " " + a)
        txt.insert(END, str(j) + ")->" + " " + a + "\n")
        j = j+1
    # ...............................................
    v.config(command=txt.yview)
    txt.pack()
# ======================================================-> window structure
window = tk.Tk()
window.title("<<ENHANCED-TEXT EDITOR>>:-) ")
window.rowconfigure(1, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
# ======================================================-> textbox structure
txt1_edit = tk.Text(window, bg="dark grey", font=('Arial', 11), relief=tk.SUNKEN)
txt2_edit = tk.Text(window, bg="dark gray", font=('Courier New', 11, 'bold'), relief=tk.SUNKEN)
# ======================================================-> frame button structure
fr_button1 = tk.Frame(window, relief=tk.RAISED, bd=0)
fr_button2 = tk.Frame(window, relief=tk.RAISED, bd=0)
# ======================================================-> button properties
btn_AboutMe = tk.Button(fr_button1, text="About Creator", bg='light blue', command=info_About_me)
btn_open = tk.Button(fr_button1, text="Open", bg='light gray', command=open_file)
btn_save = tk.Button(fr_button1, text="Save_As", bg='light gray', command=save_file)
btn_mic = tk.Button(fr_button1, text="Mic_Index", bg='light gray', command=MIC_INDEX_Window)
btn_voice_input = tk.Button(fr_button1, text="Voice Text", bg='light gray', command=voice_input)
btn_definition = tk.Button(fr_button1, text="Definition", bg='light gray', command=find_meaning)
btn_correction = tk.Button(fr_button1, text="Correction", bg='light gray', command=correction)
btn_clear_1 = tk.Button(fr_button1, text="Clear", bg='sky blue', command=clear_screen_1)
btn_translate = tk.Button(fr_button2, text="Translate", bg='light blue', command=info_translate)
btn_ENGLISH = tk.Button(fr_button2, text="ENGLISH", bg='light gray', command=lambda:translate_to("en"))
btn_BENGALI = tk.Button(fr_button2, text="BENGALI", bg='light gray', command=lambda:translate_to("bn"))
btn_HINDI = tk.Button(fr_button2, text="HINDI", bg='light gray', command=lambda:translate_to("hi"))
btn_clear_2 = tk.Button(fr_button2, text="Clear", bg='sky blue', command=clear_screen_2)
# ======================================================-> button grid
btn_AboutMe.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_open.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_mic.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
btn_voice_input.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
btn_definition.grid(row=5, column=0, sticky="ew", padx=5, pady=5)
btn_correction.grid(row=6, column=0, sticky="ew", padx=5, pady=5)
btn_clear_1.grid(row=7, column=0, sticky='ew', padx=5, pady=5)
btn_translate.grid(row=8, column=0, sticky="ew", padx=5, pady=5)
btn_ENGLISH.grid(row=9, column=0, sticky="ew", padx=5, pady=5)
btn_BENGALI.grid(row=10, column=0, sticky="ew", padx=5, pady=5)
btn_HINDI.grid(row=11, column=0, sticky="ew", padx=5, pady=5)
btn_clear_2.grid(row=12, column=0, sticky='ew', padx=5, pady=5)
# ===============-> frame window grid
fr_button1.grid(row=0, column=0, sticky="ns")
fr_button2.grid(row=1, column=0, sticky="ns")
txt1_edit.grid(row=0, column=1, sticky="new")
txt2_edit.grid(row=1, column=1, sticky="new")
# ===============-> window END
window.mainloop()
#-------------------------------END--------------------------------------------



        # my_tool = language_tool_python.LanguageTool('en-US')  
        # my_text = txt1_edit.get(1.0, tk.END)  
        # my_correction = my_tool.correct(my_text)
        # if my_text == my_correction :
        #     txt1_edit.delete("1.0", "end")
        #     txt1_edit.insert(tk.END, my_correction)
        # else :
        #     txt2_edit.delete("1.0", "end")
        #     txt2_edit.insert(tk.END, "NO CORRECTION needed!!! :-/")