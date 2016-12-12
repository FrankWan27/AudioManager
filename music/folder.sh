#!/bin/bash

songs=`ls ~/Programming/AudioManager/music`

for song in $songs
do
    echo when does serror happen
    echo `python AudioManager.py --file=$song`
    echo $song
done

