import numpy as np
from src.signal_generation import sum_sine_waves
from src.filter_design import (
    butter_lowpass,
    butter_highpass,
    apply_filter,
    rc_lowpass,
    rc_highpass,
    rc_bandpass,
)
from src.fft_utils import compute_fft


def test_lowpass_removes_high_frequency():
    fs = 10000
    duration = 0.1
    components = [(50, 1.0), (500, 1.0)]
    _, signal = sum_sine_waves(components, fs, duration)
    b, a = butter_lowpass(100, fs, order=1)
    filtered = apply_filter(signal, b, a)
    freqs, mag = compute_fft(filtered, fs)
    amp_50 = mag[np.argmin(np.abs(freqs - 50))]
    amp_500 = mag[np.argmin(np.abs(freqs - 500))]
    assert amp_50 > amp_500


def test_highpass_removes_low_frequency():
    fs = 10000
    duration = 0.1
    components = [(50, 1.0), (500, 1.0)]
    _, signal = sum_sine_waves(components, fs, duration)
    b, a = butter_highpass(200, fs, order=1)
    filtered = apply_filter(signal, b, a)
    freqs, mag = compute_fft(filtered, fs)
    amp_50 = mag[np.argmin(np.abs(freqs - 50))]
    amp_500 = mag[np.argmin(np.abs(freqs - 500))]
    assert amp_500 > amp_50


def test_rc_filter_design():
    r, c = rc_lowpass(50, r=1e3)
    assert np.isclose(1 / (2 * np.pi * r * c), 50, atol=1)
    r2, c2 = rc_highpass(500, c=1e-6)
    assert np.isclose(1 / (2 * np.pi * r2 * c2), 500, atol=1)
    rbp, cbp = rc_bandpass(400, 600, r=1e3)
    fc_low = 1 / (2 * np.pi * rbp * cbp)
    assert 400 <= fc_low <= 600