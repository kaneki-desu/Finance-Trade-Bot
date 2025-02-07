import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from datetime import datetime, timedelta
import pytz
import pprint 
pp = pprint.PrettyPrinter(indent=4)
import time

# Define base URL
news_url = "https://economictimes.indiatimes.com/markets/stocks/news"
response = requests.get(news_url)
soup = BeautifulSoup(response.text, 'html.parser')
each_story_divs = soup.find_all('div', class_='eachStory')
# storyPage=news_url+ each_story_divs[1].find('a')['href']
storyPages = [
    news_url + story_div.find('a')['href']
    for story_div in each_story_divs
    if story_div.find('a') and 'href' in story_div.find('a').attrs
]

# Set timezone to IST (Indian Standard Time)
ist = pytz.timezone('Asia/Kolkata')

# Get current date and time in IST
yesterday_date = (datetime.now(ist) - timedelta(days=1)).strftime('%d-%m-%Y')
today_date = datetime.now(ist).strftime('%d-%m-%Y')

# Define CSV filename with date

data_folder="E:\TradeBot\Scrapped-Data"
csv_filename = os.path.join(data_folder, f"scraped_news_{today_date}.csv")
# Scrape the story pages
storyPages = [
    news_url + story_div.find('a')['href']
    for story_div in each_story_divs
    if story_div.find('a') and 'href' in story_div.find('a').attrs
]

data = []  # List to store extracted data

for i, storyPage in enumerate(storyPages, 1):
    try:
        response = requests.get(storyPage, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        page_content = soup.find('div', class_='artText')

        if page_content:
            text_content = page_content.get_text(strip=True)
        else:
            text_content = "Content not found"

        relative_path = storyPage.replace(news_url, "")  # Remove base URL

        data.append({'Date': today_date, 'Relative Path': relative_path, 'Content': text_content})
        print(f"✅ {i}/{len(storyPages)}: Scraped {storyPage}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to fetch {storyPage}: {e}")
        data.append({'Date': today_date, 'Relative Path': "Request failed", 'Content': 'Request failed'})

# Convert to DataFrame
df = pd.DataFrame(data)

# Check if the file exists to append data
if os.path.exists(csv_filename):
    existing_df = pd.read_csv(csv_filename)
    df = pd.concat([existing_df, df], ignore_index=True)  # Append new data

# Save to CSV
df.to_csv(csv_filename, index=False)
print(f"✅ Data saved to {csv_filename}")
time.sleep(10)
print("EXecuted")
