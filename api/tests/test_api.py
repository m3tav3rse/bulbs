import os
import pytest
import requests

DEVICE_IP = os.getenv("DEVICE_IP")

if not DEVICE_IP:
    raise ValueError("DEVICE_IP not set")

BASE_URL = f"http://{DEVICE_IP}"
URL_LED = f"{BASE_URL}/led"
URL_LED_ON = f"{URL_LED}/on"
URL_LED_OFF = f"{URL_LED}/off"
URL_LED_COLOR = f"{URL_LED}/color"
URL_LED_BRIGHTNESS = f"{URL_LED}/brightness"

def test_led_color_get():
    response = requests.get(URL_LED_COLOR)

    assert response.status_code == 200
    assert response.json()["color"]

def test_led_color_put():
    response = requests.put(f"{URL_LED_COLOR}/388e3c")

    assert response.status_code == 200

def test_led_color_put_invalid():
    response = requests.put(f"{URL_LED_COLOR}/M38e3c")

    assert response.status_code == 400
    assert response.json()["message"]

def test_led_color_functionality():
    color = "#388e3c"

    assert requests.put(f"{URL_LED_COLOR}/{color[1:]}").status_code == 200
    response_get = requests.get(URL_LED_COLOR)

    assert response_get.status_code == 200
    assert response_get.json()["color"] == color

def test_led_brightness_get():
    response = requests.get(URL_LED_BRIGHTNESS)

    assert response.status_code == 200
    assert type(response.json()["brightness"]) == float

def test_led_brightness_put():
    response = requests.put(f"{URL_LED_BRIGHTNESS}/0.5")

    assert response.status_code == 200

def test_led_brightness_put_invalid():
    response = requests.put(f"{URL_LED_BRIGHTNESS}/5")

    assert response.status_code == 400
    assert response.json()["message"]

def test_led_brightness_functionality():
    brightness = 0.21

    assert requests.put(f"{URL_LED_BRIGHTNESS}/{brightness}") == 200
    response_get = requests.get(URL_LED_BRIGHTNESS)

    assert response_get.status_code == 200
    assert response_get.json()["brightness"] == brightness

def test_led_status():
    response = requests.get(URL_LED)

    body = response.json()
    code = response.status_code

    assert code == 200
    assert type(body["on"]) == int
    assert type(body["color"]) == str
    assert type(body["brightness"]) == float

def test_led_off():
    assert requests.put(URL_LED_OFF).status_code == 200
    assert requests.get(URL_LED_OFF).json()["off"]

def test_led_on():
    assert requests.put(URL_LED_ON).status_code == 200
    assert requests.get(URL_LED_ON).json()["on"]

