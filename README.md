# Mastodon
Een heel klein projectje om een bericht, eventueel met een afbeelding, op Mastodon te plaatsen. Niet meer, niets minder. In eerste instantie via input in de applicatie. Ook een versie nodig die via de command-line een invoer kan hebben.

## Afhankelijkheden
* config.json voor de toegangsgegevens van de Mastodon gebruiker.
* mastodon Python module. Deze is in de (virtuele) omgeving te installeren via ```pip3 install Mastodon.py```

### Bestanden
* PostMastodon.py is een klein voorbeeldprogramma waarin een tekstbericht wordt gevraagd en daarna kan eventueel een pad naar een afbeelding worden opgegeven om dit dan te plaatsen op Mastodon.
* config.json heeft de API gegevens van de gebruiker, deze dient bijgewerkt te worden met de eigen gebruikers gegevens en worden hernoemd naar secrets.json
* mastodon-venv is de virtuele omgeving van Python, in dit geval versie 3.12, waaraan de Mastodon module is toegevoegd.
