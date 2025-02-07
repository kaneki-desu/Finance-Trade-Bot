
Note : This project is still in development. This is just the basic gist of the project

🚀 AI-Powered Stock Trading Bot

An intelligent trading assistant that leverages market indicators, real-time news sentiment analysis, and automated trading via Zerodha's API to optimize stock market decisions.





📊 Features

🔢 Market Indicator Analysis:

Trained on popular indicators like RSI, MACD, Moving Averages, etc.

AI identifies the best indicators to predict price actions.

🔖 Real-Time News Sentiment Analysis:

Web scraper tracks current stock news.

Classifies news as positive, negative, or neutral using NLP.

Sentiment influences trading decisions.

🤖 Automated Trading (v2 Feature):

Executes trades automatically using Zerodha's API.

Optimizes buy/sell points based on technical data and news sentiment.

🔄 Continuous Learning:

Model adapts based on previous trades and evolving market trends.



🚚 Getting Started

1. Clone the Repository:

git clone https://github.com/kaneki-desu/Finance-Trade-Bot.git
cd Finance-Trade-Bot

2. Create & Activate Virtual Environment:

python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

3. Install Required Libraries:

pip install -r requirements.txt

4. Run the Bot:

python main.py

🔄 How It Works

Data Collection:

Technical Indicators: The bot gathers real-time stock data and calculates indicators.

News Scraping: Scrapes financial news from trusted sources.

Sentiment Analysis:

Uses NLP techniques to assess if news is positive, negative, or neutral.

AI Decision Making:

Combines technical analysis and sentiment for informed trading decisions.

Automated Trading:

Executes trades via Zerodha's API (Version 2 feature).

📈 Sample Results



Sample dashboard showcasing market indicators, news sentiment, and trading actions.

🕹️ Technologies Used

Python — Core language

TensorFlow & PyTorch — For AI/ML models

BeautifulSoup & Requests — Web scraping

Pandas & NumPy — Data manipulation

Matplotlib — Data visualization

Zerodha Kite API — Automated trading

🌟 Future Enhancements

🔌 Complete Zerodha API Integration: Full automation with error handling.

💡 Advanced Risk Management: Stop-loss, take-profit strategies.

🌐 Interactive Dashboard: Visualize trades, market indicators, and sentiment.

🔄 Model Retraining: Continuous learning with new data inputs.



🚀 Contact

📧 Email: sibajit.mazumdar@gmail.com🌟 GitHub: kaneki-desu📲 

Happy Trading! 📈🚀

