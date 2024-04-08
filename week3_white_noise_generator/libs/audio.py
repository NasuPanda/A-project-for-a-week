import time

import numpy as np
import scipy.io.wavfile
import simpleaudio as sa
import sounddevice as sd
import soundfile as sf
from common import constants


def __adjust_white_noise_to_int16(white_noise: np.ndarray, sample_rate: int, volume: float=0.5):
    # Ensure volume is between 0 and 1
    volume = np.clip(volume, 0.0, 1.0)

    # Adjust amplitude based on volume
    adjusted_noise = white_noise * volume

    # simpleaudio works best with integer audio data (typically 16-bit signed integers).
    white_noise_int16 = (adjusted_noise * 32767).astype(np.int16)

    return white_noise_int16

def play_white_noise(white_noise: np.ndarray, sample_rate: int, volume: float=0.5):
    """Send generated white noise to speakers"""
    white_noise_int16 = __adjust_white_noise_to_int16(white_noise, sample_rate, volume)

    # This holds information about the audio data, number of channels (1 for mono), sample width (in bytes - likely 2 for 16-bit), and sample rate.
    play_obj = sa.play_buffer(white_noise_int16, 1, 2, sample_rate)
    play_obj.wait_done()

def save_white_noise_as_wav(white_noise: np.ndarray, sample_rate: int, duration: int, volume: float=0.5):
    """Save white noise as wav"""
    white_noise_int16 = __adjust_white_noise_to_int16(white_noise, sample_rate, volume)
    filename = f"{constants.AUDIO_OUTPUT_DIR}/whitenoise_{duration}s.wav"
    scipy.io.wavfile.write(filename, sample_rate, white_noise_int16)

def play_audio_loop(audio_file: str, number_of_loops: int):
    """Play audio file for N times"""
    data, sample_rate = sf.read(audio_file)

    # Loop N times
    for __ in range(number_of_loops):
        sd.play(data, sample_rate, blocking=True)

def play_audio_for_minutes(audio_file: str, duration_minutes: int):
    """Play audio file for minutes"""
    data, sample_rate = sf.read(audio_file)

    duration_seconds = duration_minutes * 60

    start_time = time.time()
    while time.time() - start_time < duration_seconds:
        sd.play(data, sample_rate, blocking=True)

