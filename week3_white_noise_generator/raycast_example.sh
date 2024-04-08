#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Play White Noise
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🔇
# @raycast.argument1 { "type": "text", "placeholder": "Number of loops" }

# Documentation:
# @raycast.description Play white noise
cd ~/projects/2024/A-project-for-a-week/week3_white_noise_generator
# A raycast script is executed in a non-login shell. Therefore the pipenv comman from my $PATH isn't loaded.
# You can either append -l to your shebang or just use your binary directly.
/Users/ns/.asdf/shims/pipenv run python play_white_noise.py -l "$1"
