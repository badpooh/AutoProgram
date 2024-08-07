from http import client
from os import error
from urllib import response
from pymodbus.client import ModbusTcpClient as ModbusClient


class SetupTesting:
    
    SERVER_IP = '10.10.26.159'  # 장치 IP 주소
    SERVER_PORT = 5100  #A7300

    def tcp_connect(self):
        self.client = ModbusClient(self.SERVER_IP, port=self.SERVER_PORT)
        connection = self.client.connect()
        if connection:
            print("Success")
        else:
            print("Fail")
            
    def tcp_disconnect(self):
        self.client = ModbusClient(self.SERVER_IP, port=self.SERVER_PORT)
        if self.client:
            self.client.close()
            print("Disconnect")
        else:
            error()




test = SetupTesting()
test.tcp_connect()
test.setup_all_test()
test.tcp_disconnect()