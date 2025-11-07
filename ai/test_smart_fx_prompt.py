import openai
import json

# Load your prompt
with open("smart_fx_prompt.txt", "r") as f:
    base_prompt = f.read()

# Mock FX data (just an example)
fx_data = {
    "pair": "AUD/USD",
    "rates": [0.665, 0.667, 0.669, 0.670, 0.672],  # increasing trend
    "dates": ["2025-07-29", "2025-07-30", "2025-07-31", "2025-08-01", "2025-08-02"]
}

# Insert FX data into prompt
final_prompt = base_prompt.replace("{{INSERT_JSON_HERE}}", json.dumps(fx_data))

# Call OpenAI API (replace with your API key)
openai.api_key = "sk-..."

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": final_prompt}]
)

print(response.choices[0].message["content"])
