---
name: basque-expert
description: Basque language AI tools — speech recognition (ASR) and text-to-speech (TTS). Use when the user needs to transcribe audio files into Basque text or convert Basque text into spoken audio. ASR uses sherpa-onnx with Parakeet TDT model; TTS uses piper with Maider voice.
---

# Basque Expert Skill

## Overview

Provides offline Basque speech recognition (ASR) and text-to-speech (TTS) capabilities using ONNX models.

**ASR:** Transcribe audio files to Basque text via sherpa-onnx + Parakeet TDT 0.6B model
**TTS:** Convert Basque text to speech via piper + Maider voice model

## Usage

### ASR (Speech Recognition)

```bash
/home/urtzai/.openclaw/skills/basque-expert/scripts/venv/bin/python3 /home/urtzai/.openclaw/skills/basque-expert/scripts/asr.py <audio_path>
```

- Accepts any audio format supported by soundfile (WAV, MP3, FLAC, OGG, etc.)
- Outputs transcribed Basque text to stdout
- Requires: sherpa-onnx v1.12.39 + soundfile in venv

### TTS (Text-to-Speech)

```bash
/home/urtzai/.openclaw/skills/basque-expert/scripts/venv/bin/python3 /home/urtzai/.openclaw/skills/basque-expert/scripts/tts.py "<text>" <output_path>
```

- Accepts Basque text as input
- Outputs WAV audio file to specified path
- Requires: piper-tts v1.4.2 in venv

## Model Paths

- ASR models: `/home/urtzai/.openclaw/skills/basque-expert/models/asr/`
  - encoder.int8.onnx, decoder.int8.onnx, joiner.int8.onnx, tokens.txt
- TTS model: `/home/urtzai/.openclaw/skills/basque-expert/models/tts/eu-maider-medium.onnx`

## Dependencies (venv)

All dependencies are installed in the virtual environment at `scripts/venv/`. Do not install packages globally.
