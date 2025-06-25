import numpy as np
from numpy.typing import ArrayLike


def cross_correlation(sig1: ArrayLike, sig2: ArrayLike) -> tuple[np.ndarray, np.ndarray]:
    """Compute the cross-correlation between two signals.

    The result is normalized so that the autocorrelation of each signal at lag 0 is 1.
    Returns lags in number of samples.
    """
    sig1 = np.asarray(sig1)
    sig2 = np.asarray(sig2)
    corr = np.correlate(sig1, sig2, mode="full")
    norm = np.sqrt(np.sum(sig1 ** 2) * np.sum(sig2 ** 2))
    if norm == 0:
        norm = 1
    corr /= norm
    lags = np.arange(-len(sig1) + 1, len(sig2))
    return lags, corr
