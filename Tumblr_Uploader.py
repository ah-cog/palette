import pytumblr

# Authorization information
consumer_key = 'pA9FeSm9NZR9TyKdKR0SigFE2EXgLirTnKBc4s67LabGL3raoS'
consumer_secret = 'R3TReZ9sA7h04lkJdTskJNBsR4ycZc0jhsCHXAGF2oxOx6MeqZ'
oauth_token = 'qvtcaalyQaoywuwBvqVZ3RYtqWkDqfN1f3lXBNOyjrwi3uJaeX'
oauth_secret = '3eUIJCneaNrBCVx8Nrl55uu8yxgTYQyFlNp7AeTwfBs7wEcYke'

# Authenticate with Tumblr
client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    oauth_token,
    oauth_secret,
)

client.create_photo("colorspace-discrete", state="published", tags=["testing", "ok"], data="leggies.jpg")
