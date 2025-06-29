import numpy as np


def sine_wave(freq: float, amplitude: float, fs: int, duration: float) -> np.ndarray:
    """Generate a single sine wave signal."""
    t = np.arange(0, duration, 1 / fs)
    signal = amplitude * np.sin(2 * np.pi * freq * t)
    return t, signal


def sum_sine_waves(components, fs: int, duration: float) -> tuple[np.ndarray, np.ndarray]:
    """Return the sum of sine waves defined by ``(freq, amp)`` pairs."""
    t = np.arange(0, duration, 1 / fs)
    components = np.asarray(components, dtype=float)
    if components.size == 0:
        return t, np.zeros_like(t)
    freqs = components[:, 0][:, None]
    amps = components[:, 1][:, None]
    phases = 2 * np.pi * freqs * t
    signal = np.sum(amps * np.sin(phases), axis=0)
    return t, signal


def add_noise(signal: np.ndarray, noise_level: float) -> np.ndarray:
    """Add Gaussian noise to a signal."""
    noise = noise_level * np.random.randn(*signal.shape)
    return signal + noise
