import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk



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

def update_greeting(text):
    greeting.config(text='Morse Code: ' + text)

def submit():
    text = entry.get()
    morse = translator(text)
    update_greeting(morse)



window = tk.Tk()

frame = tk.Frame(bg='grey')
frame.pack()
greeting = tk.Label(master=frame, text='Enter your Text Below',
                    width=50,
                    height=25,
                    fg='skyblue',
                    bg='grey')
greeting.pack()

entry = tk.Entry(fg='black', bg='crimson', width=50)
entry.pack()

frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
btn_submit= tk.Button(master=frm_buttons, text='Submit', command=submit)
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)
btn_clear = tk.Button(master=frm_buttons, text='Clear', command=delete)
btn_clear.pack(side=tk.RIGHT, ipadx=10)

window.mainloop()

