"""
This is the PDL (Property Desciption Language) for HarmonyOS app testing, which is 
kind of DSL(Domain Sepcific Language).
Please checkout our doc and paper for details.
"""

from hmdriver2._client import HmClient
from hmdriver2.driver import Driver
from hmdriver2._uiobject import UiObject
from typing import TYPE_CHECKING, Type
if TYPE_CHECKING:
    pass


# from uiautomator2._selector import Selector, UiObject
# from uiautomator2 import Device as Driver
from typing import Any, Union, TYPE_CHECKING
if TYPE_CHECKING:
    from kea.droidbot import DroidBot

import time

class PDL(Driver):
    
    def __init__(self, delay=1, serial=None) -> None:
        self.delay = delay
        super().__init__(serial=serial)

    def set_device_serial(self, serial):
        pass
    
    def __new__(cls: Type[Any], serial: str) -> Any:
        return super().__new__(cls, serial)

    def __call__(self, **kwargs: Any) -> "Ui":
        kwargs
        ui = Ui(self, **kwargs)
        return ui

    def set_droidbot(self, droidbot:"DroidBot"):
        self.droidbot = droidbot

    def rotate(self, mode: str):
        self.droidbot.device.save_screenshot_for_report(event_name="rotate", event = self)
        super().set_orientation(mode)
        time.sleep(1)

    def press(self, key: Union[int, str], meta=None):
        self.droidbot.device.save_screenshot_for_report(event_name="press", event = key)
        super().press(key, meta)


class Ui(UiObject):
    def __init__(self, session:"PDL", **kwargs) -> None:
        client = session._client
        droidbot = session.droidbot
        self.droidbot = droidbot
        super().__init__(client, **kwargs)

    def click(self, offset=None):
        self.droidbot.device.save_screenshot_for_report(event_name="click", event = self)
        super().click()

    def long_click(self, duration: float = 0.5):
        self.droidbot.device.save_screenshot_for_report(event_name="long_click", event = self)
        super().long_click()
    
    def input_text(self, text):
        self.droidbot.device.save_screenshot_for_report(event_name="input_text " + text, event = self)
        super().input_text(text)
        