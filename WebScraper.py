import re
import snscrape.modules.twitter as sntwitter
import requests

maxTweets = 100
dateAndContent = []
approvedContentList = []

def approvedContent(tweet, keyword):
    return(keyword in tweet.content)

def removeUrls(text):
    urlPattern = re.compile(r'https?://\S+|www\.\S+')
    return urlPattern.sub(r'', text)

for tweetNum, tweet in enumerate(sntwitter.TwitterUserScraper("DbsContents").get_items()):
    if tweetNum >= maxTweets:
        break
    else:
        if approvedContent(tweet, “JJK”):
            dateAndContent.append([tweet.date, tweet.content])
        
approvedTweets = len(dateAndContent)

for tweetIndex in range(approvedTweets):
    tweet = dateAndContent[tweetIndex]
    convertedHour = int(tweet[0].strftime("%H"))

    if convertedHour < 0 or convertedHour > 23:
        break

    tweet_content_no_url = removeUrls(tweet[1])
    approvedContentList.append(tweet_content_no_url)

    if tweetIndex + 1 < approvedTweets:
        nextTweet = dateAndContent[tweetIndex + 1]
        nextHour = int(nextTweet[0].strftime("%H"))

    if convertedHour < nextHour:
        break

for i, tweet in enumerate(approvedContentList):
    print("{}. {}\n".format(i + 1, tweet))

recentTweets = approvedContentList[:3]

# insert your own key from textbelt and your recipient phone number 
for eachTweet in recentTweets:
    JJKUPDATE = requests.post('https://textbelt.com/text', {'phone': 'RECIPIENT','message': eachTweet,'key': 'YOURAPIKEY',})
print(JJKUPDATE.json())


