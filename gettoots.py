import json
from mastodon import Mastodon

# Step 1: Load the API credentials from a separate configuration file
# Copy config.json to secret.json and edit it with your own API credentials.
with open("secret.json", "r") as config_file:
    config = json.load(config_file)

mastodon = Mastodon(
    access_token=config["access_token"],
    api_base_url=config["api_base_url"]
)

hashtag = "canada"
results = mastodon.timeline_hashtag(hashtag, limit=10)
for toot in results:
    print(toot['content'])
