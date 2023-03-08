#!/usr/bin/python3

""" Script that fetch the number of subscribers for a given subreddit."""
import requests


def number_of_subcribers(subreddit):
    """Set the HTTP headers for the request to the Reddit API"""

    headers = {'User-Agent': 'Scrapping_subscribers '}
    subreddit_url = "https://reddit.com/r/{}.json".format(subreddit)
    response = requests.get(subreddit_url, headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        subscriber_number = (
            json_data.get('data')
            .get('children')[0]
            .get('data')
            .get('subreddit_subscribers')
        )
        return subscriber_number
    else:
        return 0
