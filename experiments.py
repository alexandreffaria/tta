import numpy as np
import random
import time
from prime import find_primes
from generateWAV import generateWAV

seconds = 10
sampleRate = 44100
frequency = 440

emptyArray = np.empty(sampleRate*seconds, dtype=np.int16)

sineWave = emptyArray

for i in range(len(sineWave)):
    sineWave[i] = np.sin(2 * np.pi * frequency * i / sampleRate)

sine_wave_normalized = np.int16(sineWave / np.max(np.abs(sineWave)) * 32767)

fullRandom = emptyArray

for i in range(len(fullRandom)):
    fullRandom[i] = random.randint(-32768, 32768)

linear = emptyArray

for i in range(-32768, 32768):
    linear[i] = i


sixteenBitsPrimes = find_primes(0,32768)


generateWAV("generated/440hz", sine_wave_normalized)
generateWAV("generated/random", fullRandom)
generateWAV("generated/linear", linear)
generateWAV("generated/primes", sixteenBitsPrimes)