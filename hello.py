from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
client = OpenAI(
  base_url=os.getenv("OPENAI_BASE_URL"),
  api_key=os.getenv("OPENAI_API_KEY"),
)

# First API call with reasoning
response = client.chat.completions.create(
  model="inclusionai/ling-3.0-tiny:free",
  messages=[
          {
            "role": "user",
            "content": "How many r's are in the word 'rubber'?"
          }
        ],
  extra_body={"reasoning": {"enabled": True}}
)

# Extract the assistant message with reasoning_details
response = response.choices[0].message
print(response)

# Preserve the assistant message with reasoning_details
messages = [
  {"role": "user", "content": "How many r's are in the word 'strawberry'?"},
  {
    "role": "assistant",
    "content": response.content,
    "reasoning_details": response.reasoning_details  # Pass back unmodified
  },
  {"role": "user", "content": "Are you sure? Think carefully."}
]

# Second API call - model continues reasoning from where it left off
response2 = client.chat.completions.create(
  model="qwen/qwen3.8-max",
  messages=messages,
  extra_body={"reasoning": {"enabled": True}}
)