#!/usr/bin/env python

import os
import sys

import requests
from discord_webhook import DiscordWebhook, DiscordEmbed

HASH_URL = 'https://www.fuzzwork.co.uk/dump/mysql-latest.tar.bz2.md5'
HASH_FILE = 'hash_file'
WEBHOOK_URL = os.environ['WEBHOOK_URL']

# Ask Fuzzworks whats the current hash
r = requests.get(HASH_URL)
current_hash = r.text.split(' ')[0]

hash_file = os.path.join(
    os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))), HASH_FILE)

# Check what is the last hash we knew of
with open(hash_file, 'r') as f:
    known_hash = f.read().strip()

# If hashes are still the same, do nothing
if known_hash == current_hash:
    sys.exit(0)

with open(hash_file, 'w') as f:
    f.write(current_hash)

webhook = DiscordWebhook(url=WEBHOOK_URL)
embed = DiscordEmbed(title='New SDE Detected',
                     description='It looks like there is a new SDE.\n' +
                                 f'Old hash  `{known_hash}`\n' +
                                 f'New hash: `{current_hash}`', color='03b2f8')
webhook.add_embed(embed)
webhook.execute()
