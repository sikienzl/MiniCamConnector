class AP:
    aps = {}

    def set_aps(self, aps):
        self.aps = aps

    def get_aps(self):
        return self.aps

    aps_ssid = {}

    def set_aps_ssid(self, aps_ssid):
        self.aps_ssid = aps_ssid

    def get_aps_ssid(self):
        return self.aps_ssid

    apNumber = 0

    def set_ap_number(self, apNumber):
        self.apNumber = apNumber

    def get_ap_number(self):
        return self.apNumber

    key_management_mode = ""

    def set_key_management_mode(self, key_management_mode):
        self.key_management_mode = key_management_mode

    def get_key_management_mode(self):
        return self.key_management_mode
