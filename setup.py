from setuptools import setup, find_packages
from codecs import open
from os import path
from envir import __version__

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'readme.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='envir',

    version=__version__,

    description='better way to load and format environment variables',
    long_description=long_description,

    url='https://github.com/kilerd/envir',

    author='Kilerd Chan',
    author_email='blove694@gmail.com',

    license='MIT',

    classifiers=[

        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='yai index package',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[],
)
