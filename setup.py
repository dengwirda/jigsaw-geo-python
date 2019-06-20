
import io, os
import subprocess
import shutil
import pathlib

from setuptools import setup, find_packages
from distutils.command.build import build

NAME = "jigsawpy"
DESCRIPTION = \
    "Python interface for the JIGSAW meshing library."
AUTHOR = "Darren Engwirda"
AUTHOR_EMAIL = "darren.engwirda@columbia.edu"
URL = "https://github.com/dengwirda/"
VERSION = "0.0.2"
REQUIRES_PYTHON = ">=3.3.0"
KEYWORDS = "Mesh-generation Delaunay Voronoi"

REQUIRED = [
    "numpy", "pathlib"
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


class cmake_build(build):
    def run(self):
        """
        Call make_jigsaw before doing 'normal' things
        
        """
       
        self.make_jigsaw(); super().run()


    def make_jigsaw(self):
        """
        The actual cmake-based build steps for JIGSAW
        
        """
        
        if (self.dry_run): return

        cwd_pointer = os.getcwd()

        try:
            self.announce("cmake config.",level=3)

            source_path = str(
            pathlib.Path(here)/"xtern"/"jigsaw")

            builds_path = str(
            pathlib.Path(source_path) / "build")

            os.makedirs(builds_path,exist_ok=True)

            exesrc_path = str(
            pathlib.Path(source_path) /  "bin" )

            libsrc_path = str(
            pathlib.Path(source_path) /  "lib" ) 

            target_path = str(
                pathlib.Path(here) / "jigsawpy")

            exedst_path = str(
            pathlib.Path(target_path) / "_bin" )

            libdst_path = str(
            pathlib.Path(target_path) / "_lib" )

            shutil.rmtree(
                exedst_path,ignore_errors=True )
            shutil.rmtree(
                libdst_path,ignore_errors=True )

            os.chdir(builds_path)

            config_call = \
        ["cmake", "..","-DCMAKE_BUILD_TYPE=Release"]

            subprocess.run(config_call,check=True)

            self.announce("cmake complie",level=3)

            compilecall = \
        ["cmake","--build",".","--config","Release",
                               "--target","install"]

            subprocess.run(compilecall,check=True)

            self.announce("cmake cleanup",level=3)

            shutil.rmtree(builds_path)

            shutil.copytree(exesrc_path,exedst_path)
            shutil.copytree(libsrc_path,libdst_path)

        finally:
            os.chdir(cwd_pointer)


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
    keywords = KEYWORDS,    
    url = URL,
    packages = find_packages (),
    cmdclass={
        "build" : cmake_build,
        },
    package_data = {"jigsawpy":["_bin/*", "_lib/*"]
        },
    install_requires = REQUIRED,
    classifiers = CLASSIFY,
    entry_points = {}
)



