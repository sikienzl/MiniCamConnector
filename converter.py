class Converter:

    def convertIntoStringArray(self, wifi):
        interfaceStrArray = {}
        for wifiInterfaceNumber in range(0, len(wifi)):
            interfaceStrArray[wifiInterfaceNumber] = wifi[wifiInterfaceNumber].name()
        return interfaceStrArray