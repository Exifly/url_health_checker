from discord_manager import DiscordManager
from datetime import datetime
import requests


class StatusChecker:
    _webhook_url: str
    _url_to_check: str

    def __init__(self, webhook_url: str, url_to_check: str):
        self._webhook_url = webhook_url
        self._url_to_check = url_to_check

    def _is_online(self) -> tuple[bool, int]:
        try:
            response = requests.get(self._url_to_check)
            return response.status_code == 200, response.status_code
        except Exception as error:
            print(f"Error: {error}")
            return False, 0

    def run(self) -> None:
        is_online, status_code = self._is_online()
        if is_online:
            return

        discord_manager = DiscordManager(
            webhook_url=self._webhook_url,
            title="CODEISHOT IS CURRENTLY OFFLINE",
            description=f"the ping returned a status code of {status_code}",
            color=16711680,
            fields=[
                {"name": "Endpoint tested", "value": str(self._url_to_check)},
                {"name": "Status code", "value": str(status_code)},
                {"name": "Date", "value": str(datetime.now())},
            ],
        )

        discord_manager.send_message()
