# Python Voice Assistant

A user-friendly voice-controlled assistant with a clean graphical interface built using Tkinter. This application allows users to manage tasks, search the web, and interact with their computer using simple voice commands.

---

## Features

### Speech Recognition
Processes voice commands using the `speech_recognition` module.

### Text-to-Speech
Provides audio responses using `gTTS` and `pyttsx3`.

### Knowledge Access
Retrieves quick summaries from Wikipedia.

### Media Control
Searches and plays music on YouTube using `pywhatkit`.

### Web Navigation
Allows quick access to websites like Google and YouTube.

### Entertainment
Includes a built-in joke generator using `pyjokes`.

### Utility Tools
- Check the current time  
- Set voice-activated alarms  

### Personalization
- Greets users by name  
- Adjusts greetings based on the time of day  

---

## Tech Stack and Modules

| Category              | Modules Used |
|----------------------|-------------|
| Voice Processing     | speech_recognition, gTTS, playsound, pyttsx3 |
| GUI Development      | tkinter, Pillow (PIL) |
| System and Utilities | os, webbrowser, datetime, threading, plyer |
| Data and Logic       | wikipedia, pywhatkit, pyjokes, dateparser |

---

## Setup and Installation

Make sure Python 3.x is installed, then run:

```bash
pip install pyttsx3 SpeechRecognition wikipedia-api pywhatkit plyer pillow gTTS playsound dateparser
```

```bash
python main.py
```
