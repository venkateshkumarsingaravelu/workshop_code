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

# ---------------------------------------------------------
# 1. ZERO-SHOT PROMPT
# ---------------------------------------------------------
zero_shot = client.chat.completions.create(
    model="~deepseek/deepseek-v4-flash-latest",
    messages=[
        {"role": "user", "content": 
            "How can we improve customer engagement for our new product launch?"}
    ]
)

print("\n=== ZERO-SHOT RESPONSE ===\n")
print(zero_shot.choices[0].message.content)


# ---------------------------------------------------------
# 2. FEW-SHOT PROMPT
# ---------------------------------------------------------
few_shot = client.chat.completions.create(
    model="~deepseek/deepseek-v4-flash-latest",
    messages=[
        {"role": "user", "content": 
            """
            You are helping with marketing strategy.

            Example 1:
            Q: How do we increase brand awareness?
            A: Use paid social ads, influencer partnerships, and consistent storytelling.

            Example 2:
            Q: How can we improve email open rates?
            A: Segment audiences, personalize content, and test subject lines.

            Now answer:
            Q: How can we improve customer engagement for our new product launch?
            A:
            """
        }
    ]
)

print("\n=== FEW-SHOT RESPONSE ===\n")
print(few_shot.choices[0].message.content)


# ---------------------------------------------------------
# 3. ROLE-BASED PROMPT
# ---------------------------------------------------------
role_prompt = client.chat.completions.create(
    model="~deepseek/deepseek-v4-flash-latest",
    messages=[
        {
            "role": "system",
            "content": (
                "You are the Head of Marketing for a fast-growing organization. "
                "Provide strategic, actionable, data-driven recommendations."
            )
        },
        {
            "role": "user",
            "content": "How can we improve customer engagement for our new product launch?"
        }
    ]
)

print("\n=== ROLE-BASED RESPONSE ===\n")
print(role_prompt.choices[0].message.content)


# ---------------------------------------------------------
# 4. COMBINED (ROLE + FEW-SHOT) — BEST QUALITY
# ---------------------------------------------------------
combined_prompt = client.chat.completions.create(
    model="~deepseek/deepseek-v4-flash-latest",
    messages=[
        {
            "role": "system",
            "content": (
                "You are the Head of Marketing. Provide strategic, data-driven recommendations."
            )
        },
        {
            "role": "user",
            "content": 
            """
            Example 1:
            Q: How do we increase brand awareness?
            A: Use multi-channel storytelling, influencer amplification, and consistent brand identity.

            Example 2:
            Q: How can we improve email open rates?
            A: Segment audiences, personalize messaging, and test subject lines.

            Now answer:
            Q: How can we improve customer engagement for our new product launch?
            A:
            """
        }
    ]
)

print("\n=== COMBINED ROLE + FEW-SHOT RESPONSE ===\n")
print(combined_prompt.choices[0].message.content)
