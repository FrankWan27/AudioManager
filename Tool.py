import mutagen
from mutagen.easyid3 import EasyID3
import os

#check if %[char] exists
formats = {'a':'Artist', 't':'Title', 'b':'Album', 'c':'Album Artist', 'n':'Track Number', 'g':'Genre'}
mp3formats = {'a':'TPE1', 't':'TIT2', 'b':'TALB', 'c':'TPE2', 'n':'TRCK', 'g':'TCON'}
aifformats = mp3formats
oggformats = {'a':'ARTIST', 't':'TITLE', 'b':'ALBUM'}

def renameFile(filePath, fileFormat):
    
    audio = mutagen.File(filePath)
    #look through format to check for %'s
    subs = []
    for i in range(len(fileFormat)-1):
        if fileFormat[i:i+1] == '%':
            subs.append(fileFormat[i+1:i+2])        



    for sub in subs:
        if sub not in formats:
            print('ERROR: %' + sub + ' is not recognized.')
            return;
    
    #rename file
    newName = ''

    #get correct audio format
    if str(type(audio)) == "<class 'mutagen.mp3.MP3'>":
        audioformat = mp3formats
    elif str(type(audio)) == "<class 'mutagen.aiff.AIFF'>":
        audioformat = aifformats
    elif str(type(audio)) == "<class 'mutagen.oggvorbis.OggVorbis'>":
        audioformat = oggformats
    else:
        print("Audio Format " + str(type(audio)) + " is unknown.")
        return;

    #go through format, replacing % with tags     
    i = 0
    while i < len(fileFormat):
        c = fileFormat[i:i+1]
        nc = fileFormat[i+1:i+2]
        i += 1
        if c == '%':
            i += 1
            
            if audioformat[nc] not in audio.tags:
                newName += 'Unknown ' + formats[nc]
            elif audioformat == oggformats:
                newName += str(audio.tags[audioformat[nc]][0])
            else:
                newName += str(audio.tags[audioformat[nc]])
            
        else:
            newName += c
    
    ext = os.path.splitext(filePath)[1]
    newName += ext
    path, fileName = os.path.split(filePath)
    
    print('\"' + fileName + '\"' + ' being renamed to \"' + newName + '\"')
    
    os.rename(filePath, os.path.join(path, newName))

def renameFolder(folderPath, fileFormat):

    for file in os.listdir(folderPath):
        renameFile(os.path.join(folderPath, file), fileFormat)

def editTag(filePath, fileFormat, rows):
    
    ext = os.path.splitext(filePath)[1]
    if ext == '.mp3' or ext == '.aif' or ext == '.wav':
        audio = EasyID3(filePath)
    elif ext == '.ogg': 
        audio = mutagen.File(filePath)
    else:
        print('Audio Format ' + ext + ' is currently unsupported :(')
        return

    formatList = []

    i = 0
    string = ''
    while i < len(fileFormat):
        if fileFormat[i:i+1] == '%':
            if string != '':
                formatList.append(string)
                string = ''
            formatList.append(fileFormat[i:i+2])  
            i += 1
        else:
            string += fileFormat[i:i+1]           
        i += 1
    
    fileName = os.path.split(filePath)[1][0:-4]

    i = 0 
    for s in range(len(formatList)):
        if formatList[s][0] != '%':
            for c in formatList[s]:
                if c == fileName[i]:
                    i += 1
                else:
                    print('Audio Format does not match File Name at index ' + i + '.')
                    return
        else:
            tag = ''                
            tagLength = 0

            if s < len(formatList) - 1:
                nextWord = formatList[s + 1]
                while(fileName[i+tagLength:i+tagLength+len(nextWord)] != nextWord):
                    if i + tagLength + len(nextWord) > len(fileName):
                        print('Audio Format does not match File Name at index a lot' )
                        return
                    else:
                        tagLength += 1
                tag = fileName[i:i+tagLength]
            else:
                tag = fileName[i:len(fileName)]

            audio[formats[formatList[s][1]].replace(' ','')] = tag
            i += tagLength





    subs = []
    for i in range(len(fileFormat)-1):
        if fileFormat[i:i+1] == '%':
            subs.append(fileFormat[i+1:i+2])  
    for sub in subs:
        if sub not in formats:
            print('ERROR: %' + sub + ' is not recognized.')
            return;

    for row in rows:
        audio[row[3].replace(' ', '')] = row[4].get()
        #for code, f in formats.iteritems():
    
    print(audio.pprint())
    audio.save()

def editTagFolder(folderPath, fileFormat, rows):

    for file in os.listdir(folderPath):
        editTag(os.path.join(folderPath, file), fileFormat, rows)

def cleanFile(filePath):

    path, fileName = os.path.split(filePath)
    
    i = 0
    newName = ''
    while i < len(fileName):
        if fileName[i:i+1] == '_':
            newName += ' '
        elif fileName[i:i+3] == '%20':
            newName += ' '
            i += 2
        else:
            newName += fileName[i:i+1]
        i += 1

    print('\"' + fileName + '\"' + ' being renamed to \"' + newName + '\"')
    
    os.rename(filePath, os.path.join(path, newName))

def cleanFolder(folderPath):
    for file in os.listdir(folderPath):
        cleanFile(os.path.join(folderPath, file))   