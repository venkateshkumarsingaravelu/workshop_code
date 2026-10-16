from openai import OpenAI

from dotenv import load_dotenv
from openai import OpenAI
import os

# Load environment variables
load_dotenv()

# Initialize client with custom base URL
client = OpenAI(
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

messages = [
  {
    "role": "user",
    "content": [
      {
        "type": "text",
        "text": "What is in this image, video and audio?"
      },
      {
        "type": "image_url",
        "image_url": {
          "url": "https://live.staticflickr.com/3851/14825276609_098cac593d_b.jpg"
        }
      # },
      # {
      #   "type": "video_url",
      #   "video_url": {
      #     "url": "https://storage.googleapis.com/cloud-samples-data/video/JaneGoodall.mp4"
      #   }
      # },
      # {
      #   "type": "input_audio",
      #   "input_audio": {
      #     "data": "UklGRnoGAABXQVZFZm10IBAAAAABAAEAQB",
      #     "format": "wav"
      #   }
      }
    ]
  }
]

# First API call. Reasoning shares the output budget with the
# answer, so reserve room (>= ~2000 tokens) for visible text
response = client.chat.completions.create(
  model="meta/muse-spark-1.2",
  messages=messages,
  max_tokens=2000,
  extra_body={"reasoning": {"effort": "medium"}}
)

# Extract the assistant message with reasoning_details
# (the model's reasoning comes back as an encrypted blob)
reply = response.choices[0].message
print(reply)
# Preserve the assistant message with reasoning_details
messages += [
  {
    "role": "assistant",
    "content": reply.content,
    "reasoning_details": reply.reasoning_details  # Pass back unmodified
  },
  {"role": "user", "content": "Are you sure? Think carefully."}
]

# Second API call - model continues reasoning from where it left off
response2 = client.chat.completions.create(
  model="meta/muse-spark-1.2",
  messages=messages,
  max_tokens=2000,
  extra_body={"reasoning": {"effort": "medium"}}
)