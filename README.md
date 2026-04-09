# Speech-to-Text with Whisper

## Overview

This example demonstrates how to convert spoken audio into text using a speech-to-text model.

Speech input is recorded from the microphone and transcribed into text using a pretrained model.

---

## Speech-to-Text (STT)

Speech-to-text systems convert audio signals into written language.

This is the first step in any voice-based AI system.

---

## Model Used

This example uses:

* Whisper

Whisper is an open-source speech recognition model capable of transcribing multiple languages with high accuracy.

---

## How It Works

1. Record audio from the microphone
2. Save audio to a file
3. Load a speech-to-text model
4. Transcribe audio into text

---

## Audio Recording

Audio is captured using the microphone and saved as a `.wav` file.

---

## Transcription

The model processes the audio file and outputs the recognized text.

---

## Installation

```bash
pip install openai-whisper sounddevice scipy
```

---

## Running the Example

```bash
python main.py
```

Speak during the recording window.

The script prints the transcribed text.

---

## Example Output

```text
what should i eat tonight
```

---

## Applications

* voice assistants
* transcription systems
* real-time speech interfaces
* conversational AI

---

## References

* Whisper
