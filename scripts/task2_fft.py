import os
import sys
from pathlib import Path
from matplotlib import pyplot as plt

# make sure the repository root is on the path so imports work when
# running this file directly
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts import add_repo_root_to_path

add_repo_root_to_path()

from src.signal_generation import sum_sine_waves, add_noise
from src.fft_utils import compute_fft


def main(output_dir="results/figures"):
    os.makedirs(output_dir, exist_ok=True)

    fs = 1000
    duration = 2.0
    components = [(50, 1.0), (120, 0.5)]
    t, signal = sum_sine_waves(components, fs, duration)

    plt.figure()
    plt.plot(t, signal)
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.title("Two-sine signal")
    wave_path = os.path.join(output_dir, "task2_1_sum_two_sine_waves.png")
    plt.savefig(wave_path)
    plt.close()

    freqs, mag = compute_fft(signal, fs, full_range=True)
    plt.figure()
    plt.plot(freqs, mag)
    plt.xlim(0, fs)
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Magnitude")
    plt.title("FFT")
    spectrum_path = os.path.join(output_dir, "task2_2_normalized_spectrum.png")
    plt.savefig(spectrum_path)
    plt.close()

    noisy_signal = add_noise(signal, 0.5)
    plt.figure()
    plt.plot(t, noisy_signal)
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.title("Noisy signal")
    noisy_wave_path = os.path.join(output_dir, "task2_3_noisy_signal.png")
    plt.savefig(noisy_wave_path)
    plt.close()

    freqs_n, mag_n = compute_fft(noisy_signal, fs, full_range=True)
    plt.figure()
    plt.plot(freqs_n, mag_n)
    plt.xlim(0, fs)
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Magnitude")
    plt.title("FFT of noisy signal")
    noisy_spectrum_path = os.path.join(output_dir, "task2_4_noisy_spectrum.png")
    plt.savefig(noisy_spectrum_path)
    plt.close()

    return wave_path, spectrum_path, noisy_wave_path, noisy_spectrum_path


if __name__ == "__main__":
    main()
