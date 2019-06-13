from setuptools import setup, find_packages

version = '0.0.1'

setup(name='jigsawpy',
      version=version,
      description='JIGSAW(GEO): Mesh generation for geoscientific modellings.',
      url='https://github.com/dengwirda/jigsaw-geo-python',
      author='Darren Engwirda',
      author_email='de2363@columbia.edu',
      license='custom',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Operating System :: OS Independent',
          'Intended Audience :: Science/Research',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Topic :: Scientific/Engineering',
      ],
      packages=find_packages(),
      package_data={},
      install_requires=['numpy', 'pathlib'],
      entry_points={})
