# Mastodon
Een heel klein projectje om een bericht, eventueel met een afbeelding, op Mastodon te plaatsen. Niet meer, niets minder. In eerste instantie via input in de applicatie. Ook een versie nodig die via de command-line een invoer kan hebben.

## Afhankelijkheden
* **config.json** voor de toegangsgegevens van de Mastodon gebruiker.
* **mastodon Python module** dient in de (virtuele) omgeving geïnstallert te worden met ```pip3 install Mastodon.py```

## Bestanden
* **PostMastodon.py** is een klein voorbeeldprogramma waarin een tekstbericht wordt gevraagd en daarna kan eventueel een pad naar een afbeelding worden opgegeven om dit dan te plaatsen op Mastodon.
* **PutMastodon.py** tweede "versie" van het programma dat ook d.m.v. een argument op de command-line iets kan plaatsen op Mastodon.
* **config.json** heeft de API gegevens van de gebruiker, deze dient bijgewerkt te worden met de eigen gebruikers gegevens en worden hernoemd naar **secrets.json**

## Virtuele Python omgeving
Een virtuele omgeving kun je op de MacOS eenvoudig aanmaken met: ```python3 -m venv mastodon-venv```.
Het starten van een virtuele Python omgeving op MacOS: ```source mastodon-venv/bin/activate```.
