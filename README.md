# JJKTwitterWebScraper

This python script leverages the `snscrape` module to scrape a Twitter user's tweets and filters them based on a specific keyword. Once it collects and filters the tweets, it will remove any URLs present within the tweet content, and then sends the most recent three approved tweets as a text message using the `textbelt` API.

## Prerequisites

To run this script, you will need:

- Python 3.6 or above
- `snscrape` module 
- `requests` module
- `re` (Regular Expression) module

You can install the `snscrape` and `requests` packages using pip:

\```bash
pip install snscrape requests
\```

## Getting Started

1. Clone this repository.
\```bash
git clone https://github.com/AmaroTruong/JJKTwitterWebScraper.git
\```
2. Navigate to the directory.
\```bash
cd Project
\```
3. Open the script file (`WebScraper.py`) in your preferred text editor.
4. Update `YOURAPIKEY` with your textbelt API key and `RECIPIENT` with the recipient's phone number:
\```python
JJKUPDATE = requests.post('https://textbelt.com/text', {'phone': 'RECIPIENT','message': eachTweet,'key': 'YOURAPIKEY',})
\```

## Running the Script

Once you have installed the prerequisites and updated the recipient's phone number and API key, you can run the script with:

\```bash
python script.py
\```

If the script runs successfully, it will print out the selected tweets, and send the most recent three to the specified phone number. If there are any errors, they will be printed to the console.

## Code Overview

This script has three primary functions:

- `approvedContent(tweet, keyword)`: This function checks if a given keyword is present in a tweet's content.
- `removeUrls(text)`: This function removes any URLs from the given text.
- The main body of the script scrapes a given Twitter user's tweets, filters them based on a keyword, removes URLs, checks the tweet times, and sends a subset of the tweets as a text message.

## Screenshots
<img width="681" alt="Screenshot 2023-07-05 at 12 48 19 AM" src="https://github.com/AmaroTruong/JJKTwitterWebScraper/assets/137460611/e02be8ff-2423-4744-abaa-8080633e4bf7">

## How it works

Tweets from the Twitter account, "@DbsContents" are scraped to keep track of the most recent updates about "JJK" (Jujutsu Kaisen).

With the use of the snscrape library and its API endpoints, the tweets are compiled into a list. This involves several string manipulations and iterations over the tweets.

Specifically focusing on the keyword "JJK", these relevant tweets are organized into a JSON request for Textbelt's API, a service that specializes in SMS automation.

Every day @ 7:30 PM, (23:30 UTC) the script would be running on a python everywhere, in cohesion with PyInstaller, to send a message to my personal phone about JJK news/leaks.






