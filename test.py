from pathlib import Path
from json import loads

from monzo_schema import MonzoSchema

for i in Path("reqs").iterdir():
    print("Attempting to load data from {i}")
    with i.open("r") as fh:
        MonzoSchema(**loads(fh.read()))