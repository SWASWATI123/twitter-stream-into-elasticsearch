# Tweeter into ElasticSearch

connect twitter using twitter api and put tweet into ElasticSearch.


## Python version
```
$ python -V
Python 3.5.0
```

## Install Elasticsearch package
```
pip install Elasticsearch
```

## Set Env Twitter OAuth

```
export TWITTER_CONSUMER_KEY=YOUR KEY
export TWITTER_CONSUMER_SECRET=YOUR KEY
export TWITTER_ACCESS_TOKEN=YOUR KEY
export TWITTER_ACCESS_TOKEN_SECRET=YOUR KEY
```

## Up ElasticSearch by docker.
[https://github.com/forest6511/Hinagata/tree/master/docker](https://github.com/forest6511/Hinagata/tree/master/docker)

## Run
```
python ./twitter-streaming.py 
```

## Confirm twitter stream data by kibara

http://localhost:5601/

## TODO

Need to create mapping.json
