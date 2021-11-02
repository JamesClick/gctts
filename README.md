# This Game On Entertainment interview question is no longer to be used.
See: [https://documentation.in.goe/tech/interviewing#2022_protocol](https://documentation.in.goe/tech/interviewing#2022_protocol)

## Google Cloud Text To Speech CLI
### _Or, GCTTS for short_

## Purpose
I needed a quick way to generate high quality TTS mp3 clips.

## Usage:
    gctts mp3 --apikey=APIKEY FILENAME.mp3

## Installation:
Available on the PyPI registry. For most installations, use `pip3 install --user gctts`

## Lifehacks:
### Persistent API Key
Use the environment variable `GCTTS_APIKEY` to set the API key.
