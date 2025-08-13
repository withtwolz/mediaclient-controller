"""Netflix Game Controller and Components"""

import os
from typing import Any, Dict, Sequence, Tuple

from appium import webdriver
from appium.webdriver.client_config import AppiumClientConfig
from appium.options.android.uiautomator2.base import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

from settings import AppiumSettings


class Direction:
    """A base directional class"""

    left: Tuple[int] = (-100, 0)
    right: Tuple[int] = (100, 0)
    up: Tuple[int] = (0, 100)
    down: Tuple[int] = (0, -100)


class AnalogStick:
    """A directional analog stick"""

    id: str = "id_analogstick"


class DirectionalPad:
    """A directional pad"""

    id: str = "id_dpad"


class SettingsButton:
    """The toolbar-left gear/settings button"""

    id: str = "id_settings"


class HomeButton:
    """The toolbar Netflix home button"""

    id: str = "id_logo"


class HamburgerMenu:
    """The toolbar-right hamburger menu"""

    id: str = "id_menu"


class ActionButtons:
    """The right side 1-4 buttons, A/B/X/Y"""

    a_button: str = "id_button_a"
    b_button: str = "id_button_b"
    x_button: str = "id_button_x"
    y_button: str = "id_button_y"


#################
#  Controllers  #
#################


class GameController:
    """Generic game controller"""

    def __init__(self, desired_caps: Dict[str, Any]):
        """Init our controller parts and appium"""
        self.settings = AppiumSettings()
        self.client_config = AppiumClientConfig(
            remote_server_addr=self.settings.get_server_url(),
            direct_connection=True,
            keep_alive=False,
            ignore_certificates=True,
        )
        self.driver = webdriver.Remote(
            options=UiAutomator2Options().load_capabilities(desired_caps),
            client_config=self.client_config,
        )

        self.astick = AnalogStick
        self.dpad = DirectionalPad
        self.toolbar_settings = SettingsButton
        self.toolbar_home = HomeButton
        self.toolbar_hamburger = HamburgerMenu
        self.action_buttons = ActionButtons

    def stick_left(self):
        """Use the stick to go left"""
        return self.drag_stick(Direction.left)

    def drag_stick(self, direction: Direction):
        """Analog stick is first tapped to active, then dragged toward direction"""
        self.driver.find_element(AppiumBy.ID, self.astick.id)

        return self

    def tap_toolbar_settings(self):
        """Tap the settings button in center toolbar"""
        self.driver.find_element(AppiumBy.ID, self.toolbar_settings)

    def tap_toolbar_home(self):
        """Tap the home button in center toolbar"""
        self.driver.find_element(AppiumBy.ID, self.toolbar_home)

    def tap_toolbar_hamburger(self):
        """Tap the hamburger button in center toolbar"""
        self.driver.find_element(AppiumBy.ID, self.toolbar_hamburger)

    def tap_a_button(self):
        """Tap the A button"""
        self.driver.find_element(AppiumBy.ID, self.action_buttons.a_button)

    def tap_b_button(self):
        """Tap the B button"""
        self.driver.find_element(AppiumBy.ID, self.action_buttons.b_button)

    def tap_x_button(self):
        """Tap the X button"""
        self.driver.find_element(AppiumBy.ID, self.action_buttons.x_button)

    def tap_y_button(self):
        """Tap the Y button"""
        self.driver.find_element(AppiumBy.ID, self.action_buttons.y_button)
