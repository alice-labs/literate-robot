# Plane & Carrier classes
class Plane:
    def __init__(self, carrier):
        self.carrier: Carrier = carrier

    def carry(self, items):
        pass


class MilitaryPlane(Plane):
    def __init__(self, carrier):
        super().__init__(carrier("military"))

    def carry(self, items):
        print("This is a military plane.")
        self.carrier.carry_military(items)


class CommercialPlane(Plane):
    def carry(self, items):
        print("This is a commercial plane.")
        self.carrier.carry_commercial(items)


class Carrier:
    def carry_military(self, items):
        pass

    def carry_commercial(self, items):
        pass


class Cargo(Carrier):
    def carry_military(self, items):
        print(f"The plane carries {items} military cargo goods.")

    def carry_commercial(self, items):
        print(f"The plane carries {items} commercial cargo goods.")


class Passenger(Carrier):
    def carry_military(self, items):
        print(f"The plane carries {items} military passengers.")

    def carry_commercial(self, items):
        print(f"The plane carries {items} commercial passengers.")


# Creating different combinations of Plane and Carrier
plane1 = MilitaryPlane(Cargo)
plane1.carry(100)

plane2 = CommercialPlane(Passenger)
plane2.carry(200)

plane3 = MilitaryPlane(Passenger)
plane3.carry(50)

plane4 = CommercialPlane(Cargo)
plane4.carry(150)
