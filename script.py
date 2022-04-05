import sys
import os
from requests_html import HTMLSession

'''
Gets the full text body and hashtags for the given tweet.
This is done by rendering the actual HTML page for the tweet and scraping the
information from the HTML. 

This is far simplier than trying to string together different parts of the tweet from the database.

The only downside to this is, if a Tweet is no longer publically available, it's tweet body and hashtags cannot be gathered.
However given that we are using the most up to date version of the database, this should never happen.
'''
def get_Tweet_Full_Text_And_Hashtags(tweet):
    # Gets the tweet id for the given tweet from the dataset.
    id = tweet[tweet.index("id_str")+len("id_str")+3:tweet.index("full_text")-3:]
    # Opens a new HTML session
    session = HTMLSession()
    # Creates the URL to scrape. Twitter only requires the tweet ID. Username is not needed.
    url = "https://twitter.com/user/status/" + str(id)

    # gets the HTML and renders the page. 
    r = session.get(url)
    r.html.render(sleep=2)

    # Scrap the text body from the given tweet.
    tweet_text = r.html.find('.css-1dbjc4n.r-1s2bzr4', first=True)
    # We use a try catch here to catch instances of a tweet not having any text. 
    try:
        # Get the hashtags written into the text body.
        text = tweet_text.text.split()
        hashtags = [t for t in text if t.startswith("#")]
        hashtags = ', '.join(hashtags)
        
        # Remove any newline characters in the text body then return it and the hashtags.
        return tweet_text.text.replace('\n', ' '), hashtags
    except:
        return None, None

'''
Gets the number of likes and retweets. Note that in the database, the likes are labelled as "favorites".
'''
def get_Likes_and_Retweets(tweet):
    retweets = tweet[tweet.rindex('"retweet_count":') + len('"retweet_count":'):tweet.rindex('"favorite_count":')-1:]    
    likes = tweet[tweet.rindex('"favorite_count":') + len('"favorite_count":'):tweet.rindex('"favorited":')-1:]
    return retweets, likes

'''
Determines whether a given tweet is a Quote or a Retweet.
'''
def get_Retweet_and_Quote_Status(tweet):
    is_retweet = False
    is_quote = False

    # The database labels if a tweet is a Retweet for us.
    check_for_RT = tweet[tweet.index('"full_text":"')+len('"full_text":"'):tweet.index(',"truncated":')]

    # If the tweet's text body does NOT have "RT" (retweet), and the "is_quote_status" in the database IS NOT true...
    if "RT" not in check_for_RT and '"is_quote_status": true,' not in tweet:
        # ...then the given tweet is an original tweet and therefore nether a retweet or a quote.
        is_retweet = False
        is_quote = False
        return is_retweet, is_quote

    # If the tweet's text body does NOT have "RT" (retweet), and the "is_quote_status" in the database IS true...
    if "RT" not in check_for_RT and '"is_quote_status": true,' in tweet:
        # ...then we know that the given tweet is a quote of another tweet.
        is_retweet = False
        is_quote = True
        return is_retweet, is_quote

    # If the tweet's text body DOES have "RT" (retweet), and the "is_quote_status" in the database IS NOT true...
    if "RT" in check_for_RT and '"is_quote_status": true,' not in tweet:
        # ...then we know that the given tweet is a retweet.
        is_retweet = True
        is_quote = False
        return is_retweet, is_quote

    # If the tweet's text body DOES have "RT" (retweet), and the "is_quote_status" in the database IS true...
    if "RT" in check_for_RT and '"is_quote_status": true,' in tweet:
        # ...then we know that the given tweet is both a retweet and a quote tweet.
        is_retweet = True
        is_quote = True
        return is_retweet, is_quote
    pass

# path should be location of the month data.
path = sys.argv[1]
# Get a list of all the files in the given path.
files = os.listdir('./' + path)

# Check each file in the given path
for file in files:
    file = open(path + '/' + file, encoding='utf8')

    # We will write our results to the results directory with the same file name as the current file.
    to_write = open('./results/'+ file.name +'.txt', 'w+', encoding='utf-8')

    # Read all of the tweet data in the current file. 
    all_tweets = file.readlines()

    for tweet in all_tweets:
        # This list will hold all of the data for the current tweet.
        full_data_for_tweet = []
        
        # Get the text body and the hashtags for the current tweet.
        text_result, hashtags = get_Tweet_Full_Text_And_Hashtags(tweet)

        # If the current tweet doesn't have a body then append an empty string to the final data. Otherwise append the results.
        if text_result is not None:
            full_data_for_tweet.append(text_result)
            full_data_for_tweet.append(hashtags)
        else:
            full_data_for_tweet.append('')
            full_data_for_tweet.append('')

        # Get the retweets and likes for the current tweet.
        retweets, likes = get_Likes_and_Retweets(tweet)

        # Get whether the current tweet is a retweet, a quote tweet, or both.
        is_retweet, is_quote = get_Retweet_and_Quote_Status(tweet)

        # Write all of the gathered data for the current tweet to the list.
        full_data_for_tweet.append(retweets)
        full_data_for_tweet.append(likes)
        full_data_for_tweet.append(str(is_retweet))
        full_data_for_tweet.append(str(is_quote))
        
        # Convert the current data list to a string and write it to our file. 
        to_write.write(', '.join(full_data_for_tweet) + "\n")
    