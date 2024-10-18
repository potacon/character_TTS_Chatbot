from style_bert_vits2.nlp import bert_models
from style_bert_vits2.constants import Languages
from huggingface_hub import hf_hub_download
from style_bert_vits2.tts_model import TTSModel
import numpy as np
import sounddevice as sd
from safetensors.torch import load_file
import torch
from TTS.api import TTS
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from pathlib import Path


bert_model = bert_models.load_model(Languages.JP, "ku-nlp/deberta-v2-large-japanese-char-wwm")
tokenizer = bert_models.load_tokenizer(Languages.JP, "ku-nlp/deberta-v2-large-japanese-char-wwm")

def load_tts_model(model_file, config_file, style_file, device='cpu'):
    assets_root = Path("model_assets")
    model = TTSModel(
        model_path=assets_root / model_file,
        config_path=assets_root / config_file,
        style_vec_path=assets_root / style_file,
        device=device
    )
    return model

def generate_speech(text, model):
    sr, audio = model.infer(text=text)  # Removed bert_model and tokenizer
    return sr, audio

def switch_voice(voice_name):
    if voice_name == "kaguy":
        model_file = "kaguy-styles/kaguy-styles_e84_s17000.safetensors"
        config_file = "kaguy-styles/config.json"
        style_file = "kaguy-styles/style_vectors.npy"
    elif voice_name == "another_voice":
        model_file = "another-voice.safetensors"
        config_file = "config.json"
        style_file = "style_vectors.npy"
    else:
        raise ValueError(f"Unknown voice: {voice_name}")
    
    # Load the selected voice model
    model = load_tts_model(model_file, config_file, style_file, device='cuda')
    return model


#"C:/Users/Admin/Desktop/Bert-vits/sbv2/Style-Bert-VITS2/model_assets/kaguy-styles/kaguy-styles_e84_s17000.safetensors"


'''def text_to_speech(text, output_path, speaker_wav=None):
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

    # Generate speech and save to file
    tts.tts_to_file(
        text=text,
        file_path=output_path,
        speaker_wav=speaker_wav,  # You can specify a target voice here
        language='ja'  # Set to Korean language
    )'''