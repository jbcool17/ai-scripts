import click

from . import process_models


@click.command()
@click.option("-p", "--prompt", "prompt", default="lofi")
@click.option("-d", "--duration", "duration", default=5)
@click.option("-s", "--split-audio-disabled", "split_audio_disabled", is_flag=True)
def main(**kwargs):
    click.echo(kwargs)
    process_models.main(**kwargs)


if __name__ == "__main__":
    main()
