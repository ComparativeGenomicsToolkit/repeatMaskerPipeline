from setuptools import setup, find_packages
from setuptools.command.install import install
import os, sys
import subprocess


setup(
    name = "repeatMaskerPipeline",
    version = "0.1",
    author = "Joel Armstrong",
    package_dir = {'': 'src'},
    packages = find_packages(where='src'),
    include_package_data = True,
    package_data = {
        'repeatMaskerPipeline': []
    },
    # We use the __file__ attribute so this package isn't zip_safe.
    zip_safe = False,

    python_requires = '>=3.6',

    install_requires = [],

    entry_points= {
        'console_scripts': ['repeatMaskerPipeline = repeatMaskerPipeline.repeatMaskerPipeline:main']},)
