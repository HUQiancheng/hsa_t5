import numpy as np


def sine_wave(freq: float, amplitude: float, fs: int, duration: float) -> np.ndarray:
    """Generate a single sine wave signal."""
    t = np.arange(0, duration, 1 / fs)
    signal = amplitude * np.sin(2 * np.pi * freq * t)
    return t, signal


def sum_sine_waves(components, fs: int, duration: float) -> tuple[np.ndarray, np.ndarray]:
    """Generate a sum of sine waves.

    Parameters
    ----------
    components: Iterable[tuple[float, float]]
        Sequence of (frequency, amplitude) pairs.
    fs: int
        Sampling frequency.
    duration: float
        Signal duration in seconds.

    Returns
    -------
    t: np.ndarray
        Time vector.
    signal: np.ndarray
        Generated signal.
    """
    t = np.arange(0, duration, 1 / fs)
    signal = np.zeros_like(t)
    for freq, amp in components:
        signal += amp * np.sin(2 * np.pi * freq * t)
    return t, signal


def add_noise(signal: np.ndarray, noise_level: float) -> np.ndarray:
    """Add Gaussian noise to a signal."""
    noise = noise_level * np.random.randn(*signal.shape)
    return signal + noise
