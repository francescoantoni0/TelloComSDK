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

