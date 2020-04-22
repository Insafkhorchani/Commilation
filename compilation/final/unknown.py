#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Apr 03, 2020 03:02:21 PM WAT  platform: Windows NT

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

import unknown_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    unknown_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    unknown_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+650+150")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        self.test=tk.StringVar()

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.367, rely=0.311, height=24, width=137)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#FEA827")
        self.Button1.configure(command=lambda:unknown_support.compiler(self.test))
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''compiler''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.033, rely=0.044,height=280, relwidth=0.34)
        self.Entry1.configure(background="#42B7A8")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
       
#        self.Label1 = tk.Label(self.Entry1)
#        self.Label1.place(relx=0.151, rely=0.15, height=21, width=32)
#        self.Label1.configure(background="#d9d9d9")
#        self.Label1.configure(disabledforeground="#a3a3a3")
#        self.Label1.configure(foreground="#000000")
#        self.Label1.configure(text='''code''')

        self.Entry2 = tk.Entry(top,textvariable=self.test)
        self.Entry2.place(relx=0.6, rely=0.067,height=270, relwidth=0.357)
        self.Entry2.configure(background="#42B7A8")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")



#        self.Label2 = tk.Label(top)
#        self.Label2.place(relx=0.186, rely=0.031, height=21, width=82)
#        self.Label2.configure(background="#d9d9d9")
#        self.Label2.configure(disabledforeground="#a3a3a3")
#        self.Label2.configure(foreground="#000000")
#        self.Label2.configure(text='''compilation  ..''')

if __name__ == '__main__':
    vp_start_gui()


