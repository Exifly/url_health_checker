from typing import List
import requests


class DiscordManager:
    _webhook_url: str
    _title: str
    _description: str
    _color: int
    _fields: List

    def __init__(self, webhook_url: str, fields: List, title: str, description: str, color: int):
        self._webhook_url = webhook_url
        self._fields = fields
        self._title = title
        self._description = description
        self._color = color

    def send_message(self) -> bool:
        data = {
            "embeds": [
                {
                    "title": self._title,
                    "description": self._description,
                    "color": self._color,
                    "fields": self._fields
                }
            ]
        }

        result = requests.post(
            self._webhook_url,
            json=data
        )
        return result.status_code == 204
