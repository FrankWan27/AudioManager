import Tkinter, tkFileDialog
import ttk
from Tool import *

class audioGUI(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        self.resizable(0,0)
        nb = ttk.Notebook(self)

        page1 = ttk.Frame(nb)
        page2 = ttk.Frame(nb)
        self.page3 = ttk.Frame(nb)
        page4 = ttk.Frame(nb)
        nb.add(page1, text='File Rename')
        nb.add(page2, text='Folder Rename')
        nb.add(self.page3, text='File Tag Edit')
        nb.add(page4, text='Folder Tag Edit')
        nb.grid(column=0, row=0, stick='EW')
        
        #Variables to store
        self.format = Tkinter.StringVar()
        self.format.set('%a - %t')
        self.file = Tkinter.StringVar()
        self.folder = Tkinter.StringVar()

        #FILE RENAME     
        Tkinter.Label(page1, text='File Path:').grid(column=0, row=0, sticky='EW')

        Tkinter.Entry(page1, textvariable=self.file).grid(column=1, row=0, sticky='EW')
       
        Tkinter.Button(page1, text='Browse...', command=self.openFileDialog, width=7).grid(column=2, row=0, sticky='W')
        
        Tkinter.Label(page1, text='Format:').grid(column=0, row=1, sticky='EW')
        
        Tkinter.Entry(page1, textvariable=self.format).grid(column=1, row=1, sticky='EW')
                
        Tkinter.Button(page1, text='Rename', command=self.renameFileClick, width=7).grid(column=2, row=1, sticky='W')

        #FOLDER RENAME      
        Tkinter.Label(page2, text='Folder Path:').grid(column=0, row=0, sticky='EW')

        Tkinter.Entry(page2, textvariable=self.folder).grid(column=1, row=0, sticky='EW')

        Tkinter.Button(page2, text='Browse...', command=self.openFolderDialog, width=7).grid(column=2, row=0, sticky='W')

        Tkinter.Label(page2, text='Format:').grid(column=0, row=1, sticky='EW')

        Tkinter.Entry(page2, textvariable=self.format).grid(column=1, row=1, sticky='EW')

        Tkinter.Button(page2, text='Rename', command=self.renameFolderClick, width=7).grid(column=2, row=1, sticky='W')

        #FILE TAG EDIT

        fileLabel3 = Tkinter.Label(self.page3, text='File Path:').grid(column=0, row=0, sticky='EW')

        fileEntry3 = Tkinter.Entry(self.page3, textvariable=self.file).grid(column=1, row=0, sticky='EW')
       
        fileDialog3 = Tkinter.Button(self.page3, text='Browse...', command=self.openFileDialog, width=7).grid(column=2, row=0, sticky='W')
        
        formatLabel = Tkinter.Label(self.page3, text='Format:').grid(column=0, row=1, sticky='EW')
        
        formatEntry = Tkinter.Entry(self.page3, textvariable=self.format).grid(column=1, row=1, sticky='EW')

        self.tagNum = 0
        self.metadata = ['Title', 'Artist', 'Album', 'Album Artist', 'Genre']
        self.data = []
        self.rows = []
        self.selectedTag = Tkinter.StringVar()
        self.selectedTag.set(self.metadata[0])
        self.tagMenu = apply(Tkinter.OptionMenu, (self.page3, self.selectedTag) + tuple(self.metadata))
        self.tagMenu.grid(column=0, row=self.tagNum + 2, sticky='EW')

        self.addTagButton = Tkinter.Button(self.page3, text='+ Add Tag', command=lambda : self.addTag(self.selectedTag.get()))
        self.addTagButton.grid(column=1, row=self.tagNum + 2, sticky='EW')        


        self.editTagButton = Tkinter.Button(self.page3, text='Edit Tags', command=self.editTagClick, width=7)
        self.editTagButton.grid(column=2, row=self.tagNum + 2, sticky='W')

        page1.grid_rowconfigure(1, pad=5)  
        page1.grid_columnconfigure(1, weight=1, minsiz=800)
        page1.grid_columnconfigure(0, weight=1, minsiz=120)
        page2.grid_rowconfigure(1, pad=5)  
        page2.grid_columnconfigure(1, weight=1, minsiz=800)
        page2.grid_columnconfigure(0, weight=1, minsiz=120)
        self.page3.grid_rowconfigure(0, pad=5)  
        self.page3.grid_rowconfigure(1, pad=5)  
        self.page3.grid_rowconfigure(2, pad=5)  
        self.page3.grid_columnconfigure(1, weight=1, minsiz=800)
        self.page3.grid_columnconfigure(0, weight=1, minsiz=120)

    def editTagClick(self):
        editTag(self.file.get(), self.format.get(), self.rows)

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

    def addTag(self, tag):
        group = []
        self.metadata.remove(tag)
        label = Tkinter.Label(self.page3, text=tag + ':', justify='left')
        label.grid(column=0, row=self.tagNum+2, sticky='EW')
        self.data.append(Tkinter.StringVar())
        entry = Tkinter.Entry(self.page3, textvariable=self.data[self.tagNum])
        entry.grid(column=1, row=self.tagNum+2, sticky='EW')
        group.append(label)
        group.append(entry)
        remove = Tkinter.Button(self.page3, text='Remove', width=7,command=lambda : self.removeTag(group, remove, tag))
        group.append(remove)
        group.append(tag)
        group.append(self.data[self.tagNum])
        remove.grid(column=2, row=self.tagNum+2, sticky='W')

        self.rows.append(group)

        #Shift buttons down one row
        self.tagNum += 1
        self.tagMenu.grid_remove()
        self.addTagButton.grid_forget()
        self.editTagButton.grid_forget()
        self.editTagButton.grid(column=2, row=self.tagNum + 2, sticky='W')
        self.page3.grid_rowconfigure(self.tagNum + 1, pad=5)  
        if self.metadata:
            self.selectedTag.set(self.metadata[0])
            self.tagMenu = apply(Tkinter.OptionMenu, (self.page3, self.selectedTag) + tuple(self.metadata))
            self.tagMenu.grid(column=0, row=self.tagNum + 2, sticky='EW')
            self.addTagButton.grid(column=1, row=self.tagNum + 2, sticky='EW')

    def removeTag(self, group, button, tag):
        group[0].grid_remove()
        group[1].grid_remove()
        button.grid_remove()
        self.rows.remove(group)
        self.metadata.append(tag)
        self.tagNum -= 1
        #Shift buttons up one row
        for i in range(len(self.rows)):
            for j in range(3):
                self.rows[i][j].grid_remove()
                self.rows[i][j].grid(column=j, row=i + 2, sticky='EW')
        self.tagMenu.grid_remove()
        self.addTagButton.grid_forget()
        self.editTagButton.grid_forget()
        self.page3.grid_rowconfigure(self.tagNum + 1, pad=5)  
        self.selectedTag.set(self.metadata[0])
        self.tagMenu = apply(Tkinter.OptionMenu, (self.page3, self.selectedTag) + tuple(self.metadata))
        self.tagMenu.grid(column=0, row=self.tagNum + 2, sticky='EW')
        self.addTagButton.grid(column=1, row=self.tagNum + 2, sticky='EW')
        self.editTagButton.grid(column=2, row=self.tagNum + 2, sticky='W')





if __name__ == "__main__":
    app = audioGUI(None)
    app.title('AudioManager')
    app.mainloop()
