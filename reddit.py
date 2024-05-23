import praw
import time

#This function takes subreddits and attributes as input
#It iterates through the subreddits provided and retrieves every attribute from each post found within each post within the subreddits
#The function returns an array called data filled with dictionaries each containing an individual post info

def get_data(subreddits, attributes, limiter, sleeptime):
    #Connection to reddit api, requires private key and client id which can be made found by making a reddit api key
    reddit = praw.Reddit(
        client_id= input("Enter client_id: "),
        client_secret= input("Enter client_secret: "),
        user_agent="stories",
    )
    
    data = []

    for subreddit in subreddits:
        current = reddit.subreddit(subreddit)
        for post in current.top(limit=limiter):
            post_data = {attr: getattr(post, attr, None) for attr in attributes}
            data.append(post_data)
        time.sleep(sleeptime)
        
    return data

def main():
    #The subreddits that will be utilized in order to get the stories
    subreddits = [
        "TIFU", "IAmA", "relationships", "nosleep", "prorevenge",
        "casualconversation", "personalfinance", "confession", "MaliciousCompliance",
        "AmItheAsshole", "JustNoMIL", "creepypasta",
        "shortscarystories", "ScaryStories", "Paranormal",
        "UnresolvedMysteries", "TalesFromRetail", "TalesFromTechSupport",
        "TalesFromYourServer", "TalesFromTheFrontDesk", "TalesFromTheCustomer",
        "TalesFromThePharmacy", "TalesFromThePizzaGuy", "TalesFromCallCenters",
        "TalesFromTheSquadCar"
    ]

    #The attributes that will be taken from each post from the Reddit API
    attributes = [
        'id', 'title', 'selftext', 'created_utc', 'subreddit',
        'num_comments', 'score', 'upvote_ratio'
    ]
    
    print(len(get_data(subreddits, attributes, 5, 1)))
    
if __name__ == "__main__":
    main()