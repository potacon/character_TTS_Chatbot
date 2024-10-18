import pyaudio
import wave
import whisper

model = whisper.load_model("medium")

# 내가 마이크로 말한 말을 텍스트로 변환시켜주는 코드 및 기능.
# 이 기능은 직접 만든 챗봇과 대화할 예정이 아니면 사용하지않아도 가능.

def transcribe_directly():
    sample_rate = 16000
    bits_per_sample = 16
    chunk_size = 1024
    audio_format = pyaudio.paInt16
    channels = 1

    def callback(in_data, frame_count, time_info, status):
        wav_file.writeframes(in_data)
        return None, pyaudio.paContinue

    # Open the wave file for writing
    wav_file = wave.open('./output.wav', 'wb')
    wav_file.setnchannels(channels)
    wav_file.setsampwidth(bits_per_sample // 8)
    wav_file.setframerate(sample_rate)

    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Start recording audio
    stream = audio.open(format=audio_format,
                        channels=channels,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=chunk_size,
                        stream_callback=callback)

    input("Press Enter to stop recording...")
    # Stop and close the audio stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Close the wave file
    wav_file.close()
    result = model.transcribe("./output.wav", language="ja")
    return result['text']

text = transcribe_directly()
print(text)
#한국어를 인식하려면 result = model.transcribe("./output.wav", language="ko")를,
#영어를 인식하려면 result = model.transcribe("./output.wav", language="en") 을 써주세요.