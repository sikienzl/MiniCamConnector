import pywifi

import interface
import ap
from converter import Converter
import time


class WifiController:
    NONE = "None"
    AKM_WPA = "WPA"
    AKM_WPAPSK = "WPA PSK"
    AKM_WPA2 = "WPA2"
    AKM_WPA2PSK = "WPA2 PSK"
    AKM_UNKNOWN = "Unknown"

    CIPHER_WEP = "WEP"
    CIPHER_TKIP = "TKIP"
    CIPHER_CCMP = "CCMP"

    wifi = pywifi.PyWiFi()
    accesspoint = ap.AP()
    interface = interface.Interface()

    def __get_key_management_mode_from_value(self, key_management_value):
        key_management_mode = ""
        if key_management_value == 0:
            key_management_mode = self.NONE
        elif key_management_value == 1:
            key_management_mode = self.AKM_WPA
        elif key_management_value == 2:
            key_management_mode = self.AKM_WPAPSK
        elif key_management_value == 3:
            key_management_mode = self.AKM_WPA2
        elif key_management_value == 4:
            key_management_mode = self.AKM_WPA2PSK
        else:
            key_management_mode = self.AKM_UNKNOWN
        return key_management_mode

    def __get_cipher_type_from_value(self, cipher_type_value):
        cipher_type = ""
        if cipher_type_value == 0:
            cipher_type = self.NONE
        elif cipher_type_value == 1:
            cipher_type = self.CIPHER_WEP
        elif cipher_type_value == 2:
            cipher_type = self.CIPHER_TKIP
        elif cipher_type_value == 3:
            cipher_type = self.CIPHER_CCMP
        return cipher_type

    def init_interfaces(self):
        converter = Converter()
        str_interfaces = converter.convertIntoStringArray(self.wifi.interfaces())
        self.interface.set_interfaces(str_interfaces)

    def print_interfaces(self):
        interfaces = self.interface.get_interfaces()
        for interface_count in range(0, len(interfaces)):
            print(str(interface_count) + ": " + str(interfaces[interface_count]))

    def select_set_interface(self):
        device = 0
        device_not_selected = True
        interfaces = self.interface.get_interfaces()
        while device_not_selected:
            device = int(input("Select one of these devices: "))
            if device < len(interfaces):
                self.interface.set_interface_number(device)
                device_not_selected = False

    def print_selected_interface_value(self):
        interfaces = self.interface.get_interfaces()
        print(interfaces.get_interface_number())

    def scan_for_aps_and_store_ssid(self):
        interface_number = self.interface.get_interface_number()
        iface = self.wifi.interfaces()[interface_number]
        iface.scan()
        time.sleep(5)
        ap_results = iface.scan_results()

        self.accesspoint.set_aps(ap_results)
        aps_result_list = {}

        for ap_results_number in range(0, len(ap_results)):
            aps_result_list[ap_results_number] = ap_results[ap_results_number].ssid

        self.accesspoint.set_aps_ssid(aps_result_list)

    def print_all_ap_ssid(self):
        aps_ssid = self.accesspoint.get_aps_ssid()
        print("All AP's:")
        for ap_count in range(0, len(aps_ssid)):
            print(str(ap_count) + ": " + aps_ssid[ap_count])

    def select_set_ap(self):
        ap_number = 0
        ap_not_selected = True

        while ap_not_selected:
            ap_number = int(input("Select one of these AP's: "))

            if ap_number < len(self.accesspoint.get_aps_ssid()):
                self.accesspoint.set_ap_number(ap_number)
                ap_not_selected = False

    def set_key_management_mode(self):
        ap_results = self.accesspoint.get_aps()
        key_management_mode = ""
        akm_value = ap_results[self.accesspoint.get_ap_number()].akm[0]
        key_management_mode = self.__get_key_management_mode_from_value(akm_value)
        self.accesspoint.set_key_management_mode(key_management_mode)

    def print_key_management_mode(self):
        print("Key management mode: " + self.accesspoint.get_key_management_mode())
