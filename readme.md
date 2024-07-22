# YouTube Video Sound Downloader and AI Summarizer 

## Introduction

The "YouTube Video Sound Downloader and AI Summarizer" project is a Python script that allows users to download audio from YouTube videos, transcribe their audio content using Whisper AI, and then summarize the transcript using natural language processing (NLP) techniques. The script uses PyTube to fetch video metadata, Whisper to transcribe the audio content, and NLP libraries (Ollama & Fabric) to generate summaries. The project consists of four main files: youtbue_downloader.py, main.py, whisper.py, and CreateSummary.bash. Everything is done locally on your computer.

Overall, this project provides a convenient way to download, transcribe, and summarize YouTube videos using Python and Whisper AI.

## Explanation of Files

### CreateSummary.bash

This shell script runs the main.py Python script, extracts the transcript filename from the output file, and then uses the filename as input to generate an AI summary using a pattern-based summarization approach. The script also saves the generated summary with the original filename appended with "_AI_Summary".

### main.py

This is the main entry point for the script. It prompts the user to enter a YouTube video link, creates an instance of the youtube_downloader class, and then uses it to download the audio content of the video. The script also includes functionality to transcribe the downloaded audio using Whisper AI.

### youtbue_downloader.py

This file defines a class youtube_downloader that takes a YouTube video URL as input and allows users to download the audio content of the video. The class uses PyTube to create a YouTube object, which can then be used to download the audio stream.

### whisper_ai.py

This file defines a whisper_ai class that allows users to transcribe audio files using the whisper model. It includes methods for loading the model and transcribing audio files.


## Key techonlogy
- Ollama
- Whisper
- Fabric
- Python
- Bash
- Linux 

## How to get started
1. Install [Ollama](https://ollama.com/)
2. Install [Fabric](https://github.com/danielmiessler/fabric/tree/main)
3. Install [Whisper](https://github.com/openai/whisper)
4. Download AI models from [ollama.com](https://ollama.com/library) with `ollama pull <model_name>` command
5. Start to run ollama locally `ollama serve`
6. Make `CreateSummary.bash` executable by running `chmod +x CreateSummary.bash`
7. Create a folder to where you want to save the summary
8. Edit `nano ~/.config/fabric/.env`
9. Add the following line: `FABRIC_OUTPUT_PATH="<Paht where you want fabric to store new files>"`
10. Run `./CreateSummary.bash`

