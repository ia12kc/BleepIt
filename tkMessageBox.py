from Tkinter import *

from ttk import Frame, Button, Notebook

from tkFileDialog import askopenfilename

import tkMessageBox


class BleepIt(Frame):
    def __init__(self, isapp=True, name='bleepit'):

        Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)
        self.master.title('BleepIt')
        self.isapp = isapp
        self._creat_top_panel()
        self._create_main_panel()

    def _creat_top_panel(self):

        ## Top frame

        topframe = Frame(self, relief=RAISED, borderwidth=1)
        topframe.pack(side=TOP, fill=X)

        label1 = Label(topframe, justify="left", text="BleepIt", font=('times', 20))
        label1.pack(fill=X)

    def _create_main_panel(self):

        mainPanel = Frame(self, name='main')
        mainPanel.pack(side=TOP, fill=BOTH, expand=Y)

        inpuPanel = Frame(mainPanel, name='input')
        inpuPanel.pack(side=TOP, fill=BOTH, expand=Y)

        ## File Selection

        bodyframe1 = Frame(inpuPanel, borderwidth=1, pad=5)
        bodyframe1.pack(expand=True, fill=X)

        pathlabel = Label(bodyframe1, bg="lightgrey", text="File: ", pady=1)
        pathlabel.pack(side=LEFT)

        # Selected file display
        self.path = Label(bodyframe1, bg="white", text="", width=40, padx=23, pady=1)
        self.path.pack(side=LEFT, fill=X, expand=True)

        # Browse
        browsebtn1 = Button(bodyframe1, text="Browse", command=self.buttonClick)
        browsebtn1.pack(side=RIGHT)

        ## Output format

        bodyframe3 = Frame(inpuPanel, borderwidth=1)
        bodyframe3.pack(expand=True, fill=X)

        typelabel = Label(bodyframe3, bg="lightgrey", text="Output Type: ", pady=1)
        typelabel.pack(side=LEFT)

        self.filetype = StringVar(bodyframe3)
        self.filetype.set("wav")

        options = OptionMenu(bodyframe3, self.filetype, "wav", "mp3")
        options.pack(side=LEFT, padx=30)

        trainbtn = Button(bodyframe3, text ="Train", command=self.trainButton)
        trainbtn.pack(side = RIGHT, padx = 5)

        ## Submit button section

        submitframe = Frame(inpuPanel, relief=RAISED, borderwidth=1)
        submitframe.pack(fill=X)

        cleanbtn = Button(submitframe, text="Clean", command=self.submitButton)
        cleanbtn.pack(padx=25, pady=10)


    # Browse Button
    def buttonClick(self):
        self.filename = askopenfilename()
        self.path.config(text=self.filename)

    # Submit Button
    def submitButton(self):
        try:
            print self.filename
            print self.filetype.get()
        except AttributeError:
            print "No file has beeen selected"

    # Train Button
    def trainButton(self):
        print("test")

if __name__ == '__main__':
    frame = BleepIt()
    frame.mainloop()