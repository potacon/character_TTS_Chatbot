import whisper
import numpy as np
import librosa

def transcribe_audio(audio_data, original_sample_rate=44100):
    model = whisper.load_model("base")  # Load Whisper model

    # Convert audio data to float32 format and normalize it (from int16)
    audio_data = audio_data.astype(np.float32) / 32768.0  

    # Resample the audio to 16kHz (Whisper's required format)
    target_sample_rate = 16000
    audio_data_resampled = librosa.resample(audio_data, orig_sr=original_sample_rate, target_sr=target_sample_rate)

    # Transcribe using Whisper
    result = model.transcribe(audio_data_resampled, language='ja')
    
    return result['text']


#def transcribe_audio(audio_data):
    #model = whisper.load_model("base")  # Load Whisper model without 'weights_only'

    # Convert the NumPy audio data to float32 and normalize 16-bit PCM to float
    #audio_data = audio_data.astype(np.float32) / 32768.0  

    # Whisper expects 16kHz audio. You might need to resample the audio if it's not 16kHz.

    #result = model.transcribe(audio_data, language='ko')
    #print(audio_data)
    #return result['text']