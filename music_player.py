import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self):
        pygame.init()
        self.playlist = []
        self.current_song_index = 0
        self.paused = False
        self.volume = 0.5  # Initial volume level (0.0 to 1.0)

    def load_songs(self, folder_path):
        # Load all MP3 files from the specified folder
        self.playlist = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.lower().endswith('.mp3')]
        if not self.playlist:
            print("No MP3 files found in the specified folder.")

    def play(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_song_index])
            pygame.mixer.music.set_volume(self.volume)
            pygame.mixer.music.play()

    def pause(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.paused = True
            print("Paused")

    def resume(self):
        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
            print("Resumed")

    def stop(self):
        pygame.mixer.music.stop()
        print("Stopped")

    def next_song(self):
        self.current_song_index = (self.current_song_index + 1) % len(self.playlist)
        self.play()

    def set_volume(self, volume):
        self.volume = volume
        pygame.mixer.music.set_volume(volume)
        print(f"Volume set to: {volume * 100}%")

class MusicPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")

        self.player = MusicPlayer()

        self.folder_path_var = tk.StringVar()

        # Entry for folder path
        entry_label = tk.Label(root, text="Enter Folder Path:")
        entry_label.pack(pady=5)
        folder_entry = tk.Entry(root, textvariable=self.folder_path_var, width=40)
        folder_entry.pack(pady=5)
        browse_button = tk.Button(root, text="Browse", command=self.browse_folder)
        browse_button.pack(pady=5)

        # Volume control
        volume_label = tk.Label(root, text="Volume:")
        volume_label.pack(pady=5)
        volume_slider = tk.Scale(root, from_=0.0, to=1.0, resolution=0.1, orient=tk.HORIZONTAL, command=self.set_volume)
        volume_slider.set(self.player.volume)
        volume_slider.pack(pady=5)

        # Control buttons
        play_button = tk.Button(root, text="Play", command=self.player.play)
        play_button.pack(pady=5)
        pause_button = tk.Button(root, text="Pause", command=self.player.pause)
        pause_button.pack(pady=5)
        resume_button = tk.Button(root, text="Resume", command=self.player.resume)
        resume_button.pack(pady=5)
        stop_button = tk.Button(root, text="Stop", command=self.player.stop)
        stop_button.pack(pady=5)
        next_button = tk.Button(root, text="Next Song", command=self.player.next_song)
        next_button.pack(pady=5)

    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        self.folder_path_var.set(folder_path)
        self.player.load_songs(folder_path)

    def set_volume(self, volume):
        self.player.set_volume(float(volume))

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayerApp(root)
    root.mainloop()



