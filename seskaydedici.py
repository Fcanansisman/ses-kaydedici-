import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

# Ses kaydı ayarları
samplerate = 44100  # Hz
duration = 10  # saniye

print("Kayıt başlıyor. Konuşmaya başlayın...")

# Ses kaydı
recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2, dtype='int16')
sd.wait()  # Kaydın tamamlanmasını bekleyin

print("Kayıt tamamlandı. Dosya kaydediliyor...")

# WAV dosyası olarak kaydetme
write('recording.wav', samplerate, recording)

print("Ses kaydı 'recording.wav' olarak kaydedildi.")