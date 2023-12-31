from pathlib import Path
from itertools import cycle
import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from PIL import Image, ImageTk, ImageSequence


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

class AnimatedGif(ttkb.Frame):
    def __init__(self, master):
        super().__init__(master, width=400, height=300)

        # open the GIF and create a cycle iterator
        file_path = Path(__file__).parent / "rotating_gif.gif"
        with Image.open(file_path) as im:
            # create a sequence
            sequence = ImageSequence.Iterator(im)
            images = [ImageTk.PhotoImage(s) for s in sequence]
            self.image_cycle = cycle(images)

            # length of each frame
            self.framerate = im.info["duration"]

        self.img_container = ttk.Label(self, image=next(self.image_cycle))
        self.img_container.pack(fill="both", expand="yes")
        self.after(self.framerate, self.next_frame)

    def next_frame(self):
        """Update the image for each frame"""
        self.img_container.configure(image=next(self.image_cycle))
        self.after(self.framerate, self.next_frame)

def translator(text):
    text = text.upper()
    text = list(text)
    morse = [morse_code[char] for char in text if char in morse_code]
    return ' '.join(morse)


def delete():
    entry.delete(0, tk.END)
    morse.config(text='Waiting....')
def update_greeting(text):
    morse.config(text='Morse Code: ' + text)

def submit():
    text = entry.get()
    morse = translator(text)
    update_greeting(morse)

def update_progress(*args):  # args is needed as this is a callback from a trace
    text_len = len(entry_str.get())
    bar['value'] = (text_len / 20) * 100

root = ttkb.Window(themename='solar')
root.title('Morse Code Fun!')
root.geometry('600x600')

gif = AnimatedGif(root)
gif.pack(fill=BOTH, expand=YES, padx=100)


greeting = ttkb.Label(root, text='Enter your Text Below',
                    padding=10,
                    bootstyle='info')
greeting.pack()

bar = ttkb.Progressbar(bootstyle='info')
bar.pack(side=TOP)

entry_str = StringVar()
entry_str.trace("w", update_progress)


entry = ttkb.Entry(bootstyle='light', width=50, textvariable=entry_str)
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

