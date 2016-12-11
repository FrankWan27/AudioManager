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




