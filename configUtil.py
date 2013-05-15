#!/usr/bin/env python

# To change this template, choose Tools | Templates
# and open the template in the editor.

from Tkinter import *
from sys import exit as closeProgram

class ConfigUtility(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def saveAndExit(self):
        with open("dualbrowser.cfg", "w") as cfg:
            if self.prefer == True:
                cfg.write("prefer=1\n")
            else:
                cfg.write("prefer=0\n")
            cfg.write("choice=" + self.choice.lower() + "\n")
            cfg.write("reason=" + self.reason + "\n")
            closeProgram()

    def createWidgets(self):
        try:
            with open("dualbrowser.cfg") as cfg:
                for line in cfg:
                    config = line.strip().split("=")
                    if config[0] == "prefer":
                        if config[1] == "1":
                            self.prefer = True
                        else:
                            self.prefer = False
                    elif config[0] == "choice":
                            self.choice = config[1]
                    elif config[0] == "reason":
                            self.reason = config[1]
        except IOError:
            self.prefer = False
            self.choice = ""
            self.reason = ""

        # Checkbox and variable for preference enabling.
        self.TkPrefer = IntVar()
        if self.prefer == True:
            self.TkPrefer.set(1)
        else:
            self.TkPrefer.set(0)
        self.preferentialCheckbox = Checkbutton(self,text="Enable Preference",variable=self.TkPrefer)
        self.preferentialCheckbox.grid(row=0,column=0,columnspan=2)

        # Label for preferentialTextbox
        self.ChoiceLabel = Label(self,text="Browser Choice")
        self.ChoiceLabel.grid(row=1,column=0)

        # Textbox to enter a preference.
        self.TkChoice = StringVar()
        self.TkChoice.set(self.choice)
        self.preferentialTextbox = Entry(self,textvariable=self.TkChoice)
        self.preferentialTextbox.grid(row=1,column=1)

        # Label for reasoningTextbox
        self.ReasonLabel = Label(self,text="Reason")
        self.ReasonLabel.grid(row=2,column=0)

        # Textbox to enter a reason for your preference.
        self.TkReason = StringVar()
        self.TkReason.set(self.reason)
        self.reasoningTextbox = Entry(self,textvariable=self.TkReason)
        self.reasoningTextbox.grid(row=2,column=1)

        self.savenexit = Button(self,text="Save/Exit",command=self.saveAndExit)
        self.savenexit.grid(row=3,column=0,columnspan=2,sticky=W+E)