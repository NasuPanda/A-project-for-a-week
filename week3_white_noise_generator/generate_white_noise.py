def main():
    import argparse

    from libs import audio, white_noise_generator

    parser = argparse.ArgumentParser(description="White Noise Generator")
    parser.add_argument('-d', '--duration', type=int, default=3, help='Noise duration in seconds')
    parser.add_argument('-sr', '--sample_rate', type=int, default=44100, help='Sample rate')
    parser.add_argument('-v', '--volume', type=float, default=0.5, help='Volume level (0 to 1)')
    parser.add_argument("-sc", "--scale", type=float, default=0.5, help="Equal to standard deviation")
    args = parser.parse_args()

    duration = args.duration  # Generate N seconds of noise
    sample_rate = args.sample_rate  # A common audio sample rate
    volume = args.volume
    scale = args.scale # The spread or width of the bell curve

    white_noise = white_noise_generator.generate_white_noise(
        duration_seconds=duration,
        sample_rate=sample_rate,
        scale=scale
    )
    # audio_controller.play_white_noise(
    #     white_noise=white_noise,
    #     sample_rate=sample_rate,
    #     volume=volume
    # )
    audio.save_white_noise_as_wav(
        white_noise=white_noise,
        sample_rate=sample_rate,
        duration=duration,
        volume=volume
    )

    # Test: Visualize on plot
    # import matplotlib.pyplot as plt
    # plt.plot(white_noise[:1000])
    # plt.xlabel("Index")
    # plt.ylabel("Value")
    # plt.title("White Noise")
    # plt.show()

if __name__ == "__main__":
    main()
