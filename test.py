import mutagen

audio = mutagen.File('song.ogg')
print(audio.tags.pprint())
print(audio.mime)
print(type(audio))
