import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

fs = 44100
duration = 0.1  # small chunk

plt.ion()  # interactive mode

fig, (ax1, ax2) = plt.subplots(2, 1)

while True:
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()

    audio = audio.flatten()

    # Time axis
    t = np.linspace(0, duration, len(audio))

    # FFT
    fft = np.fft.fft(audio)
    freqs = np.fft.fftfreq(len(audio), 1/fs)

    positive_freqs = freqs[:len(freqs)//2]
    magnitude = np.abs(fft[:len(fft)//2])

    # Clear plots
    ax1.clear()
    ax2.clear()

    # Plot waveform
    ax1.plot(t, audio)
    ax1.set_title("Real-Time Signal")

    # Plot FFT
    ax2.plot(positive_freqs, magnitude)
    ax2.set_title("Real-Time Frequency Spectrum")

    plt.pause(0.01)