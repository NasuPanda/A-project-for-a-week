import argparse

from common import constants
from libs import audio

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Audio File Player with Loop')
    parser.add_argument('-l', '--loop', type=int, default=1, help='How many loop (1loop = 30min)')
    args = parser.parse_args()

    print(args)

    # constants.AUDIO_FILE_60s
    # constants.AUDIO_FILE_25m
    # constants.AUDIO_FILE_30m
    audio.play_audio_loop(audio_file=constants.AUDIO_FILE_30m, number_of_loops=args.loop)
