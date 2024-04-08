# White Noise Generator
## Usage
Just run the shellscript, and it should work.

```sh
./run_white_noise_player.sh
```

NOTE:
- You can utilize Raycast script for further improvement.
- Some audio files exceeds the file size limit of git repository by some amount, so I put down them on .gitignore.

## About
Project Summary: White Noise Generator for Studying (Python)
Goal:
Create a Python program to generate white noise to improve focus while studying in noisy environments.

### Benefits
Blocks out distractions (traffic, conversations, etc.)
Improves concentration
Avoids distractions of Youtube (Now, I'm using YouTube for white noise)

### Technical Approach (with Math Concepts)

#### Representing White Noise

Understanding: White noise has equal energy distribution across all frequencies.
Math: We'll use random number generation, particularly from a Gaussian (normal) distribution, to approximate this spectral property.
Python: numpy.random.normal for generating random numbers.

#### Sound Wave Generation

Basics: A sound wave is represented by pressure fluctuations over time.
Math: We'll model this as a sine wave (or a combination of them) where the amplitude corresponds to volume, and frequency relates to the pitch.
Python: scipy.signal has useful functions for signal generation.

#### Audio Output

Python Libraries: We can use libraries like sounddevice, simpleaudio, or PyAudio to output the generated signal through speakers.

#### Additional
Potentially allow adjusting the following: Sample rate (speed of the sound), Duration of the noise, Volume control
