import numpy as np
import wave
import struct

# Parameters
sample_rate = 44100  # Sample rate in Hz
duration = 20  # Duration in seconds
frequency = 880  # Frequency of the sine wave in Hz

t = np.linspace(start=0, stop=duration, num=int(sample_rate * duration * 2), endpoint=False)  # Time axis
audio_signal = (np.sin(2 * np.pi * frequency * t)).astype(np.float32)

# Convert audio signal to bytes
audio_bytes = struct.pack("%df" % len(audio_signal), *(audio_signal))

# Write to WAV file
with wave.open('sine_wave.wav', 'wb') as wav_file:
    wav_file.setnchannels(2)  # Mono
    wav_file.setsampwidth(4)  # Size of each sample in bytes
    wav_file.setframerate(sample_rate)
    wav_file.writeframes(audio_bytes)
