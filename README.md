![SeAT](http://i.imgur.com/aPPOxSK.png)
# sde-detector

A simple script to detect new SDE's for import. Used to post to the eveseat slack #development channel.  
Please use the main SeAT repository [here](https://github.com/eveseat/seat) for issues.

## running

The container should be run as a cronjob with:

```bash
docker run --rm -it -e SLACK_API_KEY=FOO -v $(pwd)/hash_file:/app/hash_file eveseat/sde-detector
```
