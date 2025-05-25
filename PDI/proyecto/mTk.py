# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 15:51:30 2025

@author: dtrej
"""

import tkinter
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

window = tkinter.Tk()
window.wm_withdraw()
window.wm_attributes("-topmost", True)

def selectFile():
    filename = askopenfilename()
    return filename
