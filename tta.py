import numpy as np
from scipy.io import wavfile
import random

seconds = 10
sampleRate = 44100
frequency = 440

sineWave = np.empty(44100*seconds)

for i in range(len(sineWave)):
    sineWave[i] = np.sin(2 * np.pi * frequency * i / sampleRate)

# Normalize to the range of int16
sine_wave_normalized = np.int16(sineWave / np.max(np.abs(sineWave)) * 32767)

fullRandom = np.empty(44100*seconds, dtype=np.int16)

for i in range(len(fullRandom)):
    fullRandom[i] = random.randint(-32768, 32768)
    print(fullRandom[i])

wavfile.write("sine_wave.wav", sampleRate, sine_wave_normalized)
wavfile.write("random_wave.wav", sampleRate, fullRandom)