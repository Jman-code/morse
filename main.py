import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *


morse_code = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.", "!": "-.-.--",
    "/": "-..-.", "(": "-.--.", ")": "-.--.-", "&": ".-...", ":": "---...",
    ";": "-.-.-.", "=": "-...-", "+": ".-.-.", "-": "-....-", "_": "..--.-",
    "\"": ".-..-.", "$": "...-..-", "@": ".--.-.", " ": " "
}

def translator(text):
    text = text.upper()
    text = list(text)
    morse = [morse_code[char] for char in text if char in morse_code]
    return ' '.join(morse)


def delete():
    entry.delete(0, tk.END)
    morse.config(text='Waiting...')
def update_greeting(text):
    morse.config(text='Morse Code: ' + text)

def submit():
    text = entry.get()
    morse = translator(text)
    update_greeting(morse)

root = ttkb.Window(themename='cyborg')
root.title('Morse Code Fun!')
root.geometry('500x350')




greeting = ttkb.Label(root, text='Enter your Text Below',
                    padding=10,
                    bootstyle='info')
greeting.pack()

entry = ttkb.Entry(bootstyle='light', width=50)
entry.pack()
morse = ttkb.Label(root, text=' ', padding=20, font=42, bootstyle='danger')
morse.pack()
frm_buttons = ttkb.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
btn_submit= ttkb.Button(master=frm_buttons, text='Submit', command=submit, bootstyle='success')
btn_submit.pack(side=TOP, padx=10, ipadx=10)
btn_clear = ttkb.Button(master=frm_buttons, text='Clear', command=delete, bootstyle='warning')
btn_clear.pack(side=BOTTOM, ipadx=10)

root.mainloop()

