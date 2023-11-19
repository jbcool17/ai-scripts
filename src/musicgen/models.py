MODELS = {
    "test": {
        "small": "facebook/musicgen-small",
    },
    "mono": {
        "small": "facebook/musicgen-small",
        "medium": "facebook/musicgen-medium",
        "large": "facebook/musicgen-large",
    },
    "stereo": {
        "stereo-small": "facebook/musicgen-stereo-small",
        "stereo-medium": "facebook/musicgen-stereo-medium",
        "stereo-large": "facebook/musicgen-stereo-large",
    },
    "melody": {
        "mono": {
            "melody": "facebook/musicgen-melody",
            "melody-large": "facebook/musicgen-melody-large",
        },
        "stereo": {
            "stereo-melody": "facebook/musicgen-stereo-melody",
            "stereo-melody-large": "facebook/musicgen-stereo-melody-large",
        },
    },
}


def get_mono():
    return MODELS["mono"]


def get_stereo():
    return MODELS["stereo"]
