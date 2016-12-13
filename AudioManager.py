 #!/usr/bin/python
# -*- coding: utf-8 -*-
import mutagen
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--file', help='path to audio file', default='')
parser.add_argument('--format', help='naming format of mp3 file', default='%a - %t')

args = parser.parse_args()

fileName = args.file
fileFormat = args.format

if args.file == '':
    fileName = raw_input('Please enter the audio file name: ')

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
m4aformats = {'a':'©ART', 't':'©nam', 'b':'©alb', 'c':'©wrt', 'n':'trkn', 'y': '©day', 'g':'©gen'}

for sub in subs:
    if sub not in formats:
        print('ERROR: %' + sub + ' is not recognized.')
        exit(-1)

#rename file
newName = ''
i = 0

#get correct audio format
if str(type(audio)) == "<class 'mutagen.mp3.MP3'>":
    audioformat = mp3formats
elif str(type(audio)) == "<class 'mutagen.aiff.AIFF'>":
    audioformat = aifformats
elif str(type(audio)) == "<class 'mutagen.mp4.MP4'>":
    audioformat = m4aformats
elif str(type(audio)) == "<class 'mutagen.oggvorbis.OggVorbis'>":
    audioformat = oggformats
else:
    print("Audio Format " + str(type(audio)) + " is unknown.")
    exit(-1)
while i < len(fileFormat):
    c = fileFormat[i:i+1]
    nc = fileFormat[i+1:i+2]
    i += 1
    if c == '%':
        i += 1
        if audioformat[nc] not in audio.tags:
            newName += 'Unknown ' + formats[nc]
        else:
            newName += str(audio.tags[audioformat[nc]])
       
    else:
        newName += c

print('\"' + fileName + '\"' + ' being renamed to \"' + newName + '.mp3\"')
#user confirm action
cont = raw_input('Would you like to continue? (y/n) ')
if cont == 'y' or  cont == 'Y':
    audio.rename(newName)
