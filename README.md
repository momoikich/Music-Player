

# Music Player Dashboard

## Overview

The Music Player Dashboard is a web-based application that allows users to manage and play their music collection. It provides a user-friendly interface to load songs, control playback, adjust volume, and navigate through the playlist.

## Features

- Load songs from a specified folder.
- Play, pause, resume, stop, and skip to the next song.
- Volume control with a slider.
- Real-time updates on the playlist.

## Prerequisites

- Python 3.12
- Flask
- Pygame

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/momoikich/Music-Player.git
   cd Music-Player
   ```

2. Install the required dependencies:

   ```bash
   pip install Flask pygame
   ```

## Usage

1. Run the application:

   ```bash
   python music_player.py
   ```

2. Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

3. Use the provided controls to load songs, play, pause, resume, stop, and navigate the playlist.

## Folder Structure

```plaintext
/
|-- music_player.py
|-- templates/
|   |-- index.html
|-- static/
|   |-- css
|       |-- style.css
|   |-- img
|       |-- melody-hub.jpeg
```

- `music_player.py`: Main Python script containing the Flask application.
- `templates/`: Folder containing HTML templates.
- `static/`: Folder containing css file styles and images.

## Customization

Feel free to customize the application further to suit your needs. You can modify the HTML templates, add additional features, or enhance the user interface.

## Acknowledgments

This project uses Flask for web development and Pygame for audio playback.

## License

This project is licensed under the [MIT License](LICENSE).