#!/usr/bin/env python

import requests
import os
import sys
from slacker import Slacker

HASH_URL = 'https://www.fuzzwork.co.uk/dump/mysql-latest.tar.bz2.md5'
HASH_FILE = 'hash_file'
SLACK_API_KEY = os.environ['SLACK_API_KEY']
SLACK_CHANNEL = '#development'

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

print(f'New SDE detected as {current_hash}')

with open(hash_file, 'wb') as f:
    f.write(current_hash)

slack = Slacker(SLACK_API_KEY)
slack.chat.post_message(SLACK_CHANNEL,
                        'Possible new SDE available at https://www.fuzzwork.co.uk/dump/ !\n' +
                        'Old hash: {hash}\n'.format(hash=known_hash) +
                        'New hash: {hash}'.format(hash=current_hash),
                        username='SDE Bot')
