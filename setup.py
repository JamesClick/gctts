from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="gctts",
    description="A simple way to generate high quality TTS MP3 files.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/JamesClick/gctts",
    author="J. Click",
    version="1.2",
    license="MIT",
    py_modules=["gctts"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=["Click", "requests"],
    entry_points="""
        [console_scripts]
        gctts=gctts:cli
    """,
)