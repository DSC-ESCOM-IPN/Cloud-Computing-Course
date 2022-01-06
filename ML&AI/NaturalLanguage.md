# Entity and Sentiment Analysis with the Natural Language API

In this lab we'll use the Natural Language API to analyze tweets.

_First of all you need an [API KEY](https://console.cloud.google.com/apis/credentials) and you need to open a terminal and store that key as env var:_

```
export API_KEY=<YOUR-KEY>
```

## Text to use

You need a text to analyze, so look for a tweet you like or take the following example and store it in a file:

```
nano request.json
```


```
{
  "document":{
    "type":"PLAIN_TEXT",
    "content":"Joanne Rowling, who writes under the pen names J. K. Rowling and Robert Galbraith, is a British novelist and screenwriter who wrote the Harry Potter fantasy series."
  },
  "encodingType":"UTF8"
}
```

_If you want to use the tweet or any other text replace it in the json_


## Entity Analysis
```
curl "https://language.googleapis.com/v1/documents:analyzeEntities?key=${API_KEY}" \
  -s -X POST -H "Content-Type: application/json" --data-binary @request.json
```

## Sentiment Analysis

```
curl "https://language.googleapis.com/v1/documents:analyzeSentiment?key=${API_KEY}" \
  -s -X POST -H "Content-Type: application/json" --data-binary @request.json
```

To understand the output:
* score - is a number from -1.0 to 1.0 indicating how positive or negative the statement is.
* magnitude - is a number ranging from 0 to infinity that represents the weight of sentiment expressed in the statement, regardless of being positive or negative.

## Syntax Analysis

```
curl "https://language.googleapis.com/v1/documents:analyzeSyntax?key=${API_KEY}" \
  -s -X POST -H "Content-Type: application/json" --data-binary @request.json
```
**This info allows you to make some analysis like a [parse tree](https://en.wikipedia.org/wiki/Parse_tree#Dependency-based_parse_trees)**
