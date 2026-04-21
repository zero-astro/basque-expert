#!/usr/bin/env python3
"""
Itzune TTS Maider (Piper Version) 
Uses piper with the itzune/maider-tts model
"""

from piper.voice import PiperVoice
import io
import os
import sys

def synthesize_basque(text, model_path, output_path):
    # Piper TTS Python API erabiliz
    
    print(f"Synthesizing: '{text}'")
    
    # PiperVoice kargatu
    voice = PiperVoice.load(model_path)
    
    # Audioa sortu (generator bat itzultzen du)
    audio_generator = voice.synthesize(text)
    
    # Audioa bildu eta WAV fitxategian gorde
    buffer = io.BytesIO()
    for audio_chunk in audio_generator:
        sf.write(buffer, audio_chunk.audio_int16_array, audio_chunk.sample_rate, format='WAV')
    
    # Fitxategian idatzi
    with open(output_path, 'wb') as f:
        f.write(buffer.getvalue())
    
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python tts_maider.py <text> <output_path>")
        sys.exit(1)
        
    text = sys.argv[1]
    output_path = sys.argv[2]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    skill_dir = os.path.dirname(script_dir)

    model_path = os.path.join(skill_dir, "models", "tts", "eu-maider-medium.onnx")
    
    if not os.path.exists(model_path):
        print(f"Error: Model not found at {model_path}")
        sys.exit(1)
        
    synthesize_basque(text, model_path, output_path)
    print(f"Audio saved to {output_path}")
