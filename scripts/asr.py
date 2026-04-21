#!/usr/bin/env python3
"""
Parakeet TDT 0.6B Basque Transcription Script
Uses sherpa-onnx with the xezpeleta/parakeet-tdt-0.6b-v3-basque-sherpa-onnx model
"""

import sys
import os
import sherpa_onnx


def transcribe(audio_path: str) -> str:
    """Transcribe audio file using Parakeet TDT model."""
    
    # Model path - use the directory with actual ONNX files
    script_dir = os.path.dirname(os.path.abspath(__file__))
    skill_dir = os.path.dirname(script_dir)
    model_dir = os.path.join(skill_dir, "models", "asr")
    
    if not os.path.exists(model_dir):
        raise FileNotFoundError(f"Model directory not found: {model_dir}")
    
    # Create recognizer with Parakeet TDT model using explicit file paths
    recognizer = sherpa_onnx.OfflineRecognizer.from_transducer(
        encoder=f"{model_dir}/encoder.int8.onnx",
        decoder=f"{model_dir}/decoder.int8.onnx",
        joiner=f"{model_dir}/joiner.int8.onnx",
        tokens=f"{model_dir}/tokens.txt",
        num_threads=4,
        decoding_method="greedy_search",
        model_type="nemo_transducer"
    )
    
    # Load audio and create stream
    stream = recognizer.create_stream()
    
    # Read audio file
    import soundfile as sf
    samples, sample_rate = sf.read(audio_path)
    
    # Convert to mono if stereo
    if len(samples.shape) > 1:
        samples = samples.mean(axis=1)
    
    # Feed audio to stream (sherpa expects float32, 16kHz)
    if sample_rate != 16000:
        import numpy as np
        from scipy.signal import resample
        target_samples = int(len(samples) * 16000 / sample_rate)
        samples = resample(samples, target_samples)
    
    stream.accept_waveform(
        sherpa_onnx.AudioData(
            samples=samples.astype(np.float32),
            sample_rate=16000
        )
    )
    
    # Decode
    recognizer.decode_stream(stream)
    
    return stream.result.text


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python asr.py <audio_path>", flush=True)
        sys.exit(1)
    
    audio_file = sys.argv[1]
    
    if not os.path.exists(audio_file):
        print(f"Error: File {audio_file} not found", flush=True)
        sys.exit(1)
    
    try:
        text = transcribe(audio_file)
        print(text, flush=True)
    except Exception as e:
        print(f"Error during transcription: {e}", file=sys.stderr, flush=True)
        import traceback
        traceback.print_exc()
        sys.exit(1)
