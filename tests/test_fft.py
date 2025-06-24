import numpy as np
from src.signal_generation import sum_sine_waves
from src.fft_utils import compute_fft


def test_fft_identifies_frequencies():
    fs = 1000
    duration = 2
    components = [(50, 1.0), (120, 0.5)]
    _, signal = sum_sine_waves(components, fs, duration)
    freqs, mag = compute_fft(signal, fs)
    top_indices = np.argsort(mag)[-2:]
    detected_freqs = sorted(freqs[top_indices])
    assert np.isclose(detected_freqs[0], 50, atol=1)
    assert np.isclose(detected_freqs[1], 120, atol=1)
