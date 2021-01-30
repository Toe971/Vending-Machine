import asyncio
import datetime
import websockets
import json
import random
async def handler(websocket, path):
    data = [
        {
            "test": 1,
            "test2": 2
        }
    ]
    await websocket.send(json.dumps(data))
    await asyncio.sleep(1)


loop = asyncio.get_event_loop()
loop.set_debug(True)  # debug mode
try:
    loop.run_until_complete(handler())
finally:
    loop.run_until_complete(loop.shutdown_asyncgens())
    loop.close()

""" start_server = websockets.serve(handler, "127.0.0.1", 5555) """


""" asyncio.get_event_loop().run_until_complete()
asyncio.get_event_loop().run_forever()
 """
