import sys
from tkinter import *

if sys.platform == 'win32':
    import winsound
    def beep(frequency, duration):
        winsound.Beep(frequency, duration)
else:
    def beep(frequency, duration):
        pass

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.title("String Search Tool")

        Label(self.root, text="Strings to search for, one per line:").pack(fill=BOTH,)
        self.searchbox = Text(self.root)
        self.searchbox.pack()

        Label(self.root, text="Type or scan here to search:").pack(fill=BOTH)
        self.entry = Entry(self.root)
        self.entry.bind("<Return>", self.search)
        self.entry.pack()
        
        self.status = Label(self.root, text="Ready to search.", font=('', 16))
        self.status.pack(fill=BOTH)
        
    def search(self, event):
        strings = self.searchbox.get('0.0', END).split()
        entry = self.entry.get()
        self.entry.delete(0, END)
        if entry in strings:
            self.status.config(fg="green", text="Matches: " + entry)
            for m in range(1,4): beep(m * 440, 100)

        else:
            self.status.config(fg="red", text="No match.")
            beep(880, 50)
            beep(660, 50)
            
main = Main()
main.root.mainloop()
