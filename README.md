# 🤖 Jarvis AI Assistant

Jarvis AI Assistant is a Python-based desktop AI assistant powered by Google's Gemini AI model and Text-to-Speech technology. It can answer questions, execute system commands, open websites, take screenshots, and interact with users through natural language conversations.

This project is being developed in multiple phases, with each phase adding new capabilities to transform Jarvis into a fully-featured personal AI assistant.

---

## 🚀 Features (Phase 1)

### AI-Powered Conversations

* Integrated with Google Gemini AI
* Answers general knowledge questions
* Provides intelligent and contextual responses

### Text-to-Speech

* Converts AI responses into spoken audio
* Adjustable speech speed
* Cleans Markdown formatting before speaking

### System Commands

* Open Google Chrome
* Open YouTube
* Open Google Search
* Display current time
* Capture screenshots

### Smart Response Handling

* Removes Markdown symbols such as:

  * *
  * **
  * #
  * `
* Produces cleaner and more natural speech output

---

## 📁 Project Structure

```text
Jarvis AI Assistant
│
├── main.py          # Main application controller
├── brain.py         # Gemini AI integration
├── commands.py      # System command execution
├── voice.py         # Text-to-Speech functionality
├── screenshots/     # Saved screenshots
└── README.md
```

---

## 🛠️ Technologies Used

* Python
* Google Gemini API
* Pyttsx3
* PyAutoGUI
* Webbrowser Module
* Datetime Module

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/jarvis-ai-assistant.git
```

### Navigate to Project Folder

```bash
cd jarvis-ai-assistant
```

### Install Dependencies

```bash
pip install google-generativeai
pip install pyttsx3
pip install pyautogui
```

---

## 🔑 Configure Gemini API

Open:

```python
brain.py
```

Replace:

```python
genai.configure(api_key="YOUR_API_KEY")
```

with your Gemini API key.

---

## ▶️ Run Jarvis

```bash
python main.py
```

---

## 💡 Example Commands

```text
What is Artificial Intelligence?

What is Machine Learning?

Open Chrome

Open YouTube

Open Google

What is the time?

Take a screenshot
```

---

## 📌 Current Limitations

* Text input only
* No voice recognition
* No memory system
* No computer vision
* No wake-word detection

---

# 🚀 Future Improvements

## Phase 2 – Voice Control

* Speech-to-Text
* Microphone input
* Wake word detection
* Hands-free interaction

Example:

```text
Hey Jarvis, open Chrome.
```

---

## Phase 3 – Memory System

* Remember user preferences
* Store personal information
* Persistent memory using JSON database

Example:

```text
Remember my favorite language is Python.
```

---

## Phase 4 – Computer Vision

* OpenCV integration
* Webcam access
* Object detection
* Scene understanding

Example:

```text
Jarvis, what do you see?
```

---

## Phase 5 – Desktop Automation

* Open applications
* File management
* Folder organization
* System control

---

## Phase 6 – AI Agent Capabilities

* Task planning
* Multi-step reasoning
* Autonomous workflows
* Research assistant functionality

---

## Future Long-Term Goals

* Face Recognition
* Voice Authentication
* Email Assistant
* Calendar Management
* PDF Analysis
* Data Analysis Assistant
* Smart Home Integration
* Personal Productivity Assistant

---

## 👨‍💻 Author

**Vishal Bhatti**

B.Tech AI & Robotics Engineering
Guru Nanak Dev University, Amritsar

Passionate about Artificial Intelligence, Computer Vision, Robotics, and Intelligent Systems.

---

## ⭐ Project Status

Current Version: **Phase 1 Complete ✅**

Next Milestone: **Voice-Controlled Jarvis (Phase 2) 🎤**
