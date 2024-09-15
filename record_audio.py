import pyaudio
import wave
import keyboard

def record_audio():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
    print("Press 'r' to start/stop recording, 'q' to quit.")
    recording = False
    frames = []
    while True:
        if keyboard.is_pressed('r'):
            if not recording:
                print("Recording...")
                recording = True
            else:
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

if __name__ == "__main__":
    record_audio()
