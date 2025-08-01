from utils.gmail_handler import authenticate_gmail, get_latest_emails
from agents.orchestrator_agent import run_workflow

# gmail auth
service = authenticate_gmail()
emails = get_latest_emails(service)

# manual test
test = """
Subject: Forgot Password

Hello,

I forgot my password and I am trying to reset it, but the reset link is not working. 

Regards,
Armin from Bournemouth University
"""

print("\nProcessing test email...\n")
run_workflow(test)
for email in emails:
    print("\nProcessing new email...\n")
    run_workflow(email)