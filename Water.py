import os
import time
import threading
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import pygame

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_reminder_music(music_file, volume_level):
    pygame.mixer.init()
    pygame.mixer.music.load(music_file) 
    pygame.mixer.music.set_volume(volume_level)  # Set volume level
    pygame.mixer.music.play()
def stop_music():
    pygame.mixer.music.stop()

def show_popup(interval=1800):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()

    response = messagebox.showinfo("JAVRIS", "Hey SIR! Time to drink some water!\nRemember to stay hydrated!", master=root)
    if response == "ok":
        stop_music()

    root.mainloop()


def Wdr(root,interval, music_file, volume_level):
    clear_screen()
    play_reminder_music(music_file, volume_level)
    show_popup()
    root.after(interval * 1000, lambda: Wdr(interval, music_file, volume_level))


def set_interval(interval_label, interval_entry):
    interval_label.config(text="Interval (seconds): " + interval_entry.get())

def choose_music(music_label):
    music_file_path = filedialog.askopenfilename(filetypes=(("MP3 files", "*.mp3"), ("All files", "*.*")))
    if music_file_path:
        music_filename = os.path.basename(music_file_path)  # Extract filename from full path
        music_label.config(text="Music File: " + music_filename)
    return music_file_path


def set_volume(volume_label, volume_scale):
    volume_label.config(text="Volume Level: " + str(volume_scale.get()))
    return volume_scale.get() / 100  # Convert volume scale to a value between 0 and 1

def start_reminder(root,interval_entry, music_label, volume_scale, volume_label):
    interval = int(interval_entry.get())
    music_file = music_label.cget("text").split(": ")[1]
    volume_level = set_volume(volume_label, volume_scale)  # Pass volume_label here
    Wdr(root,interval, music_file, volume_level)

if __name__ == "__main__":
    # Create the main tkinter window
    root = tk.Tk()
    root.title("Water Reminder")
    root.config(background='aqua')
    root.wm_iconbitmap('D:\python\Project\Water drinking remainder\Water-Drinking-remainder/1.ico')
    
    # Widgets
    interval_label = tk.Label(root, text="Interval (seconds): ", bg='aqua', fg='black', font=('Times new roman',10,'bold'))
    interval_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
    
    interval_entry = tk.Entry(root)
    interval_entry.grid(row=0, column=1, padx=10, pady=5)
    
    set_interval_button = tk.Button(root, text="Set Interval", command=lambda: set_interval(interval_label, interval_entry), bg='aqua', fg='black', font=('Times new roman',10,'bold'))
    set_interval_button.grid(row=0, column=2, padx=10, pady=5)
    
    music_label = tk.Label(root, text="Music File: No file selected", bg='aqua', fg='black', font=('Times new roman',10,'bold'))
    music_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
    
    choose_music_button = tk.Button(root, text="Choose Music", command=lambda: choose_music(music_label),bg='aqua', fg='black', font=('Times new roman',10,'bold'))
    choose_music_button.grid(row=1, column=1, padx=10, pady=5)
    
    volume_label = tk.Label(root, text="Volume Level: 100", bg='aqua', fg='black', font=('Times new roman',10,'bold'))
    volume_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)
    
    volume_scale = ttk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
    volume_scale.set(100)  # Default volume level
    volume_scale.grid(row=2, column=1, columnspan=2, padx=10, pady=5)
    
    start_button = tk.Button(root, text="Start Reminder", bg='aqua', fg='black', font=('Times new roman',10,'bold'), command=lambda: start_reminder(root,interval_entry, music_label, volume_scale, volume_label))
    start_button.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

    # Run the tkinter event loop
    root.mainloop()

