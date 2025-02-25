import transformers
import requests

from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "the-hugging-face-model-name"  # Replace with the actual name
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)


port = 30000

url = f"http://localhost:{port}/v1/chat/completions"

data = {
    "model": "Qwen/Qwen2.5-3B",
    "messages": [{"role": "user", "content": "What is the capital of France?"}],
}

response = requests.post(url, json=data)
print(response.json())
