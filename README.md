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
- soundfile, numpy, scipy

### Transcribe Audio → Text (ASR)

```bash
./scripts/venv/bin/python3 scripts/asr.py /path/to/audio.wav
```

Accepts WAV, MP3, FLAC, OGG and any format supported by `soundfile`. Outputs Basque text to stdout.

### Text → Speech (TTS)

```bash
./scripts/venv/bin/python3 scripts/tts.py "Kaixo mundua!" output.wav
```

Outputs a WAV audio file with the Maider voice speaking your text in Basque.

## Model Details

| Component | Model | Size | Language |
|-----------|-------|------|----------|
| ASR | Parakeet TDT 0.6B (xezpeleta) | ~600MB | Basque |
| TTS | Maider (piper format) | ~100MB | Basque |

Models are stored in `models/` and loaded at runtime from ONNX files.

## Directory Structure

```
basque-expert/
├── SKILL.md          # OpenClaw skill definition
├── README.md         # This file
├── models/
│   ├── asr/          # ASR ONNX model files (encoder, decoder, joiner, tokens)
│   └── tts/          # TTS ONNX voice model (Maider)
├── scripts/
│   ├── venv/         # Python virtual environment with all dependencies
│   ├── asr.py        # ASR transcription script
│   └── tts.py        # TTS synthesis script
```

## Notes

- All processing is local — audio files never leave your machine
- Model loading takes ~5–10 seconds on first run (cached after)
- Recommended: 4+ CPU threads for best performance (ASR uses 4 by default)
