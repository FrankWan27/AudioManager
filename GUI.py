import Tkinter, tkFileDialog
class audioGUI(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        
        self.file = Tkinter.StringVar()
        
        self.fileEntry = Tkinter.Entry(self, textvariable=self.file)
        self.fileEntry.grid(column=1, row=0, sticky='EW')
        
        fileLabel = Tkinter.Label(self, text='File Path:')
        fileLabel.grid(column=0, row=0, sticky='EW')
       
        self.fileDialog = Tkinter.Button(self, text='Browse...', command=self.openDialog)
        self.fileDialog.grid(column=2, row=0, sticky='W')
        
        self.format = Tkinter.StringVar()
        self.format.set('%a - %t')
        
        self.formatEntry = Tkinter.Entry(self, textvariable=self.format)
        self.formatEntry.grid(column=1, row=1, sticky='EW')
        
        formatLabel = Tkinter.Label(self, text='Format: ')
        formatLabel.grid(column=0, row=1, sticky='EW')
        
        renameButton = Tkinter.Button(self, text='Rename', command=self.renameClick)
        renameButton.grid(column=1, row=2, sticky='W')


        self.grid_rowconfigure(1, pad=5)  
        self.grid_columnconfigure(1, weight=1, minsiz=800)

    def renameClick(self):
        print('go lul')

    def openDialog(self):
        filename = tkFileDialog.askopenfilename()
        self.file.set(filename)

if __name__ == "__main__":
    app = audioGUI(None)
    app.title('AudioManager')
    app.mainloop()
