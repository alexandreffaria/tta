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

nice = emptyArray
for i in range(len(nice) - 1):
    if i % 2 == 0:
        nice[i] = 15000
    else:
        nice[i] = -15000

generateWAV("generated/nice", nice)

# generateWAV("generated/4g40hz", sine_wave_normalized)
# generateWAV("generated/random", fullRandom)
# generateWAV("generated/linear", linear)
# generateWAV("generated/primes", sixteenBitsPrimes)
