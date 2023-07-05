# TwitterWebScrapeTool
# NBA Twitter Scraper

A Python script to scrape NBA-related tweets from a specific Twitter account. It uses snscrape for scraping and Textbelt for sending the scraped data as an SMS.

## Prerequisites

Ensure these Python libraries are installed:

- snscrape
- requests

To install the required libraries, run:


## Usage

1. Replace `'RECIPIENT'` and `'YOURAPIKEY'` with your phone number and Textbelt API key.
2. Run the script with `python filename.py` (replace `filename.py` with the name of your file).

This script scrapes the most recent 100 tweets from @TheNBACentral that contain the keyword "Report:". It removes URLs from the tweets and sends the 3 most recent approved tweets via SMS.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss.

