import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
import pygame
import eyed3

app = Flask(__name__)

class MusicPlayer:
    def __init__(self):
        pygame.init()
        self.playlist = []
        self.current_song_index = 0
        self.paused = False
        self.volume = 0.5
        self.paused_data = None

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
        self.volume = float(volume)
        pygame.mixer.music.set_volume(self.volume)
        print(f"Volume set to: {self.volume * 100}%")

    def get_total_duration(self):
        if self.playlist:
            audiofile = eyed3.load(self.playlist[self.current_song_index])
            if audiofile:
                return int(audiofile.info.time_secs)
        return 0

    def get_current_progress(self):
        if self.playlist and pygame.mixer.music.get_busy():
            return pygame.mixer.music.get_pos() / 1000
        return 0

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
    current_progress = player.get_current_progress()
    player.pause()
    total_duration = player.get_total_duration()
    player.paused_data = {'progress': current_progress, 'duration': total_duration}
    return jsonify(player.paused_data)

@app.route('/resume')
def resume():
    if player.paused_data:
        player.resume()
    return jsonify(player.paused_data)

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

@app.route('/progress', methods=['GET'])
def progress():
    if player.paused and player.paused_data:
        # If paused, return the last known progress
        return jsonify(progress=player.paused_data['progress'], duration=player.paused_data['duration'])
    
    # Retrieve the current progress and duration from your music player or server
    current_progress = player.get_current_progress()
    total_duration = player.get_total_duration()

    # Return the progress and duration as JSON
    return jsonify(progress=current_progress, duration=total_duration)


if __name__ == '__main__':
    app.run(debug=True)









