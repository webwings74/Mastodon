# Mastodon
A very small project to post a message, optionally with an image, to Mastodon. Nothing more, nothing less. Initially through input in the application. A version that accepts input from the command line is also needed.

## Dependencies
* **config.json** for the Mastodon user's access credentials.
* **mastodon Python module** must be installed in the (virtual) environment with ```pip3 install Mastodon.py```

## Files
* **PostMastodon.py** is a small example program that asks for a text message, then optionally a path to an image, and posts it to Mastodon.
* **PutMastodon.py** is a second "version" of the program that can also post to Mastodon using a command-line argument.
* **config.json** holds the user's API credentials. Update it with your own credentials and rename it to **secrets.json**.

## Python virtual environment
On macOS you can easily create a virtual environment with: ```python3 -m venv mastodon-venv```.
To activate the Python virtual environment on macOS: ```source mastodon-venv/bin/activate```.
