# Whisper Writer

A simple program that uses OpenAI's Whisper model hosted by Replicate.com to transcribe audio.

## Requirements

* Python 3.x
* `requirements.txt` installed using pip (recommended to use a virtual environment)
* PyAudio installed with additional requirements (see PyAudio documentation)
* REPLICATE_API_TOKEN environment variable set (see below)
* I could not run this in WSL because of audio input complication, powershell7 was fine though

## Installation

1. Create a virtual environment using your preferred method (e.g. `uv venv` and then `. .venv/bin/activate` on Linux).
2. Install the requirements using pip: `pip install -r requirements.txt`.
3. Install PyAudio with additional requirements (see PyAudio documentation).
4. Set the REPLICATE_API_TOKEN environment variable:
	* On Linux: `export REPLICATE_API_TOKEN=YOUR_API_TOKEN`
	* On Windows: `set REPLICATE_API_TOKEN=YOUR_API_TOKEN` (in Command Prompt) or `$env:REPLICATE_API_TOKEN = 'YOUR_API_TOKEN'` (in PowerShell)

## Usage

1. Run the program using Python: `python whisper_writer.py`.
2. Press 'r' to start recording, 's' to stop recording, and 'q' to quit.
3. The program will print out the transcription.

## Notes

* This program uses OpenAI's Whisper model hosted by Replicate.com. Please check the Replicate.com website for more information: https://replicate.com/openai/whisper?input=python.
* Make sure to replace `YOUR_API_TOKEN` with your actual REPLICATE_API_TOKEN.
