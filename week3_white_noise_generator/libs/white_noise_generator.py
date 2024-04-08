import numpy as np

def generate_white_noise(duration_seconds: float, sample_rate: int = 44100, scale: float=0.5) -> np.ndarray:
    """
    Generates a white noise audio signal.

    Args:
        duration_seconds (float): The desired duration of the noise in seconds.
        sample_rate (int): The sample rate (in Hz) at which to generate the signal.
        scale (float): This controls the spread or width of the bell curve.

    Returns:
        numpy.ndarray: An array containing the white noise signal samples.
    """

    num_samples = int(duration_seconds * sample_rate)

    # np.random.normal generates Gaussian white noise approximation
    noise_signal = np.random.normal(scale=scale, size=num_samples)

    return noise_signal
