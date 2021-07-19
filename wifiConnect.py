import pywifi


class WifiConnect:
    def connect(self, ssid, password):
        profile = pywifi.profile()
