import pytest
import numpy as np

from libs.white_noise_generator import generate_white_noise

def test_generate_white_noise():
    sample_rate = 44100
    duration = 1
    noise_signal = generate_white_noise(duration, sample_rate)

    # Check if the array has the correct length
    assert noise_signal.shape == (sample_rate,)
    # Check if the mean is close to zero (characteristic of white noise)
    assert np.abs(noise_signal.mean()).round(2) == 0.0
    # Check if values are within a reasonable range (adjust if needed)
    assert -2.5 <  np.min(noise_signal) < 2.5
