import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.io import wavfile

from playsound import playsound
playsound("C:/Users/Asus/Desktop/class.wav")
print('playing sound')


def plot_audio_waveform(audio_file):

    if not os.path.exists("C:/Users/Asus/Desktop/class.wav"):
        print("not exist")
        return
    
    sr, signal = wavfile.read("C:/Users/Asus/Desktop/class.wav")
    
    plt.figure(figsize=(50, 50))
    plt.plot(signal)
    plt.title('Waveform')
    plt.xlabel('Sample')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    audio_file = "C:/Users/Asus/Desktop/class.wav"
    plot_audio_waveform(audio_file)




audio_file ="C:/Users/Asus/Desktop/class.wav"
signal, sr = librosa.load(audio_file, sr=None)

energy = librosa.feature.rms(signal, frame_length=2048, hop_length=512)
print("energy:", energy)

zero_crossing_rate = librosa.feature.zero_crossing_rate(signal, frame_length=2048, hop_length=512)
print(" zero_crossing_rate :", zero_crossing_rate)

product = energy * zero_crossing_rate
print("energy * zero_crossing_rate:  ", product)


energy_flattened = energy.flatten()
plt.figure(figsize=(10, 4))
plt.plot(energy_flattened)
plt.xlabel('time')
plt.ylabel('value')
plt.title('energy')
plt.show()


zero_crossing_rate_flattened = zero_crossing_rate.flatten()
plt.figure(figsize=(10, 4))
plt.plot(zero_crossing_rate_flattened)
plt.xlabel('time')
plt.ylabel('value')
plt.title('zero_crossing_rate')
plt.show()

plt.figure(figsize=(10, 6))
plt.imshow(product, origin='lower', aspect='auto', cmap='viridis')
plt.xlabel('frame')
plt.ylabel('Attribute')
plt.title('energy*zero')
plt.colorbar(label='value')
plt.show()

product_flattened = product.flatten()
plt.figure(figsize=(10, 4))
plt.plot(product_flattened)
plt.xlabel('time')
plt.ylabel('value')
plt.title('energy*zero')
plt.show()


threshold_energy_voiced = 0.017  # آستانه  مصوت
threshold_energy_silence = 0.001  # آستانه سکوت
for i in range(len(product[0])):
    if product[0][i] > 0.017:
        print(f"V  i: {i}   product:  {product[0][i]}")
    elif product[0][i] > 0.001:
        print(f"U  i: {i}   product:  {product[0][i]}")
    else:
        print(f"S  i: {i}   product:  {product[0][i]}" )
plt.figure(figsize=(14, 5))
librosa.display.waveshow(product, sr=sr, alpha=0.5)


def find_intervals(product, sr):
    intervals = []
    current_interval = []
    for i in range(product.shape[1]):
        frame_value = product[0, i]
        
        if frame_value <= 0.001:
            label = 'S'
        if 0.001<frame_value <= 0.017:
            label = 'U'
        if 0.017<frame_value :
            label = 'V'

        plt.text(i / sr, max(product.flatten()), label, color='black', fontsize=12, ha='center', va='bottom')      
        if frame_value <= 0.001:
            if current_interval:
                intervals.append((current_interval[0], i))
                current_interval = []
        else:
            if not current_interval:
                current_interval.append(i)
    return intervals

intervals = find_intervals(product, sr)
for interval in intervals:
    plt.axvspan(interval[0] / sr, interval[1] / sr, alpha=0.3)

plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Waveform with Voiced, Unvoiced, and Silence Labels')
plt.tight_layout()  
plt.show()
