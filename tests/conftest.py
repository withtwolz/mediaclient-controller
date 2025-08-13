"""Pytest fixtures"""

from typing import Any, Generator
import pytest

from game_controller import GameController
from settings import AppiumSettings


@pytest.fixture
def android_client() -> Generator[GameController, Any, None]:
    """Yield an instantiated android client"""
    controller = GameController(
        desired_caps=AppiumSettings(platform_name="Android").get_desired_capabilities()
    )
    yield controller
    controller.driver.quit()
