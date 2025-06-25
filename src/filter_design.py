import numpy as np
from scipy.signal import butter, lfilter
from numpy.typing import ArrayLike


def butter_lowpass(cutoff: float, fs: int, order: int = 1):
    nyq = fs / 2
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype="low", analog=False)
    return b, a


def butter_highpass(cutoff: float, fs: int, order: int = 1):
    nyq = fs / 2
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype="high", analog=False)
    return b, a


def butter_bandpass(lowcut: float, highcut: float, fs: int, order: int = 1):
    nyq = fs / 2
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype="band", analog=False)
    return b, a


def apply_filter(data: ArrayLike, b, a) -> np.ndarray:
    """Apply a digital filter defined by ``b`` and ``a``."""
    return lfilter(b, a, data)


def rc_lowpass(cutoff: float, r: float | None = None, c: float | None = None) -> tuple[float, float]:
    """RC low-pass helper. Provide ``r`` or ``c`` and get the other."""
    if r is None and c is None:
        r = 1e3  # 1 kOhm default
    if r is None:
        r = 1 / (2 * np.pi * cutoff * c)
    if c is None:
        c = 1 / (2 * np.pi * cutoff * r)
    return float(r), float(c)


def rc_highpass(cutoff: float, r: float | None = None, c: float | None = None) -> tuple[float, float]:
    """RC high-pass helper using the same formula."""
    return rc_lowpass(cutoff, r, c)

def rc_bandpass(lowcut: float, highcut: float, r: float | None = None, c: float | None = None) -> tuple[float, float]:
    """RC band-pass helper returning common R and C for both stages."""
    if r is None and c is None:
        r = 1e3
    if r is None:
        r = 1 / (2 * np.pi * lowcut * c)
    if c is None:
        c = 1 / (2 * np.pi * highcut * r)
    return float(r), float(c)
