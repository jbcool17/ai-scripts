import os
from pathlib import Path
import click
from pydub import AudioSegment
import taglib

# def add_metadata(file_path, title, artist, album):
#     audio = AudioSegment.from_file(file_path)

#     # Add metadata to the audio file
#     audio = audio.set_metadata({'title': title, 'artist': artist, 'album': album})

#     # Save the modified audio with metadata
#     audio.export(file_path, format="mp3")

def add_metadata(file_path, title, artist, album):
    with taglib.File(file_path, save_on_exit=True) as song:
        song.tags['artist'] = artist
        song.tags['title'] = title
        song.tags['album'] = album


@click.command()
@click.argument('directory', type=click.Path(exists=True, file_okay=False))
def add_metadata_cli(directory):
    """Add metadata to WAV and MP3 files in the specified directory."""
    directory = directory.rstrip("/")
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file.lower().endswith(('.wav', '.mp3')):
                title = os.path.splitext(file)[0]
                artist = "ai"
                album = os.path.basename(root)
                print(album)

                click.echo(f"\nFile: {file}")
                click.echo(f"Title: {title}")
                click.echo(f"Artist: {artist}")
                click.echo(f"Album: {album}")
                add_metadata(file_path, title, artist, album)
                click.echo("Metadata added successfully.")

if __name__ == '__main__':
    add_metadata_cli()
