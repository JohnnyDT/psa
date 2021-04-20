from scapy.all import *
import struct
from ctypes import *

def macDoBajtov(paMAC):
    return bytes.fromhex(paMAC.replace(":", ""))

class EthRamec():
    def __init__(self, paSrcMAC):      #metoda instancie
        self.aDstMAC = "01:00:0c:cc:cc:c"      # multicast
        self.aSrcMAC = paSrcMAC

    def pridajPayload(self, paPayload):
        self.aPayload = paPayload

    def dajBajty(self):
        payloadBajty = self.aPayload.dajBajty()
        return macDoBajtov(self.aDstMAC) + macDoBajtov(self.aSrcMAC) + struct.pack("!H", len(payloadBajty)) + payloadBajty

class LLCSnap():
    def __init__(self):
        self.aDSAP = 0xaa
        self.aSSAP = 0xaa
        self.aControl = 0x03
        self.aOUI = "00:00:0c"
        self.aProtocolID = 0x2000

    def pridajPayload(self, paPayload):
        self.aPayload = paPayload

    def dajBajty(self):
        return struct.pack("!3B", self.aDSAP, self.aSSAP, self.aControl) + macDoBajtov(self.aOUI) + struct.pack("!H", self.aProtocolID) + self.aPayload.dajBajty

class CDP():
    def __init__(self):
        self.aVersion = 1
        self.aTTL = 180
        self.aTLVs = list()

    def pridajTLV(self, paTLV):
        self.aTLVs.append(paTLV)

    def dajBajty(self):
        #! TO-DO checksum
        checksum = 0
        bajty = struct.pack("!2BH", self.aVersion, self.aTTL, checksum)
        for tlv in self.aTLVs:
            bajty += tlv.dajBajty()
        return bajty

class TLV():
    def __init__(self, paType):
        self.aType = paType
        self.aLength = 4

    def dajBajty(self):
        return struct.pack("!2H", self.aType, self.aLength)

class TLVDeviceID(TLV):
    def __init__(self, paDeviceID):
        TLV.__init__(self, 0x0001)
        self.aValue = paDeviceID

    def dajBajty(self):
        valueBajty = self.aValue.encode()
        self.aLength += len(valueBajty)
        return TLV.dajBajty(self) + valueBajty

class TLVsoftware(TLVDeviceID):
    def __init__(self, paVersion):
        super().__init__(paVersion)
        self.aType = 0x0005

class TLVplatform(TLVDeviceID):
    def __init__(self, paVersion):
        super().__init__(paVersion)
        #self.aType = 0x0005

# TLVs ---> deviceID, software, platform, capabilities

ramec = EthRamec("01:02:03:04:05:06")    # instancia triedz

llc = LLCSnap()
ramec.pridajPayload(llc)

cdp = CDP()
llc.pridajPayload(CDP)

tlvDevice = TLVDeviceID("MojHP")
cdp.pridajTLV(tlvDevice)
cdp.pridajTLV(TLVsoftware("Windows 10 Pro"))

#? ziskanie informacii o
#IFACES.show()

#? Vybratie rozhrania
#iface = "Broadcom BCM43142 802.11 bgn Wi-Fi M.2 Adapter"
iface = IFACES.dev_from_index(10)

#? Vyvorenie socketu
sock = conf.L2socket(iface)

#? Poslanie dat
sock.send(ramec.dajBajty())