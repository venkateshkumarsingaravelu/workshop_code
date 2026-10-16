import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Write a TikTok-style quote."}
]

def count_chat_tokens(messages):
    total = 0
    for msg in messages:
        total += len(encoding.encode(msg["content"]))
    return total

print("Chat token count:", count_chat_tokens(messages))
