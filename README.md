# Client Library for Deebot devices (Vacuums)

[![PyPI - Downloads](https://img.shields.io/pypi/dw/deebot-client?style=for-the-badge)](https://pypi.org/project/deebot-client)
<a href="https://www.buymeacoffee.com/edenhaus" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-black.png" width="150px" height="35px" alt="Buy Me A Coffee" style="height: 35px !important;width: 150px !important;" ></a>

## Installation

If you have a recent version of Python 3, you should be able to
do `pip install deebot-client` to get the most recently released version of
this.

## Usage

To get started, you'll need to have already set up an EcoVacs account
using your smartphone.

You are welcome to try using this as a python library for other efforts.
A simple usage might go something like this:

```python
import aiohttp
import asyncio
import logging
import time

from deebot_client.api_client import ApiClient
from deebot_client.authentication import Authenticator, create_rest_config
from deebot_client.commands import *
from deebot_client.commands.clean import CleanAction
from deebot_client.events import BatteryEvent
from deebot_client.mqtt_client import MqttClient, create_mqtt_config
from deebot_client.util import md5
from deebot_client.device import Device

device_id = md5(str(time.time()))
account_id = "your email or phonenumber (cn)"
password_hash = md5("yourPassword")
country = "de"


async def main():
  async with aiohttp.ClientSession() as session:
    logging.basicConfig(level=logging.DEBUG)
    rest_config = create_rest_config(session, device_id=device_id, country=country)

    authenticator = Authenticator(rest_config, account_id, password_hash)
    api_client = ApiClient(authenticator)

    devices_ = await api_client.get_devices()

    bot = Device(devices_[0], authenticator)

    mqtt_config = create_mqtt_config(device_id=device_id, country=country)
    mqtt = MqttClient(mqtt_config, authenticator)
    await bot.initialize(mqtt)

    async def on_battery(event: BatteryEvent):
      # Do stuff on battery event
      if event.value == 100:
        # Battery full
        pass

    # Subscribe for events (more events available)
    bot.events.subscribe(BatteryEvent, on_battery)

    # Execute commands
    await bot.execute_command(Clean(CleanAction.START))
    await asyncio.sleep(900)  # Wait for...
    await bot.execute_command(Charge())


if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  loop.create_task(main())
  loop.run_forever()
```

A more advanced example can be found [here](https://github.com/And3rsL/Deebot-for-Home-Assistant).

### Note for Windows users

This library cannot be used out of the box with Windows due a limitation in the requirement `aiomqtt`.
More information and a workaround can be found [here](https://github.com/sbtinstruments/aiomqtt#note-for-windows-users)

## Thanks

My heartfelt thanks to:

- [deebotozmo](https://github.com/And3rsL/Deebotozmo), After all, this is a debotozmo fork :)
- [sucks](https://github.com/wpietri/sucks), deebotozmo was forked from it :)
- [xmpppeek](https://www.beneaththewaves.net/Software/XMPPPeek.html), a great library for examining XMPP traffic flows (
  yes, your vacuum speaks Jabbber!),
- [mitmproxy](https://mitmproxy.org/), a fantastic tool for analyzing HTTPS,
- [click](http://click.pocoo.org/), a wonderfully complete and thoughtful library for making Python command-line
  interfaces,
- [requests](http://docs.python-requests.org/en/master/), a polished Python library for HTTP requests,
- [Decompilers online](http://www.javadecompilers.com/apk), which was very helpful in figuring out what the Android app
  was up to,
- Albert Louw, who was kind enough to post code
  from [his own experiments](https://community.smartthings.com/t/ecovacs-deebot-n79/93410/33)
  with his device, and
- All the users who have given useful feedback and contributed code!
