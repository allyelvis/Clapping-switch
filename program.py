import sounddevice as sd
import numpy as np

def detect_clap(threshold=0.5, duration=1):
    print("Clap detection started...")
    while True:
        recording = sd.rec(int(duration * 44100), samplerate=44100, channels=1, dtype='float64')
        sd.wait()
        amplitude = np.max(np.abs(recording))
        if amplitude > threshold:
            print("Clap detected!")
            # Do something when a clap is detected, like toggling a switch
        else:
            print("No clap detected.")

# Adjust threshold and duration as needed
detect_clap(threshold=0.3, duration=1)
