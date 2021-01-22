# Monzo Webhook Schema

This is a work in progress project to document the complete schema for the Monzo Webhook API.

It is implemented in Python using the [Pydantic](https://pydantic-docs.helpmanual.io/) data validation library.

## How did you make this?

The schema is based on my observations of data from the API. In order to make it complete, contributions from the community are needed. This means that we'll be able to cover a wider variety of transaction types.

## Usage

The `MonzoWebhookSchema` class can be used to validate and access data programatically. A JSON Schema can also be generated from this file.

You can use this to easily create applications that use real-time data from Monzo!

```python
from flask import Flask, request
from monzo_webhook import MonzoWebhookSchema

app = Flask(__name__)

@app.route("/mywebhook")
def webhook():
    data = MonzoWebhookSchema(**request.get_json())

    if data.amount < 0:
        print(f"Received £{data.amount/100}")
    else:
        print(f"Spent £{data.amount/100} on {data.category}")
    return "", 200
```