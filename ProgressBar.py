# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 15:32:33 2020

@author: waziri
"""

from tkinter import *
from tkinter.ttk import *

class ProgressBarApp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self,*args, **kwargs)
        
    
        self.progress_bar = Progressbar(orient="horizontal",
                                        length=200, mode="determinate")
        self.progress_bar.pack(side=TOP)
    
        self.btn_start = Button(text="Start")
        self.btn_start.pack(side=LEFT)
        
        self.btn_stop = Button(text="Stop")
        self.btn_stop.pack(side=LEFT)
    
    
pBar = ProgressBarApp()
pBar.mainloop()