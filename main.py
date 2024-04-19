from bot import Bot

import asyncio
import os
import sys

from atexit import register

async def auto_restart():
    while not await asyncio.sleep(5):
        def _():
            os.system(f"kill -9 {os.getpid()} && python3 -m main.py")
        register(_)
        sys.exit(0)

Bot().run()
