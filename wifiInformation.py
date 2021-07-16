import pywifi
import time

def getInterfacesArray():
    wifi = pywifi.PyWiFi()
    strInterfacesArray = convertIntoStringArry(wifi.interfaces())
    print("0: " + strInterfacesArray[0])

def convertIntoStringArry(wifi):
    interfaceStrArray = {}
    for wifiInterfaceNumber in range(0, len(wifi)):
        interfaceStrArray[wifiInterfaceNumber] = wifi[wifiInterfaceNumber].name()
    return interfaceStrArray

def getAPs(wifiInterfacNumber):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[wifiInterfacNumber]
    iface.scan()
    time.sleep(5)
    ap_results= iface.scan_results()

    """print("hier " + ap_results[2].ssid)"""

    aps_result_list = {}

    for ap_results_number in range(0, len(ap_results)):
        aps_result_list[ap_results_number] = ap_results[ap_results_number].ssid
        #print(str(ap_results_number) + ": " + ap_results[ap_results_number].ssid)

    return aps_result_list