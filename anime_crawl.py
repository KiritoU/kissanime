import logging
import time

from settings import CONFIG
from base import Crawler
from helper import helper

logging.basicConfig(format="%(asctime)s %(levelname)s:%(message)s", level=logging.INFO)

crawler = Crawler()

if __name__ == "__main__":
    page = 2
    while True:

        try:
            crawled_page = crawler.crawl_page(
                f"{CONFIG.KISSANIME_NEW_AND_HOST_PAGE}?page={page}"
            )
            if (
                not crawled_page
                and page >= CONFIG.KISSANIME_NEW_AND_HOST_PAGE_LAST_PAGE
            ):
                page = 2
            else:
                page += 1

        except Exception as e:
            helper.error_log(msg=f"anime crawl failed\n{e}", log_file="anime_crawl.log")
        time.sleep(CONFIG.WAIT_BETWEEN_ALL)
