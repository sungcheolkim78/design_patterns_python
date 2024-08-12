import os
import re
import threading
import urllib
import urllib.request
from urllib.parse import urljoin, urlparse

import httplib2
from bs4 import BeautifulSoup


class CrawlerSingleton(object):
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(CrawlerSingleton, cls).__new__(cls)
        return cls.instance


def navigate_site(max_links: int = 5):
    parser_crawlersingleton = CrawlerSingleton()

    while parser_crawlersingleton.url_queue:
        if len(parser_crawlersingleton.visited_url) == max_links:
            return

        url = parser_crawlersingleton.url_queue.pop()

        http = httplib2.Http()
        try:
            status, response = http.request(url)
        except Exception:
            continue

        parser_crawlersingleton.visited_url.add(url)
        print(url)

        bs = BeautifulSoup(response, "html.parser")

        for link in BeautifulSoup.findAll(bs, "a"):
            link_url = link.get("href")
            if not link_url:
                continue

            parsed = urlparse(link_url)

            if parsed.netloc and parsed.netloc != parsed_url.netloc:
                continue

            scheme = parsed_url.scheme
            netloc = parsed.netloc or parsed_url.netloc
            path = parsed.path

            link_url = scheme + "://" + netloc + path

            if link_url in parser_crawlersingleton.visited_url:
                continue

            parser_crawlersingleton.url_queue = [
                link_url
            ] + parser_crawlersingleton.url_queue


def download_images(thread_name):
    singleton = CrawlerSingleton()

    while singleton.visited_url:
        url = singleton.visited_url.pop()
        http = httplib2.Http()
        print(thread_name, "Downloading images from", url)

        try:
            status, response = http.request(url)
        except Exception:
            continue

        bs = BeautifulSoup(response, "html.parser")
        images = BeautifulSoup.findAll(bs, "img")

        for image in images:
            src = image.get("src")
            src = urljoin(url, src)

            basename = os.path.basename(src)
            print("basename:", basename)

            if basename != "":
                if src not in singleton.image_downloaded:
                    singleton.image_downloaded.add(src)
                    print("Downloading", src)

                    urllib.request.urlretrieve(src, os.path.join("images", basename))
                    print(thread_name, "finished downloading images from", url)


class ParallelDownloader(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print("Starting thread", self.name)
        download_images(self.name)
        print("Finished thread", self.name)


def main():
    crwSingleton = CrawlerSingleton()
    crwSingleton.url_queue = [main_url]
    crwSingleton.visited_url = set()
    crwSingleton.image_downloaded = set()

    navigate_site()

    if not os.path.exists("images"):
        os.makedirs("images")

    thread1 = ParallelDownloader(1, "thread-1", 1)
    thread2 = ParallelDownloader(2, "Thread-2", 2)

    thread1.start()
    thread2.start()


if __name__ == "__main__":
    main_url = "https://www.geeksforgeeks.org/"
    parsed_url = urlparse(main_url)
    main()
