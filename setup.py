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

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name="ai-scripts",  # Required
    version="1.0.0",  # Required
    description="A sample Python project",  # Optional
    long_description=long_description,  # Optional
    long_description_content_type="text/markdown",  # Optional (see note above)
    url="https://github.com/pypa/sampleproject",  # Optional
    author="A. Random Developer",  # Optional
    author_email="author@example.com",  # Optional
    # classifiers=[  # Optional
    #     # How mature is this project? Common values are
    #     #   3 - Alpha
    #     #   4 - Beta
    #     #   5 - Production/Stable
    #     "Development Status :: 3 - Alpha",
    #     # Indicate who your project is intended for
    #     "Intended Audience :: Developers",
    #     "Topic :: Software Development :: Build Tools",
    #     # Pick your license as you wish
    #     "License :: OSI Approved :: MIT License",
    #     # Specify the Python versions you support here. In particular, ensure
    #     # that you indicate you support Python 3. These classifiers are *not*
    #     # checked by 'pip install'. See instead 'python_requires' below.
    #     "Programming Language :: Python :: 3.9",
    #     "Programming Language :: Python :: 3.10",
    # ],
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
