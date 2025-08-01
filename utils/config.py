import os
from dotenv import load_dotenv

load_dotenv()

CLAUDE_API_KEY = os.getenv("ANTHROPIC_API_KEY")