## Board setup

Flash micropython on your ESP8266 board using this [tutorial](https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html).

## Environment setup

Make sure you have `make`, `python` and `pip` installed. Then run:

```
make
```

## Install

Connect the board via USB and run:

```
make install
```

Reboot the board.

> **Note:** By default serial port is set to `/dev/ttyUSB0` for most linux machines.

## First run

Connect the board via USB.

Create `wlan.txt` file in `dat/` directory and run:

```
make flash-data && make run-boot
```

On success connection the board will return own `IP`.

<!-- Connect to the board's access point and run: -->

<!-- ``` -->
<!-- make connect -->
<!-- ``` -->

<!-- On success connection the board will return own `IP`. -->

<!-- > **Note:** You can use [API](#network) instead. -->

## Test

Make sure the board is connected to the same network as you. Then run:

```
DEVICE_IP=<board-ip> make test
```

## API usage

| Method  | Endpoint                                               | Usage               | Returns                          |
| ------- | ------------------------------------------------------ | ------------------- | -------------------------------- |
| **GET** | [`/led/color`](#get-led-color)                         | Get LED color       | [color](#color-object)           |
| **PUT** | [`/led/color/{value}`](#put-led-color-value)           | Set LED color       |                                  |
| **GET** | [`/led/brightness`](#get-led-brightness)               | Get LED brightness  | [brightness](#brightness-object) |
| **PUT** | [`/led/brightness/{value}`](#put-led-brightness-value) | Set LED brightness  |                                  |

---

### **GET** `/led/color`

**Request**

No parameters needed.

**Response**

On success, `200 OK` and [`color`](#color-object) object.

**Example**

Request

```sh
curl http://$DEVICE_IP/led/color
```

Response `200 OK`

```json
{
	"color": "#000000"
}
```

### **PUT** `/led/color/{value}`

**Request**

`Value` as hex color without leading `#`.

**Response**

On success, `200 OK`.

On invalid input, `400 Bad Request` with [message](#message-object) object.

**Example**

Request

```sh
curl -X PUT http://$DEVICE_IP/led/color/5a1010
```

Response `200 OK`

### **GET** `/led/brightness`

**Request**

No parameters needed.

**Response**

On success, `200 OK` and [`brightness`](#brightness-object) object.

**Example**

Request

```sh
curl http://$DEVICE_IP/led/brightness
```

Response `200 OK`

```json
{
	"brightness": 1.0
}
```

### **PUT** `/led/brightness/{value}`

**Request**

`Value` as number from `0` to `1`.

**Response**

On success, `200 OK`.

On invalid input, `400 Bad Request` with [message](#message-object) object.

**Example**

Request

```sh
curl -X PUT http://$DEVICE_IP/led/brightness/0.5
```

Response `200 OK`

---

### Color object

| Key       | Value type | Value description |
| --------- | ---------- | ----------------- |
| color     | string     | Hex color         |

### Brightness object

| Key        | Value type | Value description  |
| ---------- | ---------- | ------------------ |
| brightness | float      | Number from 0 to 1 |

### Message object

| Key       | Value type | Value description      |
| --------- | ---------- | ---------------------- |
| message   | string     | Activities description |

