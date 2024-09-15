import pyaudio
import wave
import keyboard
import replicate

def record_audio():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
    print("Press 'r' to start recording, 's' to stop recording, 'q' to quit.")
    recording = False
    frames = []
    while True:
        if keyboard.is_pressed('r') and not recording:
            print("Recording...")
            recording = True
        elif keyboard.is_pressed('s') and recording:
            print("Stopping recording...")
            recording = False
        elif keyboard.is_pressed('q'):
            print("Quitting...")
            break
        if recording:
            data = stream.read(1024)
            frames.append(data)
    stream.stop_stream()
    stream.close()
    audio.terminate()
    wf = wave.open("output.wav", 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    wf.setframerate(44100)
    wf.writeframes(b''.join(frames))
    wf.close()
    recognize_speech()

def recognize_speech():
    input = {
        "audio": "output.wav"
    }
    output = replicate.run(
        "openai/whisper:cdd97b257f93cb89dede1c7584e3f3dfc969571b357dbcee08e793740bedd854",
        input=input
    )
    print(output)

if __name__ == "__main__":
    record_audio()
