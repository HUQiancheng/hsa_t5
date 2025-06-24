import numpy as np
from src.signal_generation import sine_wave
from src.correlation_utils import cross_correlation


def test_cross_correlation_detects_delay():
    fs = 1000
    duration = 1
    _, sig = sine_wave(10, 1.0, fs, duration)
    delay = 50  # samples
    sig_delayed = np.roll(sig, delay)
    lags, corr = cross_correlation(sig, sig_delayed)
    lag_at_max = lags[np.argmax(corr)]
    assert lag_at_max == delay


def test_cross_correlation_with_noise():
    fs = 1000
    duration = 1
    _, sig = sine_wave(20, 1.0, fs, duration)
    noise = np.random.randn(len(sig)) * 0.5
    sig_noisy = sig + noise
    delay = 30
    sig2 = np.roll(sig_noisy, delay)
    lags, corr = cross_correlation(sig_noisy, sig2)
    lag_at_max = lags[np.argmax(corr)]
    assert abs(abs(lag_at_max) - delay) <= 1
