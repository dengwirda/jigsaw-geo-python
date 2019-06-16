
import io
import os

from setuptools import setup, find_packages

NAME = "jigsawpy"
DESCRIPTION = \
    "Python interface for the JIGSAW meshing library."
AUTHOR = "Darren Engwirda"
AUTHOR_EMAIL = "darren.engwirda@columbia.edu"
URL = "https://github.com/dengwirda/"
VERSION = "0.0.1"
REQUIRES_PYTHON = ">=3.3.0"

REQUIRED = [
    "numpy", "pathlib", "matplotlib"
]

CLASSIFY = [
    "Development Status :: 3 - Alpha",
    "Operating System :: OS Independent",
    "Intended Audience :: Science/Research",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Topic :: Scientific/Engineering",
    "Topic :: Scientific/Engineering :: Mathematics",
    "Topic :: Scientific/Engineering :: Physics",
    "Topic :: Scientific/Engineering :: Visualization"
]

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join( \
        here,"README.md"),encoding="utf-8") as f:
        LONG_DESCRIPTION = "\n"+f.read()

except FileNotFoundError:
    LONG_DESCRIPTION = DESCRIPTION

setup(
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    long_description_content_type = "text/markdown",
    license = "custom",    
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    python_requires = REQUIRES_PYTHON,
    url = URL,
    packages = find_packages(),
    package_data = {},    
    install_requires = REQUIRED,
    classifiers = CLASSIFY,
    entry_points = {}
)



