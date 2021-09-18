from tkinter import *
from styles import *    # cointains basic fonts and color stuffs
import random
import time
import os


def get_music_files():
    music_folder = os.listdir(
        'Music-player-using-TKinter/music'
        )    # listdir lists all the file in a directory
    return music_folder

def run_music():
    while True:
        music_files = get_music_files()
        shuffled_music = random.choice(music_files)
        
        shuffled_music_full_path = os.path.join(os.curdir, 'Music-player-using-TKinter/music', shuffled_music)  # curdir -> current directory
        
        os.startfile(shuffled_music_full_path)
        print(shuffled_music_full_path)
        time.sleep(5)   # 5 secs is given, so it plays next song in every 5 secs

