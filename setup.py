"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

import pathlib

import pkg_resources

# Always prefer setuptools over distutils
from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")


requirements_txt = pathlib.Path("requirements.txt").read_text()
requirements = list(map(str, pkg_resources.parse_requirements(requirements_txt)))

setup(
    name="ai-scripts",  # Required
    version="1.0.0",  # Required
    description="Exploring AI",
    url="https://github.com/jbcool17/ai-scripts",  # Optional
    author="John Brilla",
    package_dir={"": "src"},  # Optional
    packages=find_packages(where="src"),  # Required
    python_requires=">=3.9",
    install_requires=requirements,  # Optional
    entry_points={  # Optional
        "console_scripts": [
            "split-audio=split_audio.cli:split_audio_in_directory",
            "process-models=musicgen.process_models:main",
            "musicgen-cli=musicgen.cli:main",
        ],
    },
)
