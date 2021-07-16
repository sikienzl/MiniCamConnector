import wifiInformation


if __name__ == '__main__':
    wifiInformation.getInterfacesArray()
    result_ap_list = wifiInformation.getAPs(0)
    for ap_count in range(0, len(result_ap_list)):
        print(str(ap_count) + ": " + result_ap_list[ap_count])

