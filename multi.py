from dotenv import load_dotenv
from openai import OpenAI
import os
import base64

# Load environment variables
load_dotenv()

client = OpenAI(
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

# Encode a local audio file as base64 (example: input.wav)
with open("sample.wav", "rb") as f:
    audio_b64 = base64.b64encode(f.read()).decode("utf-8")

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Describe what is in this image, video, and audio, and suggest a marketing angle."
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": "https://live.staticflickr.com/3851/14825276609_098cac593d_b.jpg"
                }
            },
            {
                "type": "video_url",
                "video_url": {
                    "url": "https://storage.googleapis.com/cloud-samples-data/video/JaneGoodall.mp4"
                }
            },
            {
                "type": "input_audio",
                "input_audio": {
                    "data": audio_b64,
                    "format": "wav"
                }
            }
        ]
    }
]

# First API call with multimodal + reasoning
response = client.chat.completions.create(
    model="meta/muse-spark-1.2",  # or any multimodal-capable model on your endpoint
    messages=messages,
    max_tokens=2000,
    extra_body={"reasoning": {"effort": "medium"}}
)

reply = response.choices[0].message
print("\n=== FIRST RESPONSE ===\n")
print(reply.content)

# Preserve assistant message + reasoning for follow-up
messages += [
    {
        "role": "assistant",
        "content": reply.content,
        "reasoning_details": reply.reasoning_details
    },
    {
        "role": "user",
        "content": "Are you sure? Think carefully and refine the marketing insight."
    }
]

# Second API call continues reasoning
response2 = client.chat.completions.create(
    model="meta/muse-spark-1.2",
    messages=messages,
    max_tokens=2000,
    extra_body={"reasoning": {"effort": "medium"}}
)

reply2 = response2.choices[0].message
print("\n=== SECOND RESPONSE ===\n")
print(reply2.content)
