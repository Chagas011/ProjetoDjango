
import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from utils.browser import make_chrome_browser


class RecipeBaseTest(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.browser = make_chrome_browser()
        return super().setUp()

    def sleep(self, seconds=5):
        time.sleep(seconds)

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()


class RecipeHomeTest(RecipeBaseTest):

    def test_recipe_home(self):

        self.browser.get(self.live_server_url)
        self.sleep()
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('No recipes found here 🥲', body.text)
