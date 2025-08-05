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
  

# GÜNCELLENMİŞ DETAYLI INSTALLATION BILGISI

- Projeyi kurmak için öncelikle git clone <repo-link> komutuyla repoyu klonlayın ve cd <repo-klasörü> ile proje dizinine girin. Python 3.10+ kurulu olduğundan emin olun ve tercihen python -m venv venv ile sanal ortam oluşturup aktif edin. Ardından pip install -r requirements.txt komutuyla gerekli bağımlılıkları yükleyin. Proje kök dizininde .env dosyası oluşturun ve içine CLAUDE_API_KEY=your_key_here (CLAUDE'dan aldiginiz api key)satırını ekleyin. Gmail API’yi etkinleştirmek için Google Cloud Console’a gidin, Gmail API’yi aktif edin, OAuth 2.0 Client ID oluşturun ve credentials.json dosyasını indirerek utils/ klasörüne koyun. Tüm bu adımlar tamamlandıktan sonra python main.py komutuyla sistemi başlatabilirsiniz; ilk çalıştırmada tarayıcıdan Gmail hesabınıza giriş yaparak yetkilendirme yapmanız istenir. Sistem gelen son e-postaları alır, Claude ile sınıflandırır, gerekiyorsa yanıt oluşturur, kalite kontrolü yapar ve sonucu reports/ klasörüne JSON dosyası olarak kaydeder.


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
