from abc import ABC, abstractmethod

"""
    All our devices are charged via USB-C (charge method).
    Apple chargers can only charge Iphone's (charge_iphone method).
    How do you charge other devices if you only have a Apple charger?
    Solution: A Dongle...
"""


class USBC(ABC):
    @abstractmethod
    def charge(self):
        """Charge"""


class Lightning(ABC):
    @abstractmethod
    def charge_iphone(self):
        """Charge Iphone"""


class UniversalCharger(USBC):
    def __init__(self, wattage: str):
        self.wattage = wattage

    def charge(self):
        print(f"Charging at {self.wattage}!")


class AppleCharger(Lightning):
    def __init__(self, wattage: str):
        self.wattage = wattage

    def charge_iphone(self):
        print(f"Charging at {self.wattage}!")


class AppleDongle(USBC):
    def __init__(self, charger: AppleCharger):
        self.charger = charger

    def charge(self):
        self.charger.charge_iphone()


universal_charger = UniversalCharger(wattage="60W")
apple_charger = AppleCharger(wattage="15W")
apple_dongle = AppleDongle(charger=apple_charger)

# OK
universal_charger.charge()
# Can't use a universal charge method.
# apple_charger.charge()
# Apple charger can only charge Iphone's!
apple_charger.charge_iphone()
# Solution: Use a USB-C Dongle!
apple_dongle.charge()
