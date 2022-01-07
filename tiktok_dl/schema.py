"""Schema Collection for TikTok Video JSON."""
import json
import os


def parse_json(direcroy, filename):
    with open(os.path.join(direcroy, filename), "r", encoding="utf8") as f:
        return json.load(f)


def schemas():
    """Read Schemas from available schemas."""
    directory = os.path.dirname(os.path.realpath(__file__))
    return [
        parse_json(directory, i)
        for i in os.listdir(os.path.join(directory, "schemas"))
        if ".json" in i
    ]
