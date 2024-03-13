Here's a simple Python code for a clapping switch using the sounddevice library to record audio:import sounddevice as sd
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
detect_clap(threshold=0.3, duration=1)Make sure you have the sounddevice library installed (pip install sounddevice). This code listens for a clap sound by recording audio for a specified duration and then checks if the maximum amplitude exceeds a certain threshold. Adjust the threshold and duration parameters according to your environment and requirements.
