#!usr/bin/env python

import wave
import pyaudio
import numpy as np
import sys

FORMAT = pyaudio.paInt16
CHANNELS = 2 
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "file.wav"

audio = pyaudio.PyAudio()

#recording

stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
print "recording..."
frames = []

for i in range(0, int(RATE/CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print "finished"    


stream.stop_stream()
stream.close()
audio.terminate()

wavefile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wavefile.setnchannels(CHANNELS)
wavefile.setsampwidth(audio.get_sample_size(FORMAT))
wavefile.setframerate(RATE)
wavefile.writeframes(b''.join(frames))
wavefile.close()
