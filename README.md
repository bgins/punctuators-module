# punctuators-module

This Lilypad module implements https://huggingface.co/1-800-BAD-CODE/punctuation_fullstop_truecase_english to correct punctuation and casing in English.

## Local development

Build the Docker image.

```sh
docker build -t punctuators:latest .
```

Run inference:

```sh
docker run  -e INPUT_TEXT="i love this amazing module" -v $(pwd)/outputs:/outputs punctuators:latest
```

## Publish image

The image must be published for resource provider's to fetch when running the module:

Build and publish for `linux/amd64` and `linux/arm64`:

```sh
docker buildx build --platform linux/amd64,linux/arm64 -t <your-registry>/punctuators:latest --push .
```

## Run the module

Download the latest Lilypad binary: https://github.com/Lilypad-Tech/lilypad/releases

See the Lilypad docs for more information on setting a web3 private key: https://docs.lilypad.tech/lilypad/lilypad-testnet/quick-start/setting-up-metamask.

Run the module on the Lilypad network:

```sh
lilypad run github.com/bgins/punctuators-module:v0.1.0 -i input_text="all of the words are hard to read because we need to punctuate we need to capitalize too"
```

Open the directory reported by this command and the results will be in `outputs/result.json`.
