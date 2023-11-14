# Audio-Based Question and Answer System

## Overview
This project is an audio-based question and answer system that utilizes various technologies for speech recognition, text processing, and text-to-speech conversion. It employs Whisper for speech recognition, OpenAI for text processing, and gTTS for text-to-speech conversion. The system operates with multithreading, allowing concurrent tasks such as audio recording, transcription, and response handling.

## Installation
Before using the system, ensure that you have all the required dependencies installed on your system. You can install missing dependencies using pip. The following command will install the necessary dependencies:

```bash
pip install pydub pyaudio speechrecognition whisper torch numpy gtts openai click
```
## Multithreding
The script employs multithreading to handle different tasks concurrently:

1. Audio Recording: One thread continuously records audio input from the microphone.

2. Transcribing and Responding: Another thread transcribes the recorded audio, detects a wake word, and sends the transcribed text to OpenAI for generating responses. If the wake word is detected, it triggers a response.

3. Generating and Playing Audio Response: A third thread takes the generated response, saves it to a text file for reference, and converts it to audio using the Google Text-to-Speech (gTTS) library. The audio response is then played back.

## Usage
1. Run the script.

2. Start speaking, and the system will continuously listen for your input.
  
3. If you want to terminate the script, say "stop" or "exit." This will set the running flag to False, causing the threads to exit gracefully.

## Files and Folders
main.py: The main script that orchestrates the audio-based question and answer system.

.env: A local file containing the OpenAI API key.

README.md: This documentation file.

requirements.txt: A file listing the project's dependencies.

## Dependencies
pydub: Audio processing library.

pyaudio: Library for audio input/output.

speechrecognition: Speech recognition library.

whisper: Speech recognition engine.

torch: PyTorch library.

numpy: Numerical computing library.

gtts: Google Text-to-Speech library.

openai: OpenAI Python library.

click: Command-line interface library.


## Execute the Script: 

```bash
python3 week07_03.py --model base --english --energy 300 --pause 0.8 --dynamic_energy --wake_word "hey computer" –verbose
```


