import os
from flask import Flask, render_template, request, redirect, url_for
import pygame

app = Flask(__name__)

class MusicPlayer:
    def __init__(self):
        pygame.init()
        self.playlist = []
        self.current_song_index = 0
        self.paused = False
        self.volume = 0.5  # Initial volume level (0.0 to 1.0)

    def load_songs(self, folder_path):
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
        self.volume = float(volume)  # Convert to float
        pygame.mixer.music.set_volume(self.volume)
        print(f"Volume set to: {self.volume * 100}%")


player = MusicPlayer()

@app.route('/')
def index():
    return render_template('index.html', player=player)

@app.route('/load_songs', methods=['POST'])
def load_songs():
    folder_path = request.form['folder_path']
    player.load_songs(folder_path)
    return redirect(url_for('index'))

@app.route('/play')
def play():
    player.play()
    return redirect(url_for('index'))

@app.route('/pause')
def pause():
    player.pause()
    return redirect(url_for('index'))

@app.route('/resume')
def resume():
    player.resume()
    return redirect(url_for('index'))

@app.route('/stop')
def stop():
    player.stop()
    return redirect(url_for('index'))

@app.route('/next_song')
def next_song():
    player.next_song()
    return redirect(url_for('index'))

@app.route('/set_volume/<float:volume>')
def set_volume(volume):
    player.set_volume(volume)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)








