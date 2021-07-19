

class WifiInformation:

    def get_cipher_type_of_ssid(self, ssid):
        ap_results = self.__get_ap_results()
        cipher_type = ""
        for ap_results_number in range(0, len(ap_results)):
            if ap_results[ap_results_number].ssid == ssid:
                print(str(ap_results_number) + ":" + str(ap_results[ap_results_number].cipher))
                cipher_type = self.__get_cipher_type_from_value(ap_results[ap_results_number].cipher)
        return cipher_type




