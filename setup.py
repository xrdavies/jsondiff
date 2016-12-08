""" A simple JSON diff module to diff JSON object.
See:
https://github.com/xrdavies/jsondiff
"""

from setuptools import setup, find_packages
from codecs import open
from os import path
import jsondiff

here = path.abspath(path.dirname(__file__))

setup(
    name='jsondiff',

    version=jsondiff.__version__,

    description='A simple JSON diff module to diff JSON object',

    url='https://github.com/xrdavies/jsondiff',

    author='Rui Xie',
    author_email='xrdavies@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 1 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='json diff compare',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=['jsondiff',],

    install_requires=[],

    # List additional groups of dependencies here
    extras_require={},
)
