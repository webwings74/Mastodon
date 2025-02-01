# Bericht plaatsen op Mastodon, inclusief via de terminal & command-line
# bijvoorbeeld: python3 PutMastodon.py "$(pip list)" stuurt een bericht met de uitvoer van het commando pip list 

import json
import sys
from mastodon import Mastodon

# Stap 1: Laad de API-credentials uit config.json
with open("secrets.json", "r") as config_file:
    config = json.load(config_file)

mastodon = Mastodon(
    access_token=config["access_token"],
    api_base_url=config["api_base_url"]
)

# Stap 2: Bepaal bericht en optionele afbeelding
if not sys.stdin.isatty():  # Check of er iets via stdin binnenkomt
    bericht = sys.stdin.read().strip()
elif len(sys.argv) > 1:  # Controleer of er een argument is meegegeven
    bericht = sys.argv[1]
else:  # Anders vraag de gebruiker om invoer
    bericht = input("Voer het bericht in dat je wilt posten op Mastodon: ")

# Optionele afbeelding (alleen via argument of invoer, niet via stdin)
afbeelding_pad = sys.argv[2] if len(sys.argv) > 2 else input("Voer het pad naar de afbeelding in (laat leeg als je geen afbeelding wilt uploaden): ")

# Stap 3: Upload de afbeelding (indien opgegeven)
media_id = None
if afbeelding_pad:
    try:
        media = mastodon.media_post(afbeelding_pad)
        media_id = media['id']
        print("Afbeelding succesvol geüpload!")
    except Exception as e:
        print(f"Er is een fout opgetreden bij het uploaden van de afbeelding: {e}")

# Stap 4: Plaats het bericht
mastodon.status_post(bericht, media_ids=[media_id] if media_id else None)

print("Bericht geplaatst!")
