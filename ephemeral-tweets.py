#!/usr/bin/env python
# ephemeral tweets
# requirement: pip install python-twitter

import twitter
import time
import random

# secrets, keys and tokens. create an app at apps.twitter.com to get some
api = twitter.Api(consumer_key='',
                consumer_secret='',
                access_token_key='',
                access_token_secret='')

handle = 'your_twitter_username'

while True:
    statuses = api.GetUserTimeline(str(handle), since_id = 0, count = 200)

    for status in statuses:
        api.DestroyStatus(status.id)
        break

    time.sleep(3600 * random.random())
    continue
