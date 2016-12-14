import Tkinter, tkFileDialog
import ttk
from Tool import renameFile, renameFolder

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
        
        fileLabel = Tkinter.Label(page1, text='File Path:').grid(column=0, row=0, sticky='EW')

        fileEntry = Tkinter.Entry(page1, textvariable=self.file).grid(column=1, row=0, sticky='EW')
       
        fileDialog = Tkinter.Button(page1, text='Browse...', command=self.openFileDialog).grid(column=2, row=0, sticky='W')
        
        self.format = Tkinter.StringVar()
        self.format.set('%a - %t')
        
        formatLabel = Tkinter.Label(page1, text='Format:').grid(column=0, row=1, sticky='EW')
        
        formatEntry = Tkinter.Entry(page1, textvariable=self.format).grid(column=1, row=1, sticky='EW')
                
        renameButton = Tkinter.Button(page1, text='Rename', command=self.renameFileClick).grid(column=2, row=2, sticky='W')

        self.folder = Tkinter.StringVar()

        folderLabel = Tkinter.Label(page2, text='Folder Path:').grid(column=0, row=0, sticky='EW')

        folderEntry = Tkinter.Entry(page2, textvariable=self.folder).grid(column=1, row=0, sticky='EW')

        folderDialog = Tkinter.Button(page2, text='Browse...', command=self.openFolderDialog).grid(column=2, row=0, sticky='W')

        formatLabel2 = Tkinter.Label(page2, text='Format:').grid(column=0, row=1, sticky='EW')

        formatEntry2 = Tkinter.Entry(page2, textvariable=self.format).grid(column=1, row=1, sticky='EW')

        renameButton = Tkinter.Button(page2, text='Rename', command=self.renameFolderClick).grid(column=2, row=2, sticky='W')


        page1.grid_rowconfigure(1, pad=5)  
        page1.grid_columnconfigure(1, weight=1, minsiz=800)
        page2.grid_rowconfigure(1, pad=5)  
        page2.grid_columnconfigure(1, weight=1, minsiz=800)

    def renameFileClick(self):
        renameFile(self.file.get(), self.format.get())

    def renameFolderClick(self):
        renameFolder(self.folder.get(), self.format.get())

    def openFileDialog(self):
        filename = tkFileDialog.askopenfilename()
        self.file.set(filename)

    def openFolderDialog(self):
        foldername = tkFileDialog.askdirectory()
        self.folder.set(foldername)

if __name__ == "__main__":
    app = audioGUI(None)
    app.title('AudioManager')
    app.mainloop()
