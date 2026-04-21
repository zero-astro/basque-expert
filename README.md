# 🗣️ Basque Expert — Offline AI Language Tools

Offline Basque speech recognition and text-to-speech, powered by ONNX models. No API keys required.

## Features

- **ASR (Speech Recognition):** Transcribe audio files into Basque text using the Parakeet TDT 0.6B model
- **TTS (Text-to-Speech):** Convert Basque text to natural speech using the Maider voice model

Both run entirely offline — no internet connection needed after setup.

## Quick Start

### Prerequisites

A Python virtual environment is pre-configured at `scripts/venv/` with all dependencies:
- sherpa-onnx v1.12.39 (ASR engine)
- piper-tts v1.4.2 (TTS engine)

### Transcribe Audio → Text (ASR)

```bash
./scripts/venv/bin/python3 scripts/asr.py /path/to/audio.wav
```

Accepts WAV, MP3, FLAC, OGG and any format supported by `soundfile`. Outputs Basque text to stdout.
