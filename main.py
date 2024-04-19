from bot import Bot

import asyncio
import os
import sys

from atexit import register
from config import LOGGER

async def auto_restart():
    while not await asyncio.sleep(2000):
        def _():
            os.system(f"kill -9 {os.getpid()} && python3 -m main.py")
        register(_)
        except Exception as a:
            self.LOGGER(__name__).warning(a)
            self.LOGGER(__name__).info(
                "BOT BERHASIL DI RESTART"
            )
            sys.exit()

Bot().run()
