import unittest
from urllib.request import urlopen

from flask_testing import LiveServerTestCase
from selenium import webdriver

from trivial_app import create_app


class TestBase(LiveServerTestCase):
    def create_app(self):
        config_name = 'testing'
        app = create_app(config_name)
        app.config.update(
            LIVESERVER_PORT=5000
        )
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        self.driver = webdriver.Chrome()
        self.driver.get(self.get_server_url())

    def tearDown(self):
        self.driver.quit()

    def test_server_is_up_and_running(self):
        response = urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)

# test to ensure that the new text is displayed when the button is clicked.
    def test_text_displayed_button(self):
        self.driver.find_element_by_id("button").click()
        self.assertEqual("Hello World!! Welcome!", driver.find_element_by_id("text").text)


if __name__ == '__main__':
    unittest.main()
