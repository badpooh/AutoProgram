from os import error
import threading
import time
import cv2
import numpy as np
import os, glob
from datetime import datetime

from config_setup import ConfigSetup
        
class TouchManager:

    config_data = ConfigSetup()
    measurement = config_data.color_detection_data

    def color_detection(image, x, y, w, h, R, G, B):
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            selected_area = image_rgb[y:y+h, x:x+w]
            average_color = np.mean(selected_area, axis=(0, 1))
            target_color = np.array([R, G, B])
            color_difference = np.linalg.norm(average_color - target_color)
            return color_difference
    
    def measurement_touch(self):
        # self.color_detection(image, *self.measurement)



        pass

    def event_touch(self):
        pass

    def network_touch(self):
        pass
    
    def control_touch(self):
        pass
        
    def system_touch(self):
        pass
    

    
    
# class SetupTesting:
    
#     SERVER_IP = '10.10.26.159'  # 장치 IP 주소
#     TOUCH_PORT = 5100  #A7300 - 터치용
#     SETUP_PORT = 502  #A7300 - 설정용

#     image_path = r"\\10.10.20.30\screenshot"

#     search_pattern = os.path.join(image_path, './**/*10.10.26.159*.png')
#     now = datetime.now()
#     file_time_diff = {}

#     def __init__(self):
#         self.A7300client = ModbusClient(self.SERVER_IP, port=self.SERVER_PORT1)
#         self.connection = self.A7300client.connect()
#         self.A7300client.write_register(2900, 2300)
#         self.A7300client.write_register(2900, 0)
#         self.A7300client.write_register(2900, 700)
#         self.A7300client.write_register(2900, 1)
#         self.A7300client.read_holding_registers(2900, 1)
#         self.A7300client.write_register(2901, 2300)
#         self.A7300client.write_register(2901, 0)
#         self.A7300client.write_register(2901, 1600)
#         self.A7300client.write_register(2901, 1)
#         self.A7300client.read_holding_registers(2901, 1)

#     def setup_all_test(self):
#         if self.connection:
#             print("Success")
#         else:
#             print("Fail")
#         self.address = 57100
#         self.value = 1

#         hex_string = "A5A5"
#         self.bytes_data = bytes.fromhex(hex_string)

#         self.address1 = 57101
#         if self.A7300client:
#             # self.response = self.client.write_register(self.address, self.value)
#             # time.sleep(1)
#             hex_value = int(hex_string, 16)
#             self.response = self.A7300client.write_register(self.address1, hex_value)
#             print(self.response)
#             print("good")
#         else:
#             print(self.response.isError())

#     def moving_cursor(self):
#         for _ in range(2):
#             if self.A7300client:
#                 self.address = 57110
#                 self.value = 100
#                 self.response = self.A7300client.write_register(self.address, self.value)
#                 time.sleep(1)
#                 self.address1 = 57111
#                 self.value1 = 130
#                 self.response1 = self.A7300client.write_register(self.address1, self.value1)
#                 time.sleep(1)
#                 self.address2 = 57112
#                 self.value2 = 1
#                 self.value3 = 0
#                 self.response2 = self.A7300client.write_register(self.address2, self.value2)
#                 time.sleep(1)
#                 self.response3 = self.A7300client.write_register(self.address2, self.value3)
#                 #65, 180
#             else:
#                 print(self.response3.isError())

#     def change_wiring(self):
#             if self.A7300client:
                
#                 # print(self.readRes)
#                 # self.address1 = 2901
#                 # self.value4 = 2300
#                 # self.value5 = 1
#                 # self.value6 = 1600
#                 # self.value7 = 1
#                 # self.response4 = self.A7300client.write_register(self.address1, self.value4)
#                 # self.response5 = self.A7300client.write_register(self.address1, self.value5)
#                 # self.response6 = self.A7300client.write_register(self.address1, self.value6)
#                 # self.response7 = self.A7300client.write_register(self.address1, self.value7)
#                 time.sleep(1)
#                 self.response8 = self.A7300client.write_register(6001, 1)
#                 time.sleep(1)
#                 self.response9 = self.A7300client.write_register(6000, 1)
#                 time.sleep(1)
#                 self.response10 = self.A7300client.read_holding_registers(6000, 1)
                
#             else:
#                 print(self.response10.isError())


#     def load_image_file(self):
#         for file_path in glob.glob(self.search_pattern, recursive=True):
#             creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
#             time_diff = abs((self.now - creation_time).total_seconds())
#             self.file_time_diff[file_path] = time_diff

#         closest_file = min(self.file_time_diff, key=self.file_time_diff.get, default=None)
#         normalized_path = os.path.normpath(closest_file)

#         print("가장 가까운 시간에 생성된 파일:", normalized_path)

#         return normalized_path




# test123 = SetupTesting()
# # ocr = Ocrsetting()
# # test123.moving_cursor()
# # time.sleep(2)
# # test123.setup_all_test()
# # path123 = test123.load_image_file()
# # ocr.meas_vol_test(path123)

# # test123.tcp_disconnect()
# test123.change_wiring()
# test123.tcp_disconnect()

