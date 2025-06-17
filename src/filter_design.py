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
    """Apply a digital filter defined by coefficients ``b`` and ``a``."""
    return lfilter(b, a, data)


def rc_lowpass(cutoff: float, r: float | None = None, c: float | None = None) -> tuple[float, float]:
    """Design a simple RC low-pass filter.

    Parameters
    ----------
    cutoff:
        Desired cut-off frequency in Hz.
    r, c:
        Optional resistor (Ohms) or capacitor (Farads). If one value is ``None``,
        it will be computed from the other to satisfy ``fc = 1/(2*pi*R*C)``.

    Returns
    -------
    tuple of (R, C) values meeting the cut-off specification.
    """
    if r is None and c is None:
        r = 1e3  # 1 kOhm default
    if r is None:
        r = 1 / (2 * np.pi * cutoff * c)
    if c is None:
        c = 1 / (2 * np.pi * cutoff * r)
    return float(r), float(c)


def rc_highpass(cutoff: float, r: float | None = None, c: float | None = None) -> tuple[float, float]:
    """Design a simple RC high-pass filter using the same approach as :func:`rc_lowpass`."""
    return rc_lowpass(cutoff, r, c)

def rc_bandpass(lowcut: float, highcut: float, r: float | None = None, c: float | None = None) -> tuple[float, float]:
    """Design a simple RC band-pass filter by cascading a high-pass and a low-pass.

    The same R and C are returned for both stages for simplicity. The resulting
    center frequency is roughly the geometric mean of ``lowcut`` and ``highcut``.
    """
    if r is None and c is None:
        r = 1e3
    if r is None:
        r = 1 / (2 * np.pi * lowcut * c)
    if c is None:
        c = 1 / (2 * np.pi * highcut * r)
    return float(r), float(c)

