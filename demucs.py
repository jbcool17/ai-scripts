import os
from pathlib import Path
import click

@click.command()
@click.argument('directory', type=click.Path(exists=True, file_okay=False))
def demucs(directory):
    """Split out audio tracks"""
    directory = directory.rstrip("/")
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file.lower().endswith(('.wav', '.mp3')):                
                os.system(f'demucs -o {directory} {file_path}')
                click.echo("split successfully.")
if __name__ == '__main__':
    demucs()
