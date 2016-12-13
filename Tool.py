import mutagen
import os
def renameFile(fileName, fileFormat):
    
    audio = mutagen.File(fileName)
    #look through format to check for %'s
    subs = []
    for i in range(len(fileFormat)-1):
        if fileFormat[i:i+1] == '%':
            subs.append(fileFormat[i+1:i+2])        

    #check if %[char] exists
    formats = {'a':'Artist', 't':'Title', 'b':'Album', 'c':'Album Artist', 'n':'Track Number', 'y':'Year', 'g':'Genre'}
    mp3formats = {'a':'TPE1', 't':'TIT2', 'b':'TALB', 'c':'TPE2', 'n':'TRCK', 'y': 'TYER', 'g':'TCON'}
    aifformats = mp3formats
    oggformats = {'a':'ARTIST', 't':'TITLE', 'b':'ALBUM'}

    for sub in subs:
        if sub not in formats:
            print('ERROR: %' + sub + ' is not recognized.')
            exit(-1)

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
        exit(-1)

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

    ext = os.path.splitext(fileName)[1]
    print('\"' + fileName + '\"' + ' being renamed to \"' + newName + ext + '\"')
    #user confirm action
    cont = raw_input('Would you like to continue? (y/n) ')
    if cont == 'y' or  cont == 'Y':
        os.rename(fileName, newName + ext)

