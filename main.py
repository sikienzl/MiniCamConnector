from wifiInformation import WifiInformation

if __name__ == '__main__':
    wifiInfo = WifiInformation()
    wifiInterfaces = wifiInfo.getInterfaces()

    for interface_count in range(0, len(wifiInterfaces)):
        print(str(interface_count) + ": " + str(wifiInterfaces[interface_count]))
    device = 0
    device_not_selected = True
    while device_not_selected:
        device = int(input("Select one of these devices: "))
        if device < len(wifiInterfaces):
            device_not_selected = False

    print("Scan of AP's starts now:")
    result_ap_list = wifiInfo.getAPs(device)
    for ap_count in range(0, len(result_ap_list)):
        print(str(ap_count) + ": " + result_ap_list[ap_count])

    ap = 0
    ap_not_selected = True

    while ap_not_selected:
        ap = int(input("Select one of these AP's: "))
        if ap < len(result_ap_list):
            ap_not_selected = False

    ap_ssid = result_ap_list[ap]
    print("Wifi encryption: " + wifiInfo.get_key_management_mode_of_ssid(ap_ssid))
