# Tello SDK Python implementation by Francesco Antoni

This an experimental version, still to be tested.

## Connection to the drone

In order to properly communicate with the drone, the device in which this library is used obviously has to have a Wi-Fi
card. <br><br> The drone creates a Wi-Fi network to which the device has to connect. The name of the network is
TELLO-XXXXXX, where XXXXXX is the last 6 digits of the drone's MAC address.<br><br> The default IP address of the drone
is
`192.168.10.1` and the default port is `8889`. The device has to be connected to the same network as the drone.
The first method to be called after the init of the class is `connect()`, which will establish the connection
with the drone (although no proper connection will be established since the drone accept only one connection at a
time and uses UDP protocol, this is just to open the communication socket).

## Possible commands

Every method in this library corresponds to command given in the SDK documentation.
Here is a list of the possible commands: <br><br>

### Control commands

| Command        | Python method                                                             | Description                                                                         | Possible Responses |
|----------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------|--------------------|
| command        | `connect()`                                                               | entry SDK mode                                                                      | ok <br> error      |
| takeoff        | `takeoff()`                                                               | Tello auto takeoff                                                                  | ok <br> error      |
| land           | `land()`                                                                  | Tello auto land                                                                     | ok <br> error      |
| emergency      | `emergency()`                                                             | Stop all motors immediately                                                         | ok <br> error      |
| up x           | `up(x: int)`                                                              | Tello fly up (distance in cm range 20-500)                                          | ok <br> error      |
| down x         | `down(x: int)`                                                            | Tello fly down (distance in cm 20-500)                                              | ok <br> error      |
| left x         | `left(x: int)`                                                            | Tello fly left (distance in cm 20-500)                                              | ok <br> error      |
| right x        | `right(x: int)`                                                           | Tello fly right (distance in cm 20-500)                                             | ok <br> error      |
| forward x      | `forward(x: int)`                                                         | Tello fly forward (distance in cm 20-500)                                           | ok <br> error      |
| back x         | `back(x: int)`                                                            | Tello fly back (distance in cm 20-500)                                              | ok <br> error      |
| cw x           | `rotate_clockwise(x: int)`                                                | Tello rotate clockwise (angle in degrees)                                           | ok <br> error      |
| ccw x          | `rotate_counter_clockwise(x: int)`                                        | Tello rotate counter-clockwise                                                      | ok <br> error      |
| flip x         | `flip(x: str)`                                                            | Tello fly flip with x in (l, r, f, b)                                               | ok <br> error      |
| go x y z speed | `set_speed(x: int)`                                                       | Tello fly to x y z (range 20-500) with speed 10-100                                 | ok <br> error      |
| curve x y z    | `curve(x1: int, y1: int, z1: int, x2: int, y2: int, z2: int, speed: int)` | Tello fly a curve defined by the current and two given coordinates with speed 10-60 | ok <br> error      |

### Set commands

| Command    | Python method                            | Description                                                                                                                       | Possible Responses |
|------------|------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------|
| speed x    | `set_speed(x: int)`                      | Set speed to x (range 10-100)                                                                                                     | ok <br> error      |
| rc a b c d | `set_rc(a: int, b: int, c: int, d: int)` | Set remote control command with a: left/right (-100\~100) b: forward/backward (-100\~100) c: up/down (-100~100) d: yaw (-100~100) | ok <br> error      |
| wifi ssid  | `set_wifi(ssid: str, password: str)`     | Set Wi-Fi with SSID (9 chars max)                                                                                                 | ok <br> error      |

### Read commands

| Command       | Python method    | Description               | Possible Responses                  |
|---------------|------------------|---------------------------|-------------------------------------|
| speed?        | `get_speed()`    | Get current speed         | x: current speed <br> error         |
| battery?      | `get_battery()`  | Get current battery       | x: current battery <br> error       |
| time?         | `get_time()`     | Get current fly time      | x: current time <br> error          |
| height?       | `get_height()`   | Get current height        | x: current height <br> error        |
| temp?         | `get_temp()`     | Get current temp          | x: current temp <br> error          |
| attitude?     | `get_attitude()` | Get current attitude      | x: current attitude <br> error      |
| baro?         | `get_baro()`     | Get current barometer     | x: current barometer <br> error     |
| acceleration? | `get_accel()`    | Get current accelerometer | x: current accelerometer <br> error |
| tof?          | `get_tof()`      | Get current distance      | x: current distance <br> error      |
| wifi?         | `get_wifi()`     | Get current Wi-Fi SSID    | x: current Wi-Fi SSID <br> error    |