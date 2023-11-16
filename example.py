import os
import torchaudio
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write

from datetime import datetime
startTime = datetime.now()

FOLDER_NAME = f'ai-lofi-{startTime.strftime("%Y-%m-%d_%H-%M-%S")}'
os.makedirs(FOLDER_NAME)

models = {
    "small": "facebook/musicgen-small",
    # "melody": "facebook/musicgen-melody",
    # "medium": "facebook/musicgen-medium",
    # "large": "facebook/musicgen-large",
    # "melody-large": "facebook/musicgen-melody-large",
    # "stereo-small": "facebook/musicgen-stereo-small",
    # "stereo-medium": "facebook/musicgen-stereo-medium",
    # "stereo-melody": "facebook/musicgen-stereo-melody",
    # "stereo-large": "facebook/musicgen-stereo-large",
    # "stereo-melody-large": "facebook/musicgen-stereo-melody-large",
}

def generate_music(model_name: str, music_length: int, music_name: str, music_description: str):
    """
    Generate music from text
    """
    print(f"Getting model: {model_name}")
    model = MusicGen.get_pretrained(model_name)
    print(f"Setting duration: {music_length}")
    model.set_generation_params(duration=music_length)  
    descriptions = [music_description]
    print(f"Generating music {music_name} with the description: {music_description}")
    wav = model.generate(descriptions)

    print(f"Saving audio file: {music_name}")
    for idx, one_wav in enumerate(wav):
    # Will save under {idx}.wav, with loudness normalization at -14 db LUFS.
        audio_write(f'{FOLDER_NAME}/{music_name}-{idx}', one_wav.cpu(), model.sample_rate, strategy="loudness", loudness_compressor=True)

for k,v in models.items():
    model_start = datetime.now()
    print(f'Processing with {v}')
    generate_music(v, 10, f'ai-song-00-{k}', 'mellow lofi beat with piano')
    print(f'model {k} : {v} took {datetime.now() - model_start}')

print(f"{len(models)} models processed")
print(datetime.now() - startTime)

# Update metadata
os.system(f"python metadata.py {FOLDER_NAME}")

# Split out audio
os.system(f"python demucs.py {FOLDER_NAME}")