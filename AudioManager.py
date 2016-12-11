import eyed3
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--file', help='path to audio file', default='')
parser.add_argument('--format', help='naming format of mp3 file', default='%a - %t')

args = parser.parse_args()

fileName = args.file
fileFormat = args.format

if len(sys.argv) == 1:
    print('ERROR: Please enter a file name.')
    exit(-1)

audio = eyed3.load(fileName)

#look through format to check for %'s
subs = []
for i in range(len(fileFormat)-1):
    if fileFormat[i:i+1] == '%':
        subs.append(fileFormat[i+1:i+2])        

#check if %[char] exists
formats = {'a':'artist', 't':'title', 'b':'album', 'c':'album_artist', 'n':'track_num'}
for sub in subs:
    if sub not in formats:
        print('ERROR: %' + sub + ' is not recognized.')
        exit(-1)

#rename file
newName = '';
#for i in range(len(fileFormat)): <- can't increment i in for loop?
i = 0
while i < len(fileFormat):
    c = fileFormat[i:i+1]
    nc = fileFormat[i+1:i+2]
    i += 1
    if c == '%':
        i += 1
        print('ncrement')
           
        #Fix this
        if nc == 'a':
            newName += audio.tag.artist
        elif nc == 't':
            newName += audio.tag.title
        elif nc == 'b':
            newName += audio.tag.album
        elif nc == 'c':
            newName += audio.tag.album_artist
        elif nc == 'n':
            newName += audio.tag.track_num
    else:
        newName += c

print('\"' + fileName + '\"' + ' being renamed to \"' + newName + '\"')
#user confirm action
#cont = input('Would you like to continue? (y/n) ')
#if cont == 'y' or  cont == 'Y':
audio.rename(newName)
