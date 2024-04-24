import pyaudio
import wave
from pydub import AudioSegment
import os
import whisper
os.environ["PATH"] += os.pathsep + "C:/ffmpeg/bin"

# ustawienia nagrywania
FORMAT = pyaudio.paInt16    # format próbkowania
CHANNELS = 1                # liczba kanałów audio
RATE = 44100                # częstotliwość próbkowania np. 44100 Hz
CHUNK = 1024                # liczba próbek na ramkę
RECORD_SECONDS = 10         # czas nagrywania w sekundach

# inicjalizacja obiektu PyAudio
audio = pyaudio.PyAudio()

# otwarcie strumienia wejściowego (mikrofon)
stream = audio.open(format = FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
print("Nagrywanie")

frames = []

# nagrywanie dżwięku
for i in range(int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Nagrywanie zakończone")

# zatrzymanie strumienia
stream.stop_stream()
stream.close()
audio.terminate()

# zapis do pliku WAV
file_wav = "nagranie3.wav"
with wave.open(file_wav, "wb") as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))

# konwersja pliku WAV na mp3
# audio_segment = AudioSegment.from_wav(file_wav)
# file_mp3 = "nagrania.mp3"
# audio_segment.export(file_mp3, format="mp3")

model = whisper.load_model("base")
audio_path = file_wav # "C:/Users/Kompiuta/PycharmProjects/transcribe_audio_files/nagranie2.wav"
result = model.transcribe(audio_path)
print(result["text"])
