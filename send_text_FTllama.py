import requests
import json


import ollama

def query_llama3(text):
    # Use ollama to interact with the LLaMA model
    response = ollama.chat(
        model='llama3.1',
        messages=[
            {
                'role': 'user',
                'content': text
            }
        ]
    )
    return response['message']['content']

#def query_llama3(text):
    #url = "http://localhost:11434/api/chat"  #  
    #headers = {"Content-Type": "application/json"}
    #data = {
        #"model": "llama3.1",
        #"messages": [
        #    {"role": "system", "content": "Provide answers based on fine-tuning."},
        #    {"role": "user", "content": text}
        #]
    #}
    
    #response = requests.post(url, headers=headers, data=json.dumps(data))
    
    #if response.status_code == 200:
    #    response_data = json.loads(response.content.decode())
    #    return response_data['message']['content']
    #else:
    #    return f"Error: {response.status_code}"