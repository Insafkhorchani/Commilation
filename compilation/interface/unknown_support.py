#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Apr 03, 2020 05:07:09 PM WAT  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def compiler(myres):
    global i

    list=[r"C:\Users\ASUS\Desktop\compilation\final\prog1Comp.txt",r"C:\Users\ASUS\Desktop\compilation\final\prog2Comp.txt",r"C:\Users\ASUS\Desktop\compilation\final\prog3Comp.txt",r"C:\Users\ASUS\Desktop\compilation\final\prog4Comp.txt",r"C:\Users\ASUS\Desktop\compilation\final\prog6Comp.txt"]
    print('unknown_support.compiler')
    
    
    sys.stdout.flush()
    fichier = open(list[i], "r")
    i+=1

    lines = fichier.readlines()
    res ;
    for line in lines :
        
        res+=line+'\n'
    
    myres.set(res)

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import unknown
    unknown.vp_start_gui()




