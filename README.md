# Monzo Webhook Schema

![Tests](https://github.com/trickeydan/monzo-webhook-schema/workflows/Tests/badge.svg)
![LGPL Licence](https://img.shields.io/badge/license-LGPL3-green.svg)
![Bees](https://img.shields.io/badge/bees-110%25-yellow.svg)

This is a work in progress project to document the complete schema for the [Monzo Webhook API](https://docs.monzo.com/#webhooks).

It is implemented in Python using the [Pydantic](https://pydantic-docs.helpmanual.io/) data validation library.

## How did you make this?

The schema is based on my observations of data from the API. In order to make it complete, contributions from the community are needed. This means that we'll be able to cover a wider variety of transaction types.

## Usage

The `MonzoWebhookSchema` class can be used to validate and access data programatically. A JSON Schema can also be generated from this file.

You can use this to easily create applications that use real-time data from Monzo!

```python
from fastapi import FastAPI
from monzo_webhook import MonzoWebhookSchema

app = FastAPI

@app.route("/mywebhook")
async def webhook(data: MonzoWebhookSchema) -> str:
    if data.amount < 0:
        print(f"Received £{data.amount/100}")
    else:
        print(f"Spent £{data.amount/100} on {data.category}")
    return "Success"
```