![SeAT](http://i.imgur.com/aPPOxSK.png)
# sde-detector

![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/eveseat/sde-detector)

A simple script to detect new SDE's for import. Used to post to the eveseat Discord #sde-bot channel.  
Please use the main SeAT repository [here](https://github.com/eveseat/seat) for issues.

## running

The container should be run as a cronjob with something like this (use `crontab -e`):

```bash
docker run --rm -e WEBHOOK_URL="https://discord.com/api/webhooks/<key>" -v $(pwd)/hash_file:/app/hash_file eveseat/sde-detector
```
