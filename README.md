# Whisper Writer Overview
==========================

Whisper Writer is a program that records audio and uses the Whisper model to recognize speech. This document provides a technical overview of the program for other programmers.

## Important Functions

### `record_audio()`

This function records audio from the user's microphone. It uses the `pyaudio` library to open a stream and read audio data from the microphone. The function continues to record audio until the user presses the 's' key to stop recording or the 'q' key to quit the program.

### `recognize_speech(frames)`

This function takes the recorded audio data and uses the Whisper model to recognize speech. It creates a WAV file in memory using the `io` and `wave` libraries, and then passes this file to the Whisper model using the `replicate` library. The function prints the output from the Whisper model, which is the recognized text.

## Program Flow

The program starts by calling the `record_audio()` function, which records audio from the user's microphone. Once the user stops recording or quits the program, the `record_audio()` function calls the `recognize_speech()` function, passing in the recorded audio data. The `recognize_speech()` function then uses the Whisper model to recognize speech and prints the output.
