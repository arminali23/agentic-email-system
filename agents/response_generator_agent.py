from anthropic import Anthropic
from utils.config import CLAUDE_API_KEY
from utils.retry_helper import retry_claude_call

client = Anthropic(api_key=CLAUDE_API_KEY)

def generate_response(email_text, sender_name, company_name, category):
    prompt = f"""
You are an AI assistant responding to emails on behalf of a company.

Based on the email content below, generate a professional and helpful response.

Instructions:
- Keep the tone polite and helpful.
- Do NOT include greetings like "Hi Claude" or "Hello there".
- Do NOT include subject lines.
- Keep it concise and directly address the user's issue.
- Use the sender's name and company if available.

Category: {category}
Sender Name: {sender_name}
Company: {company_name}

Email content:
\"\"\"
{email_text}
\"\"\"

Now write the email body only.
"""

    def call():
        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=500,
            temperature=0.5,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text.strip()

    result = retry_claude_call(call)
    return result if result else "[ERROR] claude failed to generate response."