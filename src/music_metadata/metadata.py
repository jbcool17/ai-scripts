import os

import taglib


def add_metadata(file_path, title, artist, album):
    with taglib.File(file_path, save_on_exit=True) as song:
        song.tags["artist"] = artist
        song.tags["title"] = title
        song.tags["album"] = album


def process_directory(directory):
    """Add metadata to WAV and MP3 files in the specified directory."""
    directory = directory.rstrip("/")
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file.lower().endswith((".wav", ".mp3")):
                title = os.path.splitext(file)[0]
                artist = "ai"
                album = os.path.basename(root)
                add_metadata(file_path, title, artist, album)
                print("Metadata added successfully.")
