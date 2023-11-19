import os

import click
import demucs.separate


@click.command()
@click.argument("directory", type=click.Path(exists=True, file_okay=False))
def split_audio_in_directory(directory):
    """Split out audio tracks"""
    directory = directory.rstrip("/")
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file.lower().endswith((".wav", ".mp3")):
                click.echo(f"Processing {file_path}")
                # os.system(f'demucs -o {directory} {file_path}')
                demucs.separate.main(["-o", directory, "-n", "mdx_extra", file_path])
                click.echo("split successfully.")


if __name__ == "__main__":
    split_audio_in_directory()
