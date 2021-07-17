import pywifi
import time
from converter import Converter

class WifiInformation:
    NONE = "None"
    WPA = "WPA"
    WPAPSK = "WPA PSK"
    WPA2 = "WPA2"
    WPA2PSK = "WPA2 PSK"
    UNKNOWN = "Unknown"

    def getInterfaces(self):
        wifi = pywifi.PyWiFi()
        converter = Converter()
        strInterfaces = converter.convertIntoStringArry(wifi.interfaces())
        return strInterfaces

    """def __init__(self, ap_results):
        self.__ap_results = ap_results"""

    def __get_ap_results(self):
        return  self.__ap_results

    def __set_ap_results(self, ap_results):
        self.__ap_results = ap_results

    def getAPs(self, wifiInterfacNumber):
        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[wifiInterfacNumber]
        iface.scan()
        time.sleep(5)
        ap_results = iface.scan_results()
        self.__set_ap_results(ap_results)
        aps_result_list = {}

        for ap_results_number in range(0, len(ap_results)):
            aps_result_list[ap_results_number] = ap_results[ap_results_number].ssid

        return aps_result_list

    def get_key_management_mode_of_ssid(self, ssid):
        ap_results = self.__get_ap_results()
        key_management_mode = ""
        for ap_results_number in range(0, len(ap_results)):
            if ap_results[ap_results_number].ssid == ssid:
                for key_management_value in ap_results[ap_results_number].akm:
                    key_management_mode = self.__get_key_management_mode_from_value(key_management_value)
        return key_management_mode

    def __get_key_management_mode_from_value(self, key_management_value):
        key_management_mode = ""
        if key_management_value == 0:
            key_management_mode = self.NONE
        elif key_management_value == 1:
            key_management_mode = self.WPA
        elif key_management_value == 2:
            key_management_mode = self.WPAPSK
        elif key_management_value == 3:
            key_management_mode = self.WPA2
        elif key_management_value == 4:
            key_management_mode = self.WPA2PSK
        else:
            key_management_mode = self.UNKNOWN
        return key_management_mode


