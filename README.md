# Tello SDK Python implementation by Francesco Antoni
This an experimental version, still to be tested.
## Connection to the drone
In order to properly communicate with the drone, the device in which this library is used obviously has to have a Wi-Fi 
card. The drone creates a Wi-Fi network to which the device has to connect. The name of the network is TELLO-XXXXXX, 
where XXXXXX is the last 6 digits of the drone's MAC address. The default IP address of the drone is `192.168.10.1` and
the default port is `8889`. The device has to be connected to the same network as the drone. The first method to be
after the init of the class is `connect()`, which will establish the connection with the drone (although no proper 
connection will be established since the drone accept only one connection at a time and uses UDP protocol).