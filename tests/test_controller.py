"""Very basic tests"""

from pages.login_page import LoginPage
from game_controller import GameController


def test_controller(android_client: GameController):
    """Login to the app, open the controller activity and check some functionality"""
    android_client.driver.implicitly_wait(3)
    LoginPage(android_client).tap_continue().select_first_profile()
