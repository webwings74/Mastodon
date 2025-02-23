# Plaatsen van een simpel bericht op Mastodon, eventueel inclusief een afbeelding.
# (C)2025 Richard, webwings.nl

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

# Stap 2: Vraag de gebruiker om een bericht en optionele afbeelding in te voeren
bericht = input("Voer het bericht in dat je wilt posten op Mastodon: ")
afbeelding_pad = input("Voer het pad naar de afbeelding in (laat leeg als je geen afbeelding wilt uploaden): ")

# Stap 3: Upload de afbeelding (indien opgegeven)
media_id = None
if afbeelding_pad:
    try:
        media = mastodon.media_post(afbeelding_pad)
        media_id = media['id']
        print("Afbeelding succesvol geüpload!")
    except Exception as e:
        print(f"Er is een fout opgetreden bij het uploaden van de afbeelding: {e}")

# Stap 4: Plaats het bericht (met of zonder afbeelding)
mastodon.status_post(bericht, media_ids=[media_id] if media_id else None)

print("Bericht geplaatst!")