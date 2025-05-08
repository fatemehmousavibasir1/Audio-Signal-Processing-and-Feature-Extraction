# Audio Signal Processing and Feature Extraction

## Overview

This Python script processes an audio file (`.wav` format) to analyze its waveform, compute energy, zero-crossing rate, and derive the product of these two features. The script also classifies frames into voiced, unvoiced, and silence categories based on specific energy thresholds, and visualizes the results in various plots.

The script employs the following libraries:

- **Librosa**: For audio processing, including loading the audio file and extracting features like energy and zero-crossing rate.
- **Matplotlib**: For plotting the audio waveform and feature visualizations.
- **Scipy**: For reading `.wav` files and manipulating the audio data.
- **Playsound**: For playing the audio file.

