import os
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import pygame
# Global variable to store the music file path
music_file_path = ""
def play_reminder_music(music_file_path, volume_level):
    pygame.mixer.init()
    pygame.mixer.music.load(music_file_path)
    pygame.mixer.music.set_volume(volume_level)  # Set volume level
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def choose_music(music_label):
    global music_file_path  # Declare the global variable
    music_file_path = filedialog.askopenfilename(filetypes=(("MP3 files", "*.mp3"), ("All files", "*.*")))
    if music_file_path:
        if os.path.exists(music_file_path):
            music_filename = os.path.basename(music_file_path)  # Extract filename from full path
            music_label.config(text="Music File: " + music_filename)
        else:
            messagebox.showerror("Error", "Selected file does not exist.")
    return music_file_path


def show_popup():
    popup_window = tk.Tk()
    popup_window.attributes("-topmost", True)
    popup_window.withdraw()

    response = messagebox.showinfo("JAVRIS", "Hey SIR! Time to drink some water!\nRemember to stay hydrated!", master=popup_window)
    if response == "ok":
        stop_music()


def Wdr(root, interval, music_file_path, volume_level):
    play_reminder_music(music_file_path, volume_level)
    show_popup()
    # Schedule the next reminder after the specified interval
    root.after(interval * 1000, lambda: Wdr(root, interval, music_file_path, volume_level))



def set_interval(interval_label, interval_entry):
    interval_label.config(text="Interval (seconds): " + interval_entry.get())

def set_volume(volume_label, volume_scale):
    volume_label.config(text="Volume Level: " + str(volume_scale.get()))
    return volume_scale.get() / 100  # Convert volume scale to a value between 0 and 1

def start_reminder(root, interval_entry, music_label, volume_scale, volume_label):
    interval = int(interval_entry.get())
    volume_level = set_volume(volume_label, volume_scale)  # Pass volume_label here
    Wdr(root, interval, music_file_path, volume_level)


if __name__ == "__main__":
    # Create the main tkinter window
    root = tk.Tk()
    root.title("Water Drinking Reminder")
    root.config(background='skyblue')
    root.wm_iconbitmap('D:/python/Project/Water drinking reminder/Water-Drinking-reminder/1.ico')
    
    # Widgets
    interval_label = tk.Label(root, text="Interval (seconds): ", bg='skyblue', fg='black', font=('Times new roman',10,'bold'))
    interval_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
    
    interval_entry = tk.Entry(root)
    interval_entry.grid(row=0, column=1, padx=10, pady=5)
    
    set_interval_button = tk.Button(root, text="Set Interval", command=lambda: set_interval(interval_label, interval_entry), bg='skyblue', fg='black', font=('Times new roman',10,'bold'))
    set_interval_button.grid(row=0, column=2, padx=10, pady=5)
    
    music_label = tk.Label(root, text="Music File: No file selected", bg='skyblue', fg='black', font=('Times new roman',10,'bold'))
    music_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
    
    choose_music_button = tk.Button(root, text="Choose Music", command=lambda: choose_music(music_label),bg='skyblue', fg='black', font=('Times new roman',10,'bold'))
    choose_music_button.grid(row=1, column=1, padx=10, pady=5)
    
    volume_label = tk.Label(root, text="Volume Level: 100", bg='skyblue', fg='black', font=('Times new roman',10,'bold'))
    volume_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)
    
    volume_scale = ttk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
    volume_scale.set(100)  # Default volume level
    volume_scale.grid(row=2, column=1, columnspan=2, padx=10, pady=5)
    
    start_button = tk.Button(root, text="Start Reminder", bg='skyblue', fg='black', font=('Times new roman',10,'bold'), command=lambda: start_reminder(root,interval_entry, music_label, volume_scale, volume_label))
    start_button.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

    # Run the tkinter event loop
    root.mainloop()

