import numpy as np
from numpy.typing import ArrayLike


def compute_fft(signal: ArrayLike, fs: int, full_range: bool = False) -> tuple[
    np.ndarray, np.ndarray
]:
    """Compute the FFT magnitude of a real signal.

    Parameters
    ----------
    signal : array_like
        Input time-domain signal.
    fs : int
        Sampling frequency in Hz.
    full_range : bool, optional
        If ``True`` the returned frequency axis covers ``0..fs`` so it is
        symmetric around ``fs/2``. Otherwise only ``0..fs/2`` is returned.

    Returns
    -------
    freqs : np.ndarray
        Frequency bins (positive frequencies).
    magnitude : np.ndarray
        Normalized magnitude of the FFT.
    """
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
