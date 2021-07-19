from wifiInformation import WifiInformation
from wifiController import WifiController

if __name__ == '__main__':

    wifiController = WifiController()

    wifiController.init_interfaces()
    wifiController.print_interfaces()

    wifiController.select_set_interface()
    wifiController.scan_for_aps_and_store_ssid()
    wifiController.print_all_ap_ssid()
    wifiController.select_set_ap()
    wifiController.set_key_management_mode()
    wifiController.print_key_management_mode()
    
    """
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
    print("Wifi cipher type: " + wifiInfo.get_cipher_type_of_ssid(ap_ssid))"""
