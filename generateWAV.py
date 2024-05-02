from scipy.io import wavfile

sampleRate = 44100

def generateWAV(filename, normalizedArray):
    wavfile.write(filename + ".wav", sampleRate, normalizedArray)
