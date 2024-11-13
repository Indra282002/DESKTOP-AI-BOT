# Veronica - Your AI Assistant

### Overview

Veronica is an AI-powered virtual assistant designed to help users with various tasks, from opening applications and checking the weather to fetching news and conversing intelligently.
This project leverages speech recognition, text-to-speech, and language generation technologies to provide an interactive and intuitive assistant experience.Veronica leverages a Generative AI model
to conduct meaningful and logical conversations with users. It can respond to open-ended questions, provide information, and offer assistance based on natural language inputs. 
With its advanced AI model configuration, Veronica can answer complex questions, offer insights, and even engage in casual, context-aware conversations.

### Features

- ***Voice-Activated Commands***: Users can give voice commands, and Veronica will respond and act on them.<br>
- ***Application Launcher***: Opens popular desktop applications (Chrome, Firefox, VLC, VS Code, OBS Studio) with voice commands.<br>
- ***Web Navigation***: Opens commonly used websites like YouTube, LinkedIn, Google, Facebook, Instagram, and WhatsApp.<br>
- ***Time and Date Announcements***: Provides the current time and date.<br>
- ***Weather Information***: Fetches real-time weather details for a specified city.<br>
- ***News Fetching***: Retrieves news articles based on user queries.<br>
- ***Conversational AI with Generative Responses***: Engages in logical and meaningful conversations, answering user questions and providing helpful responses.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Indra282002/DESKTOP-AI-BOT.git
   cd DESKTOP-AI-BOT
   ```
2. **Install Dependencies**: Make sure to have Python installed, then run:-
   ```python
   pip install -r requirements.txt
   ```
3. **Set Up Environment Variables**:
   - Create a .env file in the root directory
   - Add your API keys as follows:
```java
   GOOGLE_API_KEY=your_google_api_key
   WEATHER_API_KEY=your_weather_api_key
   NEWS_API_KEY=your_news_api_key
```

### Usage
1. **Run Veronica**:
   ```bash
   python veronica.py
   ```
2. **Using Voice Commands**:
   - Example: Say, "Open Chrome" or "What's the weather in [City Name]?"
   - Conversation: To chat, just ask questions or give statements like, "Tell me a joke" or "How are you?"

### Examples
***Voice Commands***<br>
- "Open YouTube" - Opens the YouTube website.<br>
- "What's the weather?" - Asks Veronica to fetch the weather of a specified city.<br>
- "Give me news about technology" - Retrieves news articles about technology.<br>

***Sample Output***: In the terminal, Veronica will display news titles, descriptions, and provide audible responses for weather, time, and date.
---
### Contributing
Feel free to fork the repository, make changes, and submit a pull request. All contributions are welcome!
