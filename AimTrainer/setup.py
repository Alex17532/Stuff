"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['aimTrainer.py']
DATA_FILES = ["easy.txt", "hard.txt", "medium.txt", "metalHit.wav", "shoot.wav", "target.png"]
OPTIONS = {}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)