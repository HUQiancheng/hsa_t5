import os
import numpy as np
import soundfile as sf
from matplotlib import pyplot as plt
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
    plt.savefig(os.path.join(fig_dir, "chimes_channel.png"))
    plt.close()

    freqs, mag = compute_fft(mono, fs)
    plt.figure()
    plt.plot(freqs, mag)
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Magnitude")
    plt.title("FFT of chimes")
    plt.savefig(os.path.join(fig_dir, "chimes_fft.png"))
    plt.close()

    delay_samples = int(delay * fs)
    left = mono
    right = np.roll(mono, delay_samples) * scale
    stereo = np.stack([left, right], axis=1)
    stereo_path = os.path.join(audio_dir, "stereo_example.wav")
    sf.write(stereo_path, stereo, fs)

    plt.figure()
    plt.plot(t, left, label="left")
    plt.plot(t, right, label="right", alpha=0.7)
    plt.legend()
    plt.xlabel("Time [s]")
    plt.title("Stereo signals")
    plt.savefig(os.path.join(fig_dir, "stereo_signals.png"))
    plt.close()

    lags, corr = cross_correlation(left, right)
    plt.figure()
    plt.plot(lags / fs, corr)
    plt.xlabel("Delay [s]")
    plt.ylabel("Correlation")
    plt.title("Cross-correlation")
    plt.savefig(os.path.join(fig_dir, "correlation.png"))
    plt.close()

    left_n = add_noise(left, 0.1)
    right_n = add_noise(right, 0.1)
    lags_n, corr_n = cross_correlation(left_n, right_n)
    plt.figure()
    plt.plot(lags_n / fs, corr_n)
    plt.xlabel("Delay [s]")
    plt.ylabel("Correlation")
    plt.title("Cross-correlation with noise")
    noisy_corr_path = os.path.join(audio_dir, "noisy_correlation.png")
    plt.savefig(noisy_corr_path)
    plt.close()

    return stereo_path, noisy_corr_path


if __name__ == "__main__":
    main()
