# Speech to Text Transcription with the Cloud Speech API

In this lab we'll use the Speech API to extract text from songs.

_First of all you need an [API KEY](https://console.cloud.google.com/apis/credentials) and you need to open a terminal and store that key as env var:_

```
export API_KEY=<YOUR-KEY>
```

Following, you'll need a bucket that you can create by running: 
```
gsutil mb gs://YOUR-BUCKET-NAME/
```

## Prepare the audio

You can download a YouTube video with this [tool](https://yt1s.com/es88/youtube-to-mp3) and after that you'll need to convert it to a flac type, you can use this [other tool](https://convertio.co/es/mp3-flac/)
Note: **It is so important to use a 1 channel flac file**

Now you have to upload the audio file to you bucket.

## Request file

You need to create a request file as follow:
```
nano speech.json
```

```
{
  "config": {
      "encoding":"FLAC",
      "languageCode": "en-US"
  },
  "audio": {
      "uri":"gs://YOUR-BUCKET-NAME/Your-song.flac"
  },
}
```

## Get transcription

To start the transcription you'll use the following command:

```
curl -s -X POST -H "Content-Type: application/json" --data-binary @speech.json "https://speech.googleapis.com/v1/speech:longrunningrecognize?key=${API_KEY}"
```

This will return something like:

```
curl -s -X POST -H "Content-Type: application/json" --data-binary @speech.json "https://speech.googleapis.com/v1/speech:longrunningrecognize?key=${API_KEY}"
```
{
  "name": "###################"
}

You need to copy that number to run the following command:

```
curl -H "Content-Type: application/json; charset=utf-8" "https://speech.googleapis.com/v1/operations/"###################"?key=${API_KEY}"
```

**Try this with other languages**
