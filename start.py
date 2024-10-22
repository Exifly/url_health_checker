from status_checker import StatusChecker
from dotenv import load_dotenv
import schedule
import time
import os

load_dotenv()

WEBHOOK_URL = os.getenv("WEBHOOK_URL")
URL_TO_CHECK = os.getenv("URL_TO_CHECK")


if __name__ == "__main__":
    print("Starting Url checker..")
    status_checker = StatusChecker(WEBHOOK_URL, URL_TO_CHECK)
    print(
        f"Status Checker Configuration: \n\tUrl to check: {status_checker._url_to_check}"
    )
    schedule.every(5).seconds.do(status_checker.run)
    print("Started!")
    while True:
        schedule.run_pending()
        time.sleep(1)
