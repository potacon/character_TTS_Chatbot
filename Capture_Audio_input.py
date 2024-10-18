import speech_recognition as sr
import numpy as np
import pyaudio

def capture_audio():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Speak Anything :')
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='ko-KR')
        print('You said: {}'.format(text))
        audio_data = np.frombuffer(audio.get_raw_data(), dtype=np.int16)  # Raw audio data
        return audio_data  # Return only audio data, not a tuple
    except Exception as e:
        print(f'Sorry, could not recognize your voice. Error: {str(e)}')
        return None  # Return None in case of failure
    
#def capture_audio():
    #r = sr.Recognizer()
    
    #with sr.Microphone() as source:
        #print('Speack Anything :')
        #audio = r.listen(source)
    
    #try:
        #text = r.recognize_google(audio, language='ko-KR')
        #print('You said : {}'.format(text))
        #audio_data = np.frombuffer(audio.get_raw_data(), dtype=np.int16)
        #return audio_data
    #except:
        #print('Sirry could not recignize your voice')
        
