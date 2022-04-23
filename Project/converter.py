# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 15:54:25 2022

@author: Mattia
"""

import os
from pydub import AudioSegment

# files                                                                         
src_folder = "C:/Users/Mattia/Desktop/TESI/Project/chorus"
dst_folder = "C:/Users/Mattia/Desktop/TESI/Project/chorus-wav/"

os.chdir(src_folder)
audio_files = os.listdir()

for filename in audio_files:
    wav_name = filename.replace(".mp3", ".wav")
    print("{}/{}".format(src_folder, filename))
    # convert wav to mp3                                                            
    sound = AudioSegment.from_mp3("{}/{}".format(src_folder, filename))
    sound.export("{}/{}".format(dst_folder, wav_name), format="wav")