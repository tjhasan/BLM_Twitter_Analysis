from string import digits
import sys
import os
import re
from requests_html import HTMLSession
'''
Todo:
1) Get Full Text of Tweet
    - Complete.
    - Uses HTML to get the full body. However some tweets no longer exist.
2) Get Tweet Hashtags
    - Complete.
3) Likes and Retweets
    - Complete.
4) Get Retweet & Quote Status
    - Complete.
5) Sarcasm
'''

def get_Tweet_Full_Text(tweet):
    id = tweet[tweet.index("id_str")+len("id_str")+3:tweet.index("full_text")-3:]
    session = HTMLSession()
    url = "https://twitter.com/user/status/" + str(id)

    r = session.get(url)
    r.html.render(sleep=2)

    tweet_text = r.html.find('.css-1dbjc4n.r-1s2bzr4', first=True)
    try:
        return tweet_text.text
    except:
        return None

def get_Tweet_Hashtags(tweet):
    try:
        temp = tweet[tweet.index('"entities":{"hashtags":[{"text":"')+len('"entities":{"hashtags":[{"text":"'):tweet.index('"symbols":[')]
    except:
        return []
    temp = re.sub(r'\W+', ' ', temp)
    temp = temp.translate({ord(k): None for k in digits})
    temp = temp.replace('indices', '')
    temp = temp.replace('text', '')
    temp = temp.split(' ')
    temp = [i for i in temp if i]
    return temp

def get_Likes_and_Retweets(tweet):
    retweets = tweet[tweet.rindex('"retweet_count":') + len('"retweet_count":'):tweet.rindex('"favorite_count":')-1:]    
    likes = tweet[tweet.rindex('"favorite_count":') + len('"favorite_count":'):tweet.rindex('"favorited":')-1:]
    return retweets, likes

def get_Retweet_and_Quote_Status(tweet:str):
    is_retweet = False
    is_quote = False

    check_for_RT = tweet[tweet.index('"full_text":"')+len('"full_text":"'):tweet.index(',"truncated":')]
    if "RT" not in check_for_RT and '"is_quote_status": true,' not in tweet:
        is_retweet = False
        is_quote = False
        return is_retweet, is_quote
    if "RT" not in check_for_RT and '"is_quote_status": true,' in tweet:
        is_retweet = False
        is_quote = True
        return is_retweet, is_quote
    if "RT" in check_for_RT and '"is_quote_status": true,' not in tweet:
        is_retweet = True
        is_quote = False
        return is_retweet, is_quote
    if "RT" in check_for_RT and '"is_quote_status": true,' in tweet:
        is_retweet = True
        is_quote = True
        return is_retweet, is_quote
    pass

path = sys.argv[1]
files = os.listdir('./' + path)

for file in files:
    file = open(path + '/' + file, encoding='utf8')
    all_tweets = file.readlines()
    for tweet in all_tweets:
        full_data_for_tweet = []
        
        text_result = get_Tweet_Full_Text(tweet)
        if text_result is not None:
            full_data_for_tweet.append(text_result)
        else:
            # End process for the current tweet. Go to next tweet.
            full_data_for_tweet.append(None)
        hashtags = get_Tweet_Hashtags(tweet)

        retweets, likes = get_Likes_and_Retweets(tweet)

        is_retweet, is_quote = get_Retweet_and_Quote_Status(tweet)

        full_data_for_tweet.append(hashtags)
        full_data_for_tweet.append(retweets)
        full_data_for_tweet.append(likes)
        full_data_for_tweet.append(is_retweet)
        full_data_for_tweet.append(is_quote)

        print(full_data_for_tweet)
        quit()
