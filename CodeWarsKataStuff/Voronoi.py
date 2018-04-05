#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 01:43:12 2017

@author: unityspace
"""

import Tkinter as Tk
import tkFileDialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import numpy as np
from scipy.spatial import voronoi_plot_2d,Voronoi
 
class SidePanel():
    def __init__(self, root,ax0,fig):
        self.frame2 = Tk.Frame( root )
        self.frame2.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)
        self.ax=ax0
        self.fig=fig
        self.ploted = False
        plotBut = Tk.Button(self.frame2, text="Plot")
        plotBut.pack(side="top",fill=Tk.BOTH)
        plotBut.bind("<Button>", self.my_plot)
         
        voroButton = Tk.Button(self.frame2, text="Load 2D points")
        voroButton.pack(side="top",fill=Tk.BOTH)
        voroButton.bind("<Button>", self.plotVo)
 
        clearButton = Tk.Button(self.frame2, text="Clear")
        clearButton.pack(side="top",fill=Tk.BOTH)
        clearButton.bind("<Button>", self.clear)
 
    def plotVo(self,event):
        self.ax.clear()
        root = Tk.Tk()
        root.withdraw()
 
        fname = tkFileDialog.askopenfilename()
        print (fname)
 
       # fname=r"/Users/Sukhbinder/Desktop/Desktop/sys2ndnov/SK14/SK14_v3_trials/SK14_trials/data/sk14/testcases/testcase5/cooords.item"
        data=np.genfromtxt(fname,skiprows=2)
        if data.shape[1] >2:
            data =data[:,:-1]
        self.var = Voronoi(data)
        voronoi_plot_2d(self.var,ax=self.ax)
        self.ploted = True
        self.fig.canvas.draw()
         
    def clear(self,event):
        self.ax.clear()
        self.fig.canvas.draw()
         
    def my_plot(self,event):
        self.ax.clear()
        self.ax.plot(np.random.rand(100))
        self.ploted = True
        self.fig.canvas.draw()
 
class Window():
    def __init__(self, master):
        self.frame = Tk.Frame(master)
        self.f = Figure( figsize=(10, 9), dpi=80 )
        self.ax0 = self.f.add_axes( (0.05, .05, .90, .90), axisbg=(.75,.75,.75), frameon=False)
         
       # self.ax0.plot(np.max(np.random.rand(100,10)*10,axis=1),"r-")
        self.frame = Tk.Frame( root )
        self.frame.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)
         
        self.sidepanel=SidePanel(root,self.ax0,self.f)
         
        self.canvas = FigureCanvasTkAgg(self.f, master=self.frame)
        self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        self.canvas.show()
        
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, self.frame )
        self.toolbar.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        self.toolbar.update()
 
         
 
if __name__ == '__main__':
    root = Tk.Tk()
    app = Window(root)
    root.title( "Voronoi with Python" )
    root.update()
    root.deiconify()
    root.mainloop()