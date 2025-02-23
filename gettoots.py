import json
from mastodon import Mastodon

# Stap 1: Laad de API-credentials uit een apart configuratiebestand
# Verander secret.json in config.json en bewerk config.json met eigen API gegevens.
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
