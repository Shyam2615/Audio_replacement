import requests
import json

# Azure OpenAI settings
azure_openai_key = "22ec84421ec24230a3638d1b51e3a7dc"
azure_openai_endpoint = "https://internshala.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-08-01-preview"

def correct_transcription(text):
    headers = {
        "Content-Type": "application/json",
        "api-key": azure_openai_key
    }
    
    data = {
        "messages": [{"role": "user", "content": f'This is a sample text with some umms and grammatical mistakes. please correct it. and also remember give the response directly without any extra text {text}'}],
        "max_tokens": 500
    }
    
    response = requests.post(azure_openai_endpoint, headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        corrected_text = result["choices"][0]["message"]["content"].strip()
        return corrected_text
    else:
        return f"Failed to connect: {response.status_code} - {response.text}"