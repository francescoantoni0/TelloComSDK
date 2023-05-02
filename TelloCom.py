import socket


class TelloCom:
    def __init__(self):
        self.s = None
        self.__ip_address = '192.168.10.1'
        self.__port = 8889
        self.__address_tuple = (self.__ip_address, self.__port)

    def connect(self) -> str:
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind(self.__address_tuple)
        init_command = 'command'.encode('utf-8')
        self.s.sendto(init_command, self.__address_tuple)
        message, address = self.s.recvfrom(4096)
        if address == self.__ip_address:
            return message.decode('utf-8')
        else:
            raise ConnectionError('Error with the IP address')

    def takeoff(self) -> str:
        command = 'takeoff'.encode('utf-8')
        self.s.sendto(command, self.__address_tuple)
        response, add = self.s.recvfrom(4096)
        return f'From {add.decode("utf-8")}: {response.decode("utf-8")}'

    def land(self) -> str:
        command = 'land'.encode('utf-8')
        self.s.sendto(command, self.__address_tuple)
        response, add = self.s.recvfrom(4096)
        return f'From {add.decode("utf-8")}: {response.decode("utf-8")}'

    def emergency(self) -> str:
        command = 'emergency'.encode('utf-8')
        self.s.sendto(command, self.__address_tuple)
        response, add = self.s.recvfrom(4096)
        return f'From {add.decode("utf-8")}: {response.decode("utf-8")}'

    def up(self, x: int) -> str:
        if x not in range(20, 501):
            raise AttributeError('x not in range(20, 500)')
        command = f'up {x}'.encode('utf-8')
        self.s.sendto(command, self.__address_tuple)
        response, add = self.s.recvfrom(4096)
        return f'From {add.decode("utf-8")}: {response.decode("utf-8")}'

    def down(self, x: int) -> str:
        if x not in range(20, 501):
            raise AttributeError('x not in range(20, 500)')
        command = f'down {x}'.encode('utf-8')
        self.s.sendto(command, self.__address_tuple)
        response, add = self.s.recvfrom(4096)
        return f'From {add.decode("utf-8")}: {response.decode("utf-8")}'

    def left(self, x: int) -> str:
        if x not in range(20, 501):
            raise AttributeError('x not in range(20, 500)')
        command = f'left {x}'.encode('utf-8')
        self.s.sendto(command, self.__address_tuple)
        response, add = self.s.recvfrom(4096)
        return f'From {add.decode("utf-8")}: {response.decode("utf-8")}'

    def right(self, x: int) -> str:
        if x not in range(20, 501):
            raise AttributeError('x not in range(20, 500)')
        command = f'right {x}'.encode('utf-8')
        self.s.sendto(command, self.__address_tuple)
        response, add = self.s.recvfrom(4096)
        return f'From {add.decode("utf-8")}: {response.decode("utf-8")}'

    def forward(self, x: int) -> str:
        if x not in range(20, 501):
            raise AttributeError('x not in range(20, 500)')
        command = f'forward {x}'.encode('utf-8')
        self.s.sendto(command, self.__address_tuple)
        response, add = self.s.recvfrom(4096)
        return f'From {add.decode("utf-8")}: {response.decode("utf-8")}'

    def back(self, x: int) -> str:
        if x not in range(20, 501):
            raise AttributeError('x not in range(20, 500)')
        command = f'back {x}'.encode('utf-8')
        self.s.sendto(command, self.__address_tuple)
        response, add = self.s.recvfrom(4096)
        return f'From {add.decode("utf-8")}: {response.decode("utf-8")}'

    def rotate_clockwise(self, x: int) -> str:
        if x not in range(1, 3600):
            raise AttributeError('x not in range(1, 3600)')
        command = f'cw {x}'.encode('utf-8')
        self.s.sendto(command, self.__address_tuple)
        response, add = self.s.recvfrom(4096)
        return f'From {add.decode("utf-8")}: {response.decode("utf-8")}'

    def rotate_counter_clockwise(self, x: int) -> str:
        if x not in range(20, 501):
            raise AttributeError('x not in range(20, 500)')
        command = f'ccw {x}'.encode('utf-8')
        self.s.sendto(command, self.__address_tuple)
        response, add = self.s.recvfrom(4096)
        return f'From {add.decode("utf-8")}: {response.decode("utf-8")}'

    def flip(self, x: int, side: str) -> str:
        if x not in range(20, 501):
            raise AttributeError('x not in range(20, 500)')
        if side not in ['l', 'r', 'f', 'b']:
            raise AttributeError('side can only be l (left), r (right), f (forward), b (backward)')
        command = f'flip {x} {side}'.encode('utf-8')
        self.s.sendto(command, self.__address_tuple)
        response, add = self.s.recvfrom(4096)
        return f'From {add.decode("utf-8")}: {response.decode("utf-8")}'

    def go(self, x: int, y: int, z: int, speed: int) -> str:
        if (x, y, z) not in range(20, 501):
            raise AttributeError('coordinates not in range(20, 500)')
        if speed not in range(10, 101):
            raise AttributeError('speed not in range(10, 101)')
        command = f'go {x} {y} {z} {speed}'.encode('utf-8')
        self.s.sendto(command, self.__address_tuple)
        response, add = self.s.recvfrom(4096)
        return f'From {add.decode("utf-8")}: {response.decode("utf-8")}'

    def curve(self, x1: int, y1: int, z1: int, x2: int, y2: int, z2: int, speed: int):
        if (x1, y1, z1, x2, y2, z2) not in range(20, 501):
            raise AttributeError('coordinates not in range(20, 500)')
        if speed not in range(10, 101):
            raise AttributeError('speed not in range(10, 101)')
        command = f'curve {x1} {y1} {z1} {x2} {y2} {z2} {speed}'.encode('utf-8')
        self.s.sendto(command, self.__address_tuple)
        response, add = self.s.recvfrom(4096)
        return f'From {add.decode("utf-8")}: {response.decode("utf-8")}'

    def set_wifi(self, ssid: str, password: str) -> str:
        command = f'wifi {ssid} {password}'.encode('utf-8')
        self.s.sendto(command, self.__address_tuple)
        response, add = self.s.recvfrom(4096)
        return f'From {add.decode("utf-8")}: {response.decode("utf-8")}'

    def set_rc(self, a, b, c, d) -> str:
        if (a, b, c, d) not in range(-100, 100):
            raise AttributeError('coordinates not in range(-100, 100)')
        command = f'rc {a} {b} {c} {d}'.encode('utf-8')
        self.s.sendto(command, self.__address_tuple)
        response, add = self.s.recvfrom(4096)
        return f'From {add.decode("utf-8")}: {response.decode("utf-8")}'

    def get_speed(self) -> str:
        command = 'speed?'.encode('utf-8')
        self.s.sendto(command, self.__address_tuple)
        response, add = self.s.recvfrom(4096)
        return f'From {add.decode("utf-8")}: {response.decode("utf-8")}'

    def get_battery(self) -> str:
        command = 'battery?'.encode('utf-8')
        self.s.sendto(command, self.__address_tuple)
        response, add = self.s.recvfrom(4096)
        return f'From {add.decode("utf-8")}: {response.decode("utf-8")}'

    def get_time(self) -> str:
        command = 'time?'.encode('utf-8')
        self.s.sendto(command, self.__address_tuple)
        response, add = self.s.recvfrom(4096)
        return f'From {add.decode("utf-8")}: {response.decode("utf-8")}'

    def get_height(self) -> str:
        command = 'height?'.encode('utf-8')
        self.s.sendto(command, self.__address_tuple)
        response, add = self.s.recvfrom(4096)
        return f'From {add.decode("utf-8")}: {response.decode("utf-8")}'

    def get_temp(self) -> str:
        command = 'temp?'.encode('utf-8')
        self.s.sendto(command, self.__address_tuple)
        response, add = self.s.recvfrom(4096)
        return f'From {add.decode("utf-8")}: {response.decode("utf-8")}'

    def get_attitude(self) -> str:
        command = 'altitude?'.encode('utf-8')
        self.s.sendto(command, self.__address_tuple)
        response, add = self.s.recvfrom(4096)
        return f'From {add.decode("utf-8")}: {response.decode("utf-8")}'

    def get_baro(self) -> str:
        command = 'baro?'.encode('utf-8')
        self.s.sendto(command, self.__address_tuple)
        response, add = self.s.recvfrom(4096)
        return f'From {add.decode("utf-8")}: {response.decode("utf-8")}'

    def get_acceleration(self) -> str:
        command = 'acceleration?'.encode('utf-8')
        self.s.sendto(command, self.__address_tuple)
        response, add = self.s.recvfrom(4096)
        return f'From {add.decode("utf-8")}: {response.decode("utf-8")}'

    def get_tof(self) -> str:
        command = 'tof?'.encode('utf-8')
        self.s.sendto(command, self.__address_tuple)
        response, add = self.s.recvfrom(4096)
        return f'From {add.decode("utf-8")}: {response.decode("utf-8")}'

    def get_wifi(self) -> str:
        command = 'wifi?'.encode('utf-8')
        self.s.sendto(command, self.__address_tuple)
        response, add = self.s.recvfrom(4096)
        return f'From {add.decode("utf-8")}: {response.decode("utf-8")}'
