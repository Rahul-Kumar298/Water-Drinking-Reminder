import time
import os
import pygame
import tkinter as tk
from tkinter import messagebox
import threading

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_reminder_music():
    pygame.mixer.init()
    pygame.mixer.music.load("music.mp3") 
    pygame.mixer.music.play()

def show_popup():
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo("JAVRIS", "Hey SIR! Time to drink some water!\nRemember to stay hydrated!", master=root)
    root.mainloop()

def Wdr(interval):
    while True:
        clear_screen()
        music_thread = threading.Thread(target=play_reminder_music)
        popup_thread = threading.Thread(target=show_popup)
        music_thread.start()
        popup_thread.start()
        time.sleep(interval)  # Wait for the specified interval
        # No need to join the threads here
        # music_thread.join()  
        # popup_thread.join()  

if __name__ == "__main__":
    interval = 1800 # interval in seconds
    Wdr(interval)
