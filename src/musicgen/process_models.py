import os
import torchaudio
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write

from datetime import datetime
startTime = datetime.now()

FOLDER_NAME = f'ai-lofi-{startTime.strftime("%Y-%m-%d_%H-%M-%S")}'
os.makedirs(FOLDER_NAME)

MODELS = {
    "small": "facebook/musicgen-small",
    "melody": "facebook/musicgen-melody",
    "medium": "facebook/musicgen-medium",
    "large": "facebook/musicgen-large",
    "melody-large": "facebook/musicgen-melody-large",
    "stereo-small": "facebook/musicgen-stereo-small",
    "stereo-medium": "facebook/musicgen-stereo-medium",
    "stereo-melody": "facebook/musicgen-stereo-melody",
    "stereo-large": "facebook/musicgen-stereo-large",
    "stereo-melody-large": "facebook/musicgen-stereo-melody-large",
}

def generate_music(model_name: str, music_length: int, music_name: str, music_description: str):
    """
    Generate music from text
    """
    print(f"Getting model: {model_name}")
    model = MusicGen.get_pretrained(model_name)

    print(f"Setting duration: {music_length}")
    model.set_generation_params(duration=music_length)  
    
    print(f"Generating music {music_name} with the description: {music_description}")
    descriptions = [music_description]
    wav = model.generate(descriptions=descriptions,progress=True)   

    print(f"Saving audio file: {music_name}")
    for idx, one_wav in enumerate(wav):
    # Will save under {idx}.wav, with loudness normalization at -14 db LUFS.
        audio_write(f'{FOLDER_NAME}/{music_name}-{idx}', one_wav.cpu(), model.sample_rate, strategy="loudness", loudness_compressor=True)

def main():
    for k,v in MODELS.items():
        model_start = datetime.now()
        print(f'Processing with {v}')

        try:
            generate_music(v, 1, f'ai-song-00-{k}', 'mellow lofi beat with piano')
            print(f'model {k} : {v} took {datetime.now() - model_start}')
        except Exception as e:
            print(f"An error occurred: {e}")
            continue

    print(f"{len(MODELS)} models processed")
    print(datetime.now() - startTime)

    # Update metadata
    os.system(f"python metadata.py {FOLDER_NAME}")

    # Split out audio
    # os.system(f"python demucs.py {FOLDER_NAME}")

if __name__ == '__main__':
    main()