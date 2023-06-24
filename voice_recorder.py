import wave
import pyaudio

with wave.open("recording.wav", "wb") as sound_file:
    audio = pyaudio.PyAudio()
    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)

    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
    frames = []
    print('Recording...')

    try:
        while True:
            data = stream.read(1024)
            frames.append(data)
    except KeyboardInterrupt:
        pass

    sound_file.writeframes(b''.join(frames))

    print('Done')

    stream.stop_stream()
    stream.close()
    audio.terminate()
