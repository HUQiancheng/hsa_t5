import os
import sys
from matplotlib import pyplot as plt

# Ensure imports work when running the script directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.signal_generation import sum_sine_waves, add_noise
from src.fft_utils import compute_fft


def main(output_dir="results/figures"):
    os.makedirs(output_dir, exist_ok=True)

    fs = 1000
    duration = 2.0
    components = [(50, 1.0), (120, 0.5)]
    t, signal = sum_sine_waves(components, fs, duration)

    # plot waveform
    plt.figure()
    plt.plot(t, signal)
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.title("Two-sine signal")
    wave_path = os.path.join(output_dir, "task2_waveform.png")
    plt.savefig(wave_path)
    plt.close()

    # FFT of clean signal
    freqs, mag = compute_fft(signal, fs)
    plt.figure()
    plt.plot(freqs, mag)
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Magnitude")
    plt.title("FFT")
    spectrum_path = os.path.join(output_dir, "task2_spectrum.png")
    plt.savefig(spectrum_path)
    plt.close()

    # Noisy signal and FFT
    noisy_signal = add_noise(signal, 0.5)
    freqs_n, mag_n = compute_fft(noisy_signal, fs)
    plt.figure()
    plt.plot(freqs_n, mag_n)
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Magnitude")
    plt.title("FFT with noise")
    noisy_spectrum_path = os.path.join(output_dir, "task2_noisy_spectrum.png")
    plt.savefig(noisy_spectrum_path)
    plt.close()

    return wave_path, spectrum_path, noisy_spectrum_path


if __name__ == "__main__":
    main()
