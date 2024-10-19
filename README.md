# anime_chat_bot-kaguya

A custom chatbot integrated with text-to-speech (TTS) functionality, utilizing fine-tuned voice models for personalized responses. This project supports both voice input and output, allowing users to engage in dynamic conversations with a character-powered by advanced AI models.

Table of Contents
Features
Installation
Usage
TTS Models
Voice Customization
Downloading the kaguy-styles_e84_s17000.safetensors File
Downloading the LLaMA 3.1 Model
License
Features
Speech-to-Text: Captures and transcribes audio input using Whisper model.
Natural Language Processing: Generates chatbot responses using the fine-tuned LLaMA 3.1 model.
Text-to-Speech: Converts chatbot responses to speech using models like Style-BERT-VITS2.
Custom Voices: Supports custom voice models for personalized interactions.
Installation
Prerequisites
Python 3.8+
Git
Git LFS
CUDA 12.1 (if using GPU acceleration)
cuDNN 9.4.0.58
Clone the Repository
To get started, clone the repository and install dependencies:

bash
코드 복사
git clone https://github.com/potacon/character_TTS_Chatbot.git
cd character_TTS_Chatbot
Install Dependencies
Create and activate a Python virtual environment (optional but recommended):

bash
코드 복사
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required dependencies:

bash
코드 복사
pip install -r requirements.txt
Install Git LFS
Make sure Git LFS is installed and initialized:

bash
코드 복사
git lfs install
Usage
To run the chatbot with voice input/output:

Capture audio input, transcribe it with Whisper, and generate a response:

bash
코드 복사
python Main.py
The chatbot will listen to your voice, transcribe it, generate a response using LLaMA 3.1, and then convert the text back to speech using the selected TTS model.

Configuration
Make sure to customize the paths in the configuration files for the models you want to use:

LLaMA Model Path: Update the LLaMA model path to point to your fine-tuned model.
TTS Voice Models: Configure the TTS model paths, including custom voices such as kaguy-styles_e84_s17000.safetensors.
TTS Models
This project currently supports the following TTS models:

Style-BERT-VITS2: For natural-sounding, customizable voices.
Whisper: For accurate transcription from speech to text.
Additional models can be configured in the project. You can fine-tune your own voices or use pre-trained ones.

Voice Customization
To use custom voices, such as kaguy-styles_e84_s17000.safetensors, follow these steps:

Download the custom voice model from the link provided below.
Place the downloaded model file in the model_assets/kaguy-styles directory.
Modify the TTS configuration to point to the custom voice model.
If you want to switch voices dynamically, update the style_bert_vits2_model.py and Main.py to support multiple voice configurations.
Downloading the kaguy-styles_e84_s17000.safetensors File
Since the .safetensors file exceeds Git LFS storage limits, it is provided via a download link.

Download the kaguy-styles_e84_s17000.safetensors file here
(kaguya safe tensor download : https://docs.google.com/uc?export=download&id=1wnS0CEitjSv_SfX0LLZITVcplqebr6TC)
After downloading, place the file in the model_assets/kaguy-styles/ directory, then ensure your configuration points to the correct path for this custom voice.

Downloading the LLaMA 3.1 Model
To run this project, you will need to download the LLaMA 3.1 model locally, as it is not included in this repository.

Download the LLaMA 3.1 model from the official Meta AI repository or Hugging Face (depending on availability).
Place the LLaMA model in a local directory (e.g., models/llama3.1/).
Update the configuration files to point to the location of the locally downloaded LLaMA model.
Make sure the LLaMA 3.1 model is properly set up for generating chatbot responses within the project.

Troubleshooting
If you encounter Git LFS quota issues, consider cleaning up LFS-tracked files or purchasing additional data packs.
For issues related to CUDA or cuDNN versions, ensure they are correctly installed and configured as per the project requirements.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Make sure to replace your_download_link_here with the actual download link for the safetensors file and ensure the LLaMA model is correctly configured locally. Let me know if you need any further changes!
