from wifiInformation import WifiInformation


if __name__ == '__main__':
    wifiInfo = WifiInformation()
    wifiInterfaces = wifiInfo.getInterfaces()
    for interface_count in range(0, len(wifiInterfaces)):
        print(str(wifiInterfaces[interface_count]))
    result_ap_list = wifiInfo.getAPs(0)
    for ap_count in range(0, len(result_ap_list)):
        print(str(ap_count) + ": " + result_ap_list[ap_count])

