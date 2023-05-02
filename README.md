# Tello SDK Python implementation by Francesco Antoni

This an experimental version, still to be tested.

## Connection to the drone

In order to properly communicate with the drone, the device in which this library is used obviously has to have a Wi-Fi
card. <br><br> The drone creates a Wi-Fi network to which the device has to connect. The name of the network is
TELLO-XXXXXX, where XXXXXX is the last 6 digits of the drone's MAC address.<br><br> The default IP address of the drone is
`192.168.10.1` and the default port is `8889`. The device has to be connected to the same network as the drone.
The first method to be called after the init of the class is `connect()`, which will establish the connection
with the drone (although no proper connection will be established since the drone accept only one connection at a
time and uses UDP protocol, this is just to open the communication socket).


## Possible commands

Every method in this library corresponds to command given in the SDK documentation.
Here is a list of the possible commands: <br><br>
| Command | Description | Possible Responses |
| ------- |----------- | ------------------ |
| command | entry SDK mode | ok error |