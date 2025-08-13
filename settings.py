"""Pydantic Settings"""

from dotenv import load_dotenv
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppiumSettings(BaseSettings):
    """BaseSettings for python appium setup"""

    load_dotenv(".env")
    model_config = SettingsConfigDict(env_file=".env")

    app_package: str
    device_name: str
    platform_name: str

    # Server config with defaults
    appium_host: str = "127.0.0.1"
    appium_port: int = 4723

    @field_validator("platform_name")
    def check_platform(cls, value: str):
        if value.lower() not in ["android", "ios"]:
            raise ValueError(
                f"platform_name must be one of ['Android', 'iOS'] not {value}"
            )
        return value

    def get_automation_name(self) -> str:
        return {"Android": "UiAutomator2", "ios": "XCUITest"}[self.platform_name]

    def get_desired_capabilities(self) -> dict:
        return {
            "platformName": self.platform_name,
            "deviceName": self.device_name,
            "appPackage": self.app_package,
            "automationName": self.get_automation_name(),
        }

    def get_server_url(self) -> str:
        return f"http://{self.appium_host}:{self.appium_port}"
