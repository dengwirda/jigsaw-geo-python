from skbuild import setup, constants
from setuptools import find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize
import os
import sys
from glob import glob

CMAKE_INSTALL_DIR = os.path.dirname(os.path.abspath(__file__)) \
               + '/' + constants.CMAKE_INSTALL_DIR()
LIBRARY_PATH = CMAKE_INSTALL_DIR + '/jigsaw/lib'

headers = ["jigsawpy/cjigsaw/lib_jigsaw.pxd",
           "jigsawpy/cjigsaw/jigsaw_jig_t.pxd",
           "jigsawpy/cjigsaw/jigsaw_msh_t.pxd"]


extensions = []
for path in glob('jigsawpy/*.pyx'):
    name = path.split('/')[-1].split('.')[0]
    extensions.append(
        Extension("jigsawpy.{}".format(name),
                  [path, *headers],
                  libraries=['jigsaw'],
                  library_dirs=[LIBRARY_PATH]))

if "test" in sys.argv:
    for path in glob('tests/cjigsaw/*.pyx'):
        name = path.split('/')[-1].split('.')[0]
        extensions.append(
            Extension("jigsawpy.cjigsaw.tests.{}".format(name),
                      [path, *headers],
                      libraries=['jigsaw'],
                      library_dirs=[LIBRARY_PATH]))

setup(
    name="jigsawpy",
    packages=find_packages(),
    setup_requires=['cmake'],
    cmake_args=['-DCMAKE_BUILD_TYPE=Release'],
    ext_modules=cythonize(extensions),
    test_suite='nose.collector',
    tests_require=['nose'],
    install_requires=['matplotlib'],
    entry_points={
        'console_scripts': [
            '_jigsaw=jigsawpy.entrypoints._jigsaw:main'
        ]
    }
)
