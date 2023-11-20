import os
from datetime import datetime

from audiocraft.data.audio import audio_write
from audiocraft.models import MusicGen

from music_metadata import metadata
from musicgen.models import MODELS
from split_audio import cli as split_audio

MODELS = MODELS["test"]


def generate_music(model_name: str, music_length: int, music_name: str, music_description: str, folder_name: str):
    """
    Generate music from text
    """
    print(f"Getting model: {model_name}")
    model = MusicGen.get_pretrained(model_name)

    print(f"Setting duration: {music_length}")
    model.set_generation_params(duration=music_length)

    print(f"Generating music {music_name} with the description: {music_description}")
    descriptions = [music_description]
    wav = model.generate(descriptions=descriptions, progress=True)

    print(f"Saving audio file: {folder_name}/{music_name}")
    for idx, one_wav in enumerate(wav):
        # Will save under {idx}.wav, with loudness normalization at -14 db LUFS.
        audio_write(
            f"{folder_name}/{music_name}-{idx}",
            one_wav.cpu(),
            model.sample_rate,
            strategy="loudness",
            loudness_compressor=True,
        )


def main(prompt: str, duration: int, split_audio_disabled: bool):
    startTime = datetime.now()

    folder_name = f'ai-lofi-{startTime.strftime("%Y-%m-%d_%H-%M-%S")}'
    os.makedirs(folder_name)
    models_processed = 0

    with open(f"{folder_name}/details.txt", "w") as details:
        details.write(f"{prompt} \n")

    for k, v in MODELS.items():
        print()
        model_start = datetime.now()
        print(f"Processing with {v}")

        try:
            generate_music(v, duration, f"ai-song-00-{k}", prompt, folder_name)
            model_duration = datetime.now() - model_start
            print(f"SUCCESS: model {k} : {v} took {model_duration}")
            models_processed += 1

            with open(f"{folder_name}/details.txt", "a") as details:
                details.write("--- \n")
                details.write(f"model {k} : {v} took {model_duration} \n")

        except Exception as e:
            print(f"An error occurred: {e}")
            continue

    total_duration = datetime.now() - startTime
    print(f"{models_processed} models processed")
    print(total_duration)

    with open(f"{folder_name}/details.txt", "a") as details:
        details.write(f"total duration: {total_duration} \n")

    # Update metadata
    # os.system(f"python src/metadata.py {folder_name}")
    metadata.process_directory(folder_name)

    # Split out audio
    # os.system(f"split-audio {folder_name}")
    if not split_audio_disabled:
        split_audio.split_audio_in_directory([folder_name])

    print()
    print(f"Check files in the follow directory: {folder_name}")


if __name__ == "__main__":
    main()
