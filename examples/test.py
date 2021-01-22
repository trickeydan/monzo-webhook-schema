from json import loads
from pathlib import Path

from monzo_webhook import MonzoWebhookSchema

for i in Path("reqs").iterdir():
    print(f"Attempting to load data from {i}")
    with i.open("r") as fh:
        MonzoWebhookSchema(**loads(fh.read()))
