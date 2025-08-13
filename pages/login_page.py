"""Google password manager page"""

import time
from appium.webdriver.common.appiumby import AppiumBy


class LoginPage:
    """Google password manager login / Profile login"""

    def __init__(self, controller):
        self.driver = controller.driver

    continue_button = "com.google.android.gms:id/continue_button"
    cancel_button = "com.google.android.gms:id/cancel"

    def tap_continue(self):
        """Tap Continue button and wait (should replace waits with element wait for)"""
        self.driver.implicitly_wait(4)
        element = self.driver.find_element(AppiumBy.ID, self.continue_button)
        element.click()
        self.driver.implicitly_wait(4)
        return self

    def tap_cancel(self):
        """Tap Cancel button to dismiss dialog"""
        element = self.driver.find_element(AppiumBy.ID, self.cancel_button)
        element.click()
        self.driver.implicitly_wait(2)
        return self

    def select_first_profile(self):
        """TODO: This is quick hack, we should have account page independent of google login"""
        self.driver.implicitly_wait(5)
        first_profile = self.driver.find_element(
            AppiumBy.XPATH,
            "(//android.view.View[@resource-id='promo_profile_gate_profile'])[1]",
        )
        first_profile.click()
        self.driver.implicitly_wait(4)
        return self
