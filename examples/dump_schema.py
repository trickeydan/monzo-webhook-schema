"""Dump a JSON Schema of the Monzo Webhook."""
from monzo_webhook import MonzoWebhookSchema

print(MonzoWebhookSchema.schema_json(indent=2))
