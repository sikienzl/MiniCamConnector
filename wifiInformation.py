import pywifi
import time
from converter import Converter

class WifiInformation:
    def getInterfaces(self):
        wifi = pywifi.PyWiFi()
        converter = Converter()
        strInterfaces = converter.convertIntoStringArry(wifi.interfaces())
        return strInterfaces

    def getAPs(self, wifiInterfacNumber):
        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[wifiInterfacNumber]
        iface.scan()
        time.sleep(5)
        ap_results= iface.scan_results()
        aps_result_list = {}

        for ap_results_number in range(0, len(ap_results)):
            aps_result_list[ap_results_number] = ap_results[ap_results_number].ssid

        return aps_result_list