import mutagen

audio = mutagen.File('song1.mp3')
print(audio.tags.pprint())
print(audio.tags['TIT2'])

