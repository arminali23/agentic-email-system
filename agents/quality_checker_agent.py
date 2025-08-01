from anthropic import Anthropic
from utils.config import CLAUDE_API_KEY
from utils.retry_helper import retry_claude_call

client = Anthropic(api_key=CLAUDE_API_KEY)

def check_response_quality(response_text):
    prompt = f"""
You are a quality assurance assistant reviewing email responses.

Please assess the following response based on these criteria:
- Professional and polite tone
- Directly addresses the original email content
- Clear and easy to understand
- Free of grammar or spelling errors

If the response meets all criteria, reply exactly with: PASS

Otherwise, provide a short explanation of what's wrong.

Email response to review:
\"\"\"
{response_text}
\"\"\"
"""

    def call():
        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=200,
            temperature=0,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text.strip()

    result = retry_claude_call(call)
    return result if result else "[ERROR] claude failed to check response quality."