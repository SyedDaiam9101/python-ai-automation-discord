# 🤖 Python AI Automation Lab

A clean, beginner-friendly collection of practical Python automation scripts. Perfect for students learning AI automation, file management, and Python best practices.

## ✨ Features

- **📁 Smart File Organizer** - Automatically organize messy folders by file type
- **💬 AI Chatbot** - Interactive chatbot with OpenAI support (or local fallback mode)
- **📧 Email Automation** - Send automated notifications and emails safely
- **🧪 Experiments Folder** - Space for testing and prototyping new ideas

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SyedDaiam9101/python-ai-automation-discord.git
   cd python-ai-automation-lab
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables** (optional)
   ```bash
   # Copy the example file
   cp .env.example .env
   
   # Edit .env and add your API keys if you want to use OpenAI
   ```

## 📖 Usage Examples

### 1. File Organizer

Automatically organize files in a messy folder:

```bash
python automation/file_organizer.py
```

**What it does:**
- Scans a target directory
- Groups files by type (images, documents, videos, etc.)
- Creates organized folders automatically
- Moves files safely

### 2. AI Chatbot

Interactive chatbot that works with or without an API key:

```bash
python automation/chatbotbasics.py
```

**Features:**
- ✅ Works immediately with **local fallback mode** (no API needed!)
- ✅ Upgrade to OpenAI GPT when you add an API key
- ✅ Maintains conversation history
- ✅ Type 'quit' or 'exit' to end the chat

### 3. Email Automation

Send automated emails safely:

```bash
python automation/email_bot.py
```

**⚠️ IMPORTANT SECURITY NOTES:**
- **Use App Passwords**, never your main email password
- Gmail users: [Create an App Password here](https://myaccount.google.com/apppasswords)
- Never commit your `.env` file to Git
- The script will never log your credentials

## 📁 Project Structure

```
python-ai-automation-lab/
│
├── automation/              # Production automation scripts
│   ├── __init__.py         # Package initialization
│   ├── file_organizer.py   # Smart file organization tool
│   ├── chatbotbasics.py    # AI chatbot (local + OpenAI)
│   └── email_bot.py        # Email automation system
│
├── experiments/            # Testing and prototyping area
│   └── test_script.py     # Example experimental script
│
├── .env.example           # Environment variables template
├── .gitignore            # Git ignore rules
├── LICENSE               # MIT License
├── README.md             # This file
└── requirements.txt      # Python dependencies
```

## 🔧 Configuration

### For AI Chatbot (Optional)

To use OpenAI's GPT models, add to your `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

**Don't have an API key?** No problem! The chatbot has a built-in local mode.

### For Email Automation (Optional)

To enable email features, add to your `.env` file:

```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password_here
```

**🔒 Security Best Practices:**
1. Use app-specific passwords (not your main password)
2. Never share your `.env` file
3. Keep `.env` in `.gitignore` (it already is!)

## 🤝 Contributing

Contributions are welcome! Here's how to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit with clear messages (`git commit -m 'Add amazing feature'`)
5. Push to your branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

### Code Guidelines

- Follow PEP8 style guidelines
- Add docstrings to functions
- Include type hints where helpful
- Keep code simple and readable
- Test your changes before submitting

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎓 Learning Resources

New to Python automation? Check these out:

- [Python Official Docs](https://docs.python.org/3/)
- [Real Python Tutorials](https://realpython.com/)
- [Automate the Boring Stuff](https://automatetheboringstuff.com/)

## 💡 Ideas for Expansion

Want to add more automation? Try these:

- Web scraper for price monitoring
- Social media post scheduler
- Automated backup system
- Data analysis pipeline
- Discord/Slack bot integration

## ⚡ Troubleshooting

**Issue: ModuleNotFoundError**
- Solution: Run `pip install -r requirements.txt`

**Issue: Chatbot not working**
- Solution: It should work in local mode automatically. Check for error messages.

**Issue: Email not sending**
- Solution: Verify you're using an app password, not your regular password

## 📬 Contact

Questions or suggestions? Open an issue on GitHub!

---

**Made with ❤️ for students learning Python automation**

