import asyncio
import datetime
import websockets
import json
import random
async def handler(websocket, path):
    while True:
        data = [
            {
                "test": 1,
                "test2": 2
            }
        ]
        await websocket.send(json.dumps(data))
        await asyncio.sleep(1)
start_server = websockets.serve(handler, "127.0.0.1", 5555)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
print("value?")
