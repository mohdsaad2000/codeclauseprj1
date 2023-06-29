import os
import pygame
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Music Player")
root.geometry("400x300")

pygame.mixer.init()

def play():
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def resume():
    pygame.mixer.music.unpause()

def choose_song():
    global file_path
    file_path = filedialog.askopenfilename()

choose_button = Button(root, text="Choose Song", command=choose_song)
choose_button.pack(pady=10)

play_button = Button(root, text="Play", command=play)
play_button.pack(pady=10)

stop_button = Button(root, text="Stop", command=stop)
stop_button.pack(pady=10)

pause_button = Button(root, text="Pause", command=pause)
pause_button.pack(pady=10)

resume_button = Button(root, text="Resume", command=resume)
resume_button.pack(pady=10)

root.mainloop()
