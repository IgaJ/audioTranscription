 This project allows for recording audio from a microphone and transcribing it into text using the OpenAI Whisper model.<br> 
 Recordings are saved in WAV format and converted to text.

 Requirements:
 Python, PyAudio, Whisper, FFmpeg, optional PyDub if want to convert WAV file to MP3

 Installation:
 install required dependency: pip install pyaudio whisper
 to use FFmpeg download it from the official web page and add the path to the ffmpeg's binary file to the PATH environment variable: os.environ["PATH"] += os.pathsep + "C:/path/to/ffmpeg/bin"
 to start recording, run the script in terminal: python audio_file.py

 You can customize the recording settings by modifying the parameters in the script (f.e. RECORD_SECONDS)
