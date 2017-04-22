# Tweeter into ElasticSearch

Note: This is just self-studying purpose!  
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

## My note
Reference:
[https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-kuromoji-tokenizer.html](https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-kuromoji-tokenizer.html)

#### delete index
``` 
DELETE /twitter
``` 

#### create index

``` 
PUT twitter
{
  "settings": {
    "index": {
      "analysis": {
        "tokenizer": {
          "kuromoji_user_dict": {
            "type": "kuromoji_tokenizer",
            "mode": "normal"
          }
        },
        "analyzer": {
          "my_analyzer": {
            "type": "custom",
            "tokenizer": "kuromoji_user_dict",
            "filter": [
              "kuromoji_part_of_speech"
            ]
          }
        }
      }
    }
  },
  "mappings": {
    "tweet": {
      "dynamic": "strict",
      "properties": {
        "tweet_id": {
          "type": "string"
        },
        "screen_name": {
          "type": "string",
          "analyzer": "my_analyzer"
        },
        "text": {
          "type": "string",
          "analyzer": "my_analyzer"
        },
        "hashtags": {
          "type": "nested",
          "properties": {
            "type": {
              "type": "string",
              "analyzer": "my_analyzer"
            }
          }
        }
      }
    }
  }
}
```

#### search all query (json type)
```
GET /twitter/tweet/_search
{
  "query": {
    "match_all": {
    }
  }
}
```

#### search '誕生日'  (json type)
```
GET /twitter/tweet/_search
{
  "query": {
    "match": {
      "text": "誕生日"
    }
  }
}
```

#### must search '誕生日' and 'おめでとう' and  'よろしく' (json type)
```
GET /twitter/tweet/_search
{
  "query": {
    "bool": {
      "must": [
        {"match": {
          "text": "誕生日"
        }},
        {"match": {
          "text": "おめでとう"
        }},
        {"match": {
          "text": "よろしく"
        }}
      ]
    }
  }
}
```
#### must search '誕生日' and　must not 'おめでとう' (json type)
```
GET /twitter/tweet/_search
{
  "query": {
    "bool": {
      "must": [
        {"match": {
          "text": "誕生日"
        }}
      ],
      "must_not": [
        {"match": {
          "text": "おめでとう"
        }}
      ]
    }
  }
}
```