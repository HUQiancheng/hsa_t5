import numpy as np
from numpy.typing import ArrayLike


def compute_fft(signal: ArrayLike, fs: int) -> tuple[np.ndarray, np.ndarray]:
    """Compute the one-sided FFT magnitude of a real signal.

    Parameters
    ----------
    signal : array_like
        Input time-domain signal.
    fs : int
        Sampling frequency in Hz.

    Returns
    -------
    freqs : np.ndarray
        Frequency bins (positive frequencies).
    magnitude : np.ndarray
        Normalized magnitude of the FFT.
    """
    signal = np.asarray(signal)
    n = len(signal)
    spectrum = np.fft.rfft(signal)
    magnitude = np.abs(spectrum) / (n / 2)
    freqs = np.fft.rfftfreq(n, d=1 / fs)
    return freqs, magnitude
