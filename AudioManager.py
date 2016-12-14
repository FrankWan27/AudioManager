import Tkinter, tkFileDialog
import ttk
from Tool import renameFile
import Tab
class audioGUI(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        
        nb = ttk.Notebook(self)

        page1 = ttk.Frame(nb)
        page2 = ttk.Frame(nb)
        page3 = ttk.Frame(nb)
        page4 = ttk.Frame(nb)
        nb.add(page1, text='File Rename')
        nb.add(page2, text='Folder Rename')
        nb.add(page3, text='File Tag Edit')
        nb.add(page4, text='Folder Tag Edit')
        nb.grid(column=0, row=0, stick='EW')
        
        self.file = Tkinter.StringVar()
        
        fileEntry = Tkinter.Entry(page1, textvariable=self.file)
        fileEntry.grid(column=1, row=0, sticky='EW')

        fileLabel = Tkinter.Label(page1, text='File Path:')
        fileLabel.grid(column=0, row=0, sticky='EW')
       
        fileDialog = Tkinter.Button(page1, text='Browse...', command=self.openDialog)
        fileDialog.grid(column=2, row=0, sticky='W')
        
        self.format = Tkinter.StringVar()
        self.format.set('%a - %t')
        
        formatEntry = Tkinter.Entry(page1, textvariable=self.format)
        formatEntry.grid(column=1, row=1, sticky='EW')
                
        formatLabel = Tkinter.Label(page1, text='Format:')
        formatLabel.grid(column=0, row=1, sticky='EW')
        
        renameButton = Tkinter.Button(page1, text='Rename', command=self.renameClick)
        renameButton.grid(column=1, row=2, sticky='W')


        page1.grid_rowconfigure(1, pad=5)  
        page1.grid_columnconfigure(1, weight=1, minsiz=800)

    def renameClick(self):
        renameFile(self.file.get(), self.format.get())

    def openDialog(self):
        filename = tkFileDialog.askopenfilename()
        self.file.set(filename)

if __name__ == "__main__":
    app = audioGUI(None)
    app.title('AudioManager')
    app.mainloop()
