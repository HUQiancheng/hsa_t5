import os
import sys
import numpy as np
import soundfile as sf
from matplotlib import pyplot as plt

# Ensure imports work when running the script directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.correlation_utils import cross_correlation
from src.signal_generation import add_noise
from src.fft_utils import compute_fft


def main(fig_dir="results/figures", audio_dir="results/audio", delay=0.005, scale=0.8):
    os.makedirs(fig_dir, exist_ok=True)
    os.makedirs(audio_dir, exist_ok=True)

    data, fs = sf.read("data/chimes.wav")
    if data.ndim > 1:
        mono = data[:, 0]
    else:
        mono = data
    t = np.arange(len(mono)) / fs

    plt.figure()
    plt.plot(t, mono)
    plt.xlabel("Time [s]")
    plt.title("Chimes channel")
    orig_path = os.path.join(fig_dir, "task3_1_original_signal.png")
    plt.savefig(orig_path)
    plt.close()

    freqs, mag = compute_fft(mono, fs)
    plt.figure()
    plt.plot(freqs, mag)
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Magnitude")
    plt.title("FFT of chimes")
    fft_path = os.path.join(fig_dir, "task3_2_chimes_fft.png")
    plt.savefig(fft_path)
    plt.close()

    delay_samples = int(delay * fs)
    left = mono
    right = np.roll(mono, delay_samples) * scale
    stereo = np.stack([left, right], axis=1)
    stereo_path = os.path.join(audio_dir, "stereo_example.wav")
    sf.write(stereo_path, stereo, fs)

    plt.figure()
    plt.plot(t, left, label="Left channel")
    plt.plot(t, right, label="Right channel", alpha=0.7)
    plt.legend()
    plt.xlabel("Time [s]")
    plt.title("Stereo signals")
    stereo_fig_path = os.path.join(fig_dir, "task3_4_signal_with_scaling_and_delay.png")
    plt.savefig(stereo_fig_path)
    plt.close()

    lags, corr = cross_correlation(left, right)
    plt.figure()
    plt.plot(lags / fs, corr)
    plt.xlabel("Delay [s]")
    plt.ylabel("Correlation")
    plt.title("Cross-correlation")
    corr_fig = os.path.join(fig_dir, "task3_6_cross_correlation.png")
    plt.savefig(corr_fig)
    plt.close()

    left_n = add_noise(left, 0.1)
    right_n = add_noise(right, 0.1)
    lags_n, corr_n = cross_correlation(left_n, right_n)
    plt.figure()
    plt.plot(lags_n / fs, corr_n)
    plt.xlabel("Delay [s]")
    plt.ylabel("Correlation")
    plt.title("Cross-correlation with noise")
    noisy_corr_fig = os.path.join(fig_dir, "task3_8_cross_correlations.png")
    plt.savefig(noisy_corr_fig)
    plt.close()

    return stereo_path, orig_path, fft_path, stereo_fig_path, corr_fig, noisy_corr_fig


if __name__ == "__main__":
    main()
