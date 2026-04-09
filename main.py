import whisper
import sounddevice as sd
from scipy.io.wavfile import write

# ---- Settings ----
SAMPLE_RATE = 16000
DURATION = 5  # seconds

# ---- Record audio ----
print("Recording... Speak now")

audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)
sd.wait()

write("input.wav", SAMPLE_RATE, audio)

print("Recording complete.")

# ---- Load Whisper model ----
model = whisper.load_model("base")

# ---- Transcribe ----
result = model.transcribe("input.wav")

print("\n=== TRANSCRIPTION ===")
print(result["text"])