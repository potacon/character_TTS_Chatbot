from Capture_Audio_input import capture_audio
from send_text_FTllama import query_llama3
from Whisper_model import transcribe_audio
import os
from style_bert_vits2_model import switch_voice, generate_speech, bert_model, tokenizer
from pydub import AudioSegment
import sounddevice as sd
import glob
import numpy as np
import time


def play_audio(sr, audio, device_indices):
    # Ensure audio data is in stereo format (2 channels)
    if audio.ndim == 1:
        audio = np.stack([audio, audio], axis=-1)  # Convert mono to stereo if needed

    # Loop over each device index and play the audio
    for device_index in device_indices:
        sd.play(audio, samplerate=sr, device=device_index)
        sd.wait()  # Wait until audio is done playing on each device

def main():
    chosen_voice = "kaguy"  # Replace this with logic to choose different voices
    tts_model = switch_voice(chosen_voice)

    while True:
        audio = capture_audio()
        if audio is None:
            print("Failed to capture audio, trying again.")
            continue

        text = transcribe_audio(audio)
        if text is None:
            print("No text transcribed, trying again.")
            continue

        print(f"Transcribed Text: {text}")

        if "おしまい" in text.lower():
            print("Conversation ended.")
            break

        response = query_llama3(text)
        print(f"LLaMA 3.1 Response: {response}")

        sr, audio = generate_speech(response, tts_model)

        # Set the device indices to include VB-Cable and headset
        play_audio(sr, audio, device_indices=[4,6])  # Replace 6 and 4 with your VB-Cable and headset indices 6이 헤드셋


if __name__ == "__main__":
    main()



# 한국어 코드 #
"""def main():
    while True:
        audio = capture_audio()  # Capture audio

        if audio is None:
            print("Failed to capture audio, trying again.")
            continue
        
        text = transcribe_audio(audio)  # Convert speech to text
        
        if text is None:
            print("No text transcribed, trying again.")
            continue

        print(f"Transcribed Text: {text}")

        # Exit loop if user says "let's stop"
        if "그만하자" in text.lower():
            print("Conversation ended.")
            break
        
        # Get response from LLaMA 3.1
        response = query_llama3(text)
        print(f"LLaMA 3.1 Response: {response}")

if __name__ == "__main__":
    main()"""
