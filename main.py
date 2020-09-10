from config import getApi
import os
import sys
import time

api = getApi('yUE9YEot8QIGwBbnNrxkdLjdx','uH4r7hq79OUDnYBcP70v62JHZHEsyXFXyRugw10lIHBnvetBTi','1303339753371250693-sM9QmDzPBynxjBB1XoPvO8tGosDM2N','TCPqkduFxdSWvUL7x7pc4vSHBiC4d6s3NKgbdkqPIoLxm')

tweets = 0
searchs = 0
limitTweets = 300
limitSearchs = 180

def endsWith(sentence, keyword):
    return sentence.endswith(keyword)

def postStatus(update, inReplyTo, media):
    global tweets
    tweets += 1
    api.PostUpdate(update, media=media, in_reply_to_status_id=inReplyTo)

def search(research, howMany):
    global searchs
    searchs += 1
    searchResults = api.GetSearch(raw_query="q="+research+"&result_type=recent&count="+howMany)
    for search in searchResults:
        if(endsWith(search.text, "passe par feuneu") or endsWith(search.text, "passe par Feuneu")):
            postStatus("@" + search.user.screen_name, search.id, "passeParFeuneu.mp4")

def start():
    global searchs
    global tweets
    global limitTweets
    global limitSearchs
    stop = False
    while(not stop):
        try:
            search("passe par feuneu", "100")
        except:
            print("Erreur (probablement de quota, on arrete)")
            stop = True
        if(searchs >= limitSearchs):
            print("Limite atteinte des searchs")
            stop = True
        elif(tweets >= limitTweets):
            print("Limite atteinte des tweets")
            stop = True
        print(f"On a tweeté {str(tweets)} fois !")
        time.sleep(5)
    print("Fini, on attend 3H maintenant et on reprend.")

start()
