# Post a message to Mastodon, including via the terminal & command line
# for example: python3 PutMastodon.py "$(pip list)" posts a message with the output of the pip list command

import json
import sys
from mastodon import Mastodon

# Step 1: Load the API credentials from secrets.json
with open("secrets.json", "r") as config_file:
    config = json.load(config_file)

mastodon = Mastodon(
    access_token=config["access_token"],
    api_base_url=config["api_base_url"]
)

# Step 2: Determine the message and optional image
if not sys.stdin.isatty():  # Check whether something comes in via stdin
    message = sys.stdin.read().strip()
elif len(sys.argv) > 1:  # Check whether an argument was given
    message = sys.argv[1]
else:  # Otherwise ask the user for input
    message = input("Enter the message you want to post on Mastodon: ")

# Optional image (only via argument or input, not via stdin)
image_path = sys.argv[2] if len(sys.argv) > 2 else input("Enter the path to the image (leave empty if you don't want to upload an image): ")

# Step 3: Upload the image (if provided)
media_id = None
if image_path:
    try:
        media = mastodon.media_post(image_path)
        media_id = media['id']
        print("Image uploaded successfully!")
    except Exception as e:
        print(f"An error occurred while uploading the image: {e}")

# Step 4: Post the message
mastodon.status_post(message, media_ids=[media_id] if media_id else None)

print("Message posted!")
