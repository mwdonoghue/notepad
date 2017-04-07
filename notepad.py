"""
A simple notepad used to learn about wxPython.
Created using Python 2.7 on Windows 10. There have been issues running
the code in Linux. Why, I don't know yet.

Author: Mark Donoghue (mark.w.donoghue@gmail.com)
"""

import wx
import os

class MyFrame(wx.Frame):
	"""Constructor"""
	def __init__(self, parent, title):
		
		wx.Frame.__init__(self, parent, title=title, size=(640,480))
		self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
		
		
		#Build menu
		filemenu = wx.Menu()
		othermenu = wx.Menu()
		
		#File Menu components
		menuOpen = filemenu.Append(wx.ID_OPEN, "Open\tCtrl-O", "Open a file")
		self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
		menuSave = filemenu.Append(wx.ID_SAVE, "Save\tCtrl-S", "Save text to a file")
		self.Bind(wx.EVT_MENU, self.OnSave, menuSave)
		filemenu.AppendSeparator()
		menuExit = filemenu.Append(wx.ID_EXIT, "Exit\tCtrl-Q", "End program")
		self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
		
		#Other menu components
		menuAbout = othermenu.Append(wx.ID_ABOUT, "About", "Info about app")
		self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)		
		
		#Create menubar
		menuBar = wx.MenuBar()
		menuBar.Append(filemenu, "File")
		menuBar.Append(othermenu, "Other")
		self.SetMenuBar(menuBar)
		self.Show(True)
		
	def OnAbout(self, e):
		msg = wx.MessageDialog(self, "A text editor to test wxPython", "About", wx.OK)
		msg.ShowModal()
		msg.Destroy()
	
	def OnOpen(self, e):
		""" Open a file"""
		self.dirname = ''
		dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			self.filename = dlg.GetFilename()
			self.dirname = dlg.GetDirectory()
			f = open(os.path.join(self.dirname, self.filename), 'r')
			self.control.SetValue(f.read())
			f.close()
			self.SetTitle("Editing file: " + self.dirname + "\\" + self.filename)
		dlg.Destroy()
		
	def OnSave(self, e):
		self.dirname = 'Untitled.txt'
		#print self.control.GetValue();
		dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.SAVE | wx.OVERWRITE_PROMPT)
		if dlg.ShowModal() == wx.ID_OK:
			txt = self.control.GetValue()
			
			self.filename = dlg.GetFilename()
			self.dirname = dlg.GetDirectory()
			filehandle = open(os.path.join(self.dirname, self.filename), 'w')
			filehandle.write(txt)
			filehandle.close()
		dlg.Destroy()
		
	def OnClose(self, e):
		self.control.SetValue("")
		
	def OnExit(self, e):
		dlg = wx.MessageDialog(self, "Are you sure you want to quit?", "Question", wx.YES_NO)
		if dlg.ShowModal() == wx.ID_YES:	
			self.Close(True)
		
app = wx.App(False)
frame = MyFrame(None, 'TextEdit')
app.MainLoop()