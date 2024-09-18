import warnings
import whisper
import sounddevice as sd
from scipy.io.wavfile import write


def record(duration=5, sr=16000, filename='input.wav'):
    print("Recording...")
    recorded_audio = sd.rec(int(duration * sr), samplerate=sr, channels=1, dtype='float32')
    sd.wait()
    print("Recording finished")
    write(filename, sr, recorded_audio)


input_file = "input.wav"
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")
record(filename=input_file)
model = whisper.load_model("base", device='cpu')
result = model.transcribe(input_file)
print(result["text"])
