from status_checker import StatusChecker
from dotenv import load_dotenv
import schedule
import time
import os

load_dotenv()

WEBHOOK_URL = os.getenv('WEBHOOK_URL')
URL_TO_CHECK = os.getenv('URL_TO_CHECK')


if __name__ == "__main__":
    status_checker = StatusChecker(WEBHOOK_URL, URL_TO_CHECK)
    schedule.every(5).minutes.do(status_checker.run)
    while True:
        schedule.run_pending()
        time.sleep(1)
