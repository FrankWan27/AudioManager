#!/usr/bin/python
# -*- coding: utf-8 -*-


import mutagen
fileName = raw_input('Enter a file name: ')
audio = mutagen.File(fileName)
print(audio.tags.pprint())
print(audio.tags)
print((audio.tags['ARTIST'][0]))
print(audio.mime)
print(type(audio))
