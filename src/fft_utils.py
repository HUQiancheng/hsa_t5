import numpy as np
from numpy.typing import ArrayLike


def compute_fft(signal: ArrayLike, fs: int, full_range: bool = False) -> tuple[np.ndarray, np.ndarray]:
    """Return frequency bins and magnitude of ``signal``. ``full_range`` gives ``0..fs``."""
    signal = np.asarray(signal)
    n = len(signal)
    spectrum = np.fft.fft(signal)
    magnitude = np.abs(spectrum) / (n / 2)
    freqs = np.fft.fftfreq(n, d=1 / fs)
    freqs = np.where(freqs < 0, freqs + fs, freqs)
    order = np.argsort(freqs)
    freqs = freqs[order]
    magnitude = magnitude[order]
    if not full_range:
        mask = freqs <= fs / 2
        freqs = freqs[mask]
        magnitude = magnitude[mask]
    return freqs, magnitude
