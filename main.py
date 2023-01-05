import openai
import tweepy
import requests
import json
import time

openai.api_key = ""

consumer_key = "*"
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token,
                                access_token_secret)
api = tweepy.API(auth)

while True:
    print('ok')
    # retrieve and process mentions
    with open("last_mention_id.json", "r") as f:
        last_mention_id = json.load(f)

    mentions = api.mentions_timeline(since_id=last_mention_id)
    for mention in mentions:
        prompt = mention.text
        print(mention.text)
        response = openai.Image.create(prompt=prompt,
                                       model="image-alpha-001",
                                       size="256x256")
        image_url = response["data"][0]["url"]
        response = requests.get(image_url)

        with open("image.jpg", "wb") as f:
            f.write(response.content)
        user = mention.user.screen_name
        print(user)
        api.update_status_with_media(
            filename="image.jpg",
            status=f"@{user} Voici votre image générée par #DALLE {user}. Bot fai",
            in_reply_to_status_id=mention.id)
        last_mention_id = mention.id
    with open("last_mention_id.json", "w+") as f:
        json.dump(last_mention_id, f)
    time.sleep(5)  # wait for 1 hour before checking for new mentions
