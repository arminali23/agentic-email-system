# AGENTIC EMAIL MANAGEMENT SYSTEM

This project is a multi-agent system that intelligently manages email workflows using AI agents powered by Claude (Anthropic API). The system reads emails from a Gmail inbox, classifies them, generates responses when needed, and evaluates the quality of each response — all fully automated.

# ARCHITECTURE

Role of Agents;

- Email Classifier Agent – Categorizes incoming emails and extracts data.
- Response Generator Agent – Writes personalized replies using Claude.
- Response Quality Checker Agent – Ensures the reply meets tone and quality guidelines.
- Orchestrator Agent – Manages agent communication and workflow.

# SETUP & INSTALLATION

```bash
git clone https://github.com/arminali23/agentic-email-system.git
cd agentic-email-system
```

- install python dependencies
- make sure you are using python 3.10+
- pip install -r requirements.txt
- setup claude api key
- create .env file and -> CLAUDE_API_KEY=your_key_here
- gmail API setup
- go to google cloud console
- enable gmail API.
- create OAuth 2.0 credentials and download credentials.json
- place credentials.json in the utils/ folder.

When running the script for the first time, a browser window will open to authenticate with Gmail.

- run the system with python main.py in terminal

# EXAMPLE USAGE

- Input (Email from Gmail):

Subject: Forgot my password

Hello,

I forgot my password and I am trying to reset it, but the reset link is not working.

Regards,
Armin from Bournemouth University

- OUTPUT
  [Classifier Agent Output]:
  Category: Support
  Sender Name: Armin
  Company: Bournemouth University
  Needs Response: Yes

[Response Generator Output]:
Thank you for reaching out...
(response content)

[Quality Checker Output]: PASS "quality assessment"
[Saved]: reports/armin_report.json
