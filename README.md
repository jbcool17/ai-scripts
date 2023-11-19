# ai-scripts

- Exploring ai

## Usage

https://github.com/facebookresearch/audiocraft

```
# LINUX - Linux pop-os 6.5.6
python -m venv .env
source .env/bin/activate

# xformers issue - https://github.com/facebookresearch/audiocraft/issues/105
pip install xformers --no-dependencies
pip install .

```

### MUSICGEN CLI

- simple cli that takes a prompt and generates music using the small model, inserting metadata and splitting out the tracks

```bash

 musicgen-cli --prompt "lofi guitar" --description 10
```

## todo

- add ffmpeg fade in / out
