# punctuators-module

This module implements https://huggingface.co/1-800-BAD-CODE/punctuation_fullstop_truecase_english to correct punctuation and casing in English.

## Build

Build the Docker image.

```
docker build -t punctuators:latest .
```

## Run local inference

Run the Docker image locally:

```
docker run  -e INPUT_TEXT="i love this amazing workshop" -v $(pwd)/outputs:/outputs punctuators:latest
```
