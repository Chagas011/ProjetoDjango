
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def make_chrome_browser(*options):
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    if os.environ.get('SELENIUM_HEADESS') == '1':
        chrome_options.add_argument('--headless')
    chrome_service = Service(
        executable_path='/home/chagas/projetodjango/bin/chromedriver')
    brower = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return brower


if __name__ == '__main__':
    browser = make_chrome_browser('--headless')
    browser.get('https://www.youtube.com/')
