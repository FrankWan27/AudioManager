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
        self.page4 = ttk.Frame(nb)
        page5 = ttk.Frame(nb)
        nb.add(page1, text='File Rename')
        nb.add(page2, text='Folder Rename')
        nb.add(self.page3, text='File Tag Edit')
        nb.add(self.page4, text='Folder Tag Edit')
        nb.add(page5, text='Clean Filename')

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

        Tkinter.Label(self.page3, text='File Path:').grid(column=0, row=0, sticky='EW')

        Tkinter.Entry(self.page3, textvariable=self.file).grid(column=1, row=0, sticky='EW')
       
        Tkinter.Button(self.page3, text='Browse...', command=self.openFileDialog, width=7).grid(column=2, row=0, sticky='W')
        
        Tkinter.Label(self.page3, text='Format:').grid(column=0, row=1, sticky='EW')
        
        Tkinter.Entry(self.page3, textvariable=self.format).grid(column=1, row=1, sticky='EW')

        Tkinter.Button(self.page3, text='Clear', command=lambda : self.format.set(''), width=7).grid(column=2, row=1, sticky='W')
        
        self.tagNum = []
        self.metadata = []
        self.rows = []
        self.clearFormatButton = []
        self.selectedTag = []
        self.addTagButton = []
        self.editTagButton = []

        self.tagNum.append(0)
        self.metadata.append(['Title', 'Artist', 'Album', 'Album Artist', 'Genre'])
        self.rows.append([])
        self.selectedTag.append(Tkinter.StringVar())
        self.selectedTag[0].set(self.metadata[0][0])
        self.tagMenu = []
        self.tagMenu.append(apply(Tkinter.OptionMenu, (self.page3, self.selectedTag[0]) + tuple(self.metadata[0])))
        self.tagMenu[0].grid(column=0, row=self.tagNum[0] + 2, sticky='EW')

        self.addTagButton.append(Tkinter.Button(self.page3, text='+ Add Tag', command=lambda : self.addTag(self.selectedTag[0].get(), 0)))
        self.addTagButton[0].grid(column=1, row=self.tagNum[0] + 2, sticky='EW')        

        self.editTagButton.append(Tkinter.Button(self.page3, text='Edit Tags', command=self.editTagClick, width=7))
        self.editTagButton[0].grid(column=2, row=self.tagNum[0] + 2, sticky='W')

        #FOLDER TAG EDIT

        Tkinter.Label(self.page4, text='Folder Path:').grid(column=0, row=0, sticky='EW')

        Tkinter.Entry(self.page4, textvariable=self.folder).grid(column=1, row=0, sticky='EW')
       
        Tkinter.Button(self.page4, text='Browse...', command=self.openFolderDialog, width=7).grid(column=2, row=0, sticky='W')
        
        Tkinter.Label(self.page4, text='Format:').grid(column=0, row=1, sticky='EW')
        
        Tkinter.Entry(self.page4, textvariable=self.format).grid(column=1, row=1, sticky='EW')
                
        Tkinter.Button(self.page4, text='Clear', command=lambda : self.format.set(''), width=7).grid(column=2, row=1, sticky='W')

        self.tagNum.append(0)
        self.metadata.append(['Title', 'Artist', 'Album', 'Album Artist', 'Genre'])
        self.rows.append([])
        self.selectedTag.append(Tkinter.StringVar())
        self.selectedTag[1].set(self.metadata[1][0])
        self.tagMenu.append(apply(Tkinter.OptionMenu, (self.page4, self.selectedTag[1]) + tuple(self.metadata[1])))
        self.tagMenu[1].grid(column=0, row=self.tagNum[1] + 2, sticky='EW')

        self.addTagButton.append(Tkinter.Button(self.page4, text='+ Add Tag', command=lambda : self.addTag(self.selectedTag[1].get(), 1)))
        self.addTagButton[1].grid(column=1, row=self.tagNum[1] + 2, sticky='EW')        

        self.editTagButton.append(Tkinter.Button(self.page4, text='Edit Tags', command=self.editTagFolderClick, width=7))
        self.editTagButton[1].grid(column=2, row=self.tagNum[1] + 2, sticky='W')

        #CLEAN FILE NAME
        Tkinter.Label(page5, text='File Path:').grid(column=0, row=0, sticky='EW')

        Tkinter.Entry(page5, textvariable=self.file).grid(column=1, row=0, sticky='EW')
       
        Tkinter.Button(page5, text='Browse...', command=self.openFileDialog, width=7).grid(column=2, row=0, sticky='W')

        Tkinter.Button(page5, text='Clean', command=self.cleanFileClick, width=7).grid(column=3, row=0, sticky='W')

        Tkinter.Label(page5, text='Folder Path:').grid(column=0, row=1, sticky='EW')

        Tkinter.Entry(page5, textvariable=self.folder).grid(column=1, row=1, sticky='EW')
       
        Tkinter.Button(page5, text='Browse...', command=self.openFolderDialog, width=7).grid(column=2, row=1, sticky='W')

        Tkinter.Button(page5, text='Clean', command=self.cleanFolderClick, width=7).grid(column=3, row=1, sticky='W')



        page1.grid_rowconfigure(0, pad=5)
        page1.grid_rowconfigure(1, pad=5)  
        page1.grid_columnconfigure(1, weight=1, minsiz=800)
        page1.grid_columnconfigure(0, weight=1, minsiz=120)
        page2.grid_rowconfigure(0, pad=5)
        page2.grid_rowconfigure(1, pad=5)  
        page2.grid_columnconfigure(1, weight=1, minsiz=800)
        page2.grid_columnconfigure(0, weight=1, minsiz=120)
        self.page3.grid_rowconfigure(0, pad=5)  
        self.page3.grid_rowconfigure(1, pad=5)  
        self.page3.grid_rowconfigure(2, pad=5)  
        self.page3.grid_columnconfigure(1, weight=1, minsiz=800)
        self.page3.grid_columnconfigure(0, weight=1, minsiz=120)
        self.page4.grid_rowconfigure(0, pad=5)  
        self.page4.grid_rowconfigure(1, pad=5)  
        self.page4.grid_rowconfigure(2, pad=5)  
        self.page4.grid_columnconfigure(1, weight=1, minsiz=800)
        self.page4.grid_columnconfigure(0, weight=1, minsiz=120)
        page5.grid_rowconfigure(0, pad=5)  
        page5.grid_rowconfigure(1, pad=5)  
        page5.grid_columnconfigure(1, weight=1, minsiz=715)
        page5.grid_columnconfigure(0, weight=1, minsiz=120)
    
    def cleanFileClick(self):
        cleanFile(self.file.get())

    def cleanFolderClick(self):
        cleanFolder(self.folder.get())

    def editTagClick(self):
        editTag(self.file.get(), self.format.get(), self.rows[0])

    def editTagFolderClick(self):
        editTagFolder(self.folder.get(), self.format.get(), self.rows[1])

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

    def addTag(self, tag, tab):
        group = []
        self.metadata[tab].remove(tag)
        label = Tkinter.Label(self.page3 if tab == 0 else self.page4, text=tag + ':', justify='left')
        label.grid(column=0, row=self.tagNum[tab]+2, sticky='EW')
        data = Tkinter.StringVar()
        entry = Tkinter.Entry(self.page3 if tab == 0 else self.page4, textvariable=data)
        entry.grid(column=1, row=self.tagNum[tab]+2, sticky='EW')
        group.append(label)
        group.append(entry)
        remove = Tkinter.Button(self.page3 if tab == 0 else self.page4, text='Remove', width=7,command=lambda : self.removeTag(group, remove, tag, tab))
        group.append(remove)
        group.append(tag)
        group.append(data)
        remove.grid(column=2, row=self.tagNum[tab]+2, sticky='W')

        self.rows[tab].append(group)

        #Shift buttons down one row
        self.tagNum[tab] += 1
        self.tagMenu[tab].grid_remove()
        self.addTagButton[tab].grid_forget()
        self.editTagButton[tab].grid_forget()
        self.editTagButton[tab].grid(column=2, row=self.tagNum[tab] + 2, sticky='W')
        self.page3.grid_rowconfigure(self.tagNum[tab] + 1, pad=5)  
        self.page4.grid_rowconfigure(self.tagNum[tab] + 1, pad=5)  
        if self.metadata[tab]:
            self.selectedTag[tab].set(self.metadata[tab][0])
            self.tagMenu[tab] = apply(Tkinter.OptionMenu, (self.page3 if tab == 0 else self.page4, self.selectedTag[tab]) + tuple(self.metadata[tab]))
            self.tagMenu[tab].grid(column=0, row=self.tagNum[tab] + 2, sticky='EW')
            self.addTagButton[tab].grid(column=1, row=self.tagNum[tab] + 2, sticky='EW')

    def removeTag(self, group, button, tag, tab):
        group[0].grid_remove()
        group[1].grid_remove()
        button.grid_remove()
        self.rows[tab].remove(group)
        self.metadata[tab].append(tag)
        self.tagNum[tab] -= 1
        #Shift buttons up one row
        for i in range(len(self.rows[tab])):
            for j in range(3):
                self.rows[tab][i][j].grid_remove()
                self.rows[tab][i][j].grid(column=j, row=i + 2, sticky='EW')
        self.tagMenu[tab].grid_remove()
        self.addTagButton[tab].grid_forget()
        self.editTagButton[tab].grid_forget()
        self.page3.grid_rowconfigure(self.tagNum[tab] + 1, pad=5)  
        self.selectedTag[tab].set(self.metadata[tab][0])
        self.tagMenu[tab] = apply(Tkinter.OptionMenu, (self.page3 if tab == 0 else self.page4, self.selectedTag[tab]) + tuple(self.metadata[tab]))
        self.tagMenu[tab].grid(column=0, row=self.tagNum[tab] + 2, sticky='EW')
        self.addTagButton[tab].grid(column=1, row=self.tagNum[tab] + 2, sticky='EW')
        self.editTagButton[tab].grid(column=2, row=self.tagNum[tab] + 2, sticky='W')





if __name__ == "__main__":
    app = audioGUI(None)
    app.title('AudioManager')
    app.mainloop()
