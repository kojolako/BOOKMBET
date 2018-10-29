import telegram
from tkinter import *



def main():
    telegram.writetofilelastmassages("LASTDATA")
    root = Tk()
    root.title("Графическая программа на Python")
    root.geometry("400x300")

    root.mainloop()

main()


