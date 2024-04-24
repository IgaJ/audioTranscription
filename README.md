# Description
This project allows for recording audio from a microphone and transcribing it into text using the OpenAI Whisper model.<br> 
Recordings are saved in WAV format and converted to text.

# Requirements
<li>Python (3.7 or newer)
<li> PyAudio
<li>Whisper 
<li>FFmpeg
<li>optional PyDub if want to convert WAV file to MP3

# Installation:
Install required dependency: `pip install pyaudio whisper`<br>
To use FFmpeg download it from the official web page and add the path to the ffmpeg's binary file to the PATH environment variable: `os.environ["PATH"] += os.pathsep + "C:/path/to/ffmpeg/bin"`<br>
To start recording, run the script in terminal: `python audio_file.py`<br>

You can customize the recording settings by modifying the parameters in the script (f.e. RECORD_SECONDS)
