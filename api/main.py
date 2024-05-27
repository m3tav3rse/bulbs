# from machine import Pin
from asyncio import get_event_loop

from lib.nanoweb import HttpError, Nanoweb
from mod import discovery
from mod.conf import Conf
from mod.neostrip import NeoPixel, NeoStrip
from mod.webutils import get_body_json, write_response, write_response_json

conf = Conf()
led = NeoStrip(conf, NeoPixel(5, "pin"), NeoPixel(4, "pin"))
server = Nanoweb(port=8000, address='127.0.0.1')

@server.route("/connect")
async def connect(request):
    async def get():
        # sta = network.WLAN(network.STA_IF)

        await write_response_json(request, {
            "ssid": "mock",
            "status": "mocking",
            "connected": 2,
            "ip": "X",
        })

    async def post():
        try:
            body = await get_body_json(request)

            conf.set({
                "sta_ssid": body["ssid"],
                "sta_password": body["password"]
            })
        except ValueError as e:
            await write_response_json(request, {"message": str(e)}, 400, "Bad Request")
            return
        except KeyError:
            await write_response_json(request, {"message": "Invalid credentials"}, 400, "Bad request")
            return

        await write_response_json(request, {
            "message": "Reboot the device to apply changes"
        })

    try:
        await {"GET": get, "POST": post}[request.method]()
    except KeyError as e:
        raise HttpError(request, 404, "Not Found") from e


@server.route("/led")
async def led_get(request):
    if request.method != "GET":
        raise HttpError(request, 404, "Not Found")

    await write_response_json(request, {
        "on": led.get_power(),
        "color": led.get_color(),
        "brightness": led.get_brightness()
    })

@server.route("/led/on")
async def led_on(request):
    async def get():
        await write_response_json(request, {
            "on": led.get_power()
        })

    async def put():
        led.set_power(1)

        await write_response(request)

    try:
        await {"GET": get, "PUT": put}[request.method]()
    except KeyError as e:
        raise HttpError(request, 404, "Not Found") from e

@server.route("/led/off")
async def led_off(request):
    async def get():
        await write_response_json(request, {
            "off": 0 if led.get_power() else 1
        })

    async def put():
        led.set_power(0)

        await write_response(request)

    try:
        await {"GET": get, "PUT": put}[request.method]()
    except KeyError as e:
        raise HttpError(request, 404, "Not Found") from e

@server.route("/led/brightness")
async def brightness_get(request):
    if request.method != "GET":
        raise HttpError(request, 404, "Not Found")

    await write_response_json(request, {
        "brightness": led.get_brightness()
    })

@server.route("/led/brightness/*")
async def brightness_put(request):
    if request.method != "PUT":
        raise HttpError(request, 404, "Not Found")

    brightness = float(request.url.split("/")[-1])

    try:
        led.set_brightness(brightness)
    except Exception as e:
        await write_response_json(request, {"message": str(e)}, 400, "Bad Request")

        return

    await write_response(request)

@server.route("/led/color")
async def color_get(request):
    if request.method != "GET":
        raise HttpError(request, 404, "Not Found")

    await write_response_json(request, {
        "color": led.get_color()
    })

@server.route("/led/color/*")
async def color_put(request):
    if request.method != "PUT":
        raise HttpError(request, 404, "Not Found")

    color = f"#{request.url.split("/")[-1]}"

    try:
        led.set_color(color)
    except Exception as e:
        await write_response_json(request, {"message": str(e)}, 400, "Bad Request")

        return

    await write_response(request)

def start_server():
    loop = get_event_loop()
    http_server = server.run()

    loop.create_task(http_server)
    loop.create_task(discovery.server())
    loop.run_forever()

if __name__ == "__main__":
    start_server()

