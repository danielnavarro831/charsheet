from tkinter import *
import openpyxl


class charSheet:
    def __init__(self):
        self.version = "0.01"
        self.app = Tk()
        self.app.resizable(False, False)
        self.app.title("D&D Character Sheet")

        self.version_label = Label(self.app, text="Ver: " + self.version + " ", bd=1, relief=SUNKEN, anchor=E)
        self.menu = Menu(self.app)
        self.app.config(menu=self.menu)
        self.file_menu = Menu(self.menu)
        self.file_menu.add_command(label="Exit", command=self.app.quit)
        self.menu.add_cascade(label="File", menu=self.file_menu)

        self.version_label.grid(row=1, column=0, columnspan=2, sticky=W + E)
        self.app.mainloop()


test = charSheet()
