# Post a simple message to Mastodon, optionally including an image.
# (C)2025 Richard, webwings.nl

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

# Step 2: Ask the user for a message and an optional image
message = input("Enter the message you want to post on Mastodon: ")
image_path = input("Enter the path to the image (leave empty if you don't want to upload an image): ")

# Step 3: Upload the image (if provided)
media_id = None
if image_path:
    try:
        media = mastodon.media_post(image_path)
        media_id = media['id']
        print("Image uploaded successfully!")
    except Exception as e:
        print(f"An error occurred while uploading the image: {e}")

# Step 4: Post the message (with or without image)
mastodon.status_post(message, media_ids=[media_id] if media_id else None)

print("Message posted!")