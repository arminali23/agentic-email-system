from anthropic import Anthropic
from utils.config import CLAUDE_API_KEY
from utils.retry_helper import retry_claude_call

client = Anthropic(api_key=CLAUDE_API_KEY)

def classify_email(email_text):
    prompt = f"""
You are an intelligent email classification agent.

Your task is to analyze the email content below and respond **only** in the following exact 4-line format (no extra text):

category: <Support | Newsletter | Outbound | Verification>
sender Name: <Full name if available, else N/A>
company: <Company name if available, else N/A>
needs response: <Yes | No>

ONLY provide those 4 lines. Do NOT add explanations, introductions, or commentary.

Email:
\"\"\"
{email_text}
\"\"\"
"""

    def call():
        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=300,
            temperature=0,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text

    result = retry_claude_call(call)
    return result if result else "[ERROR] claude failed to classify email."