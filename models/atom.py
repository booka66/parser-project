class Atom:
    def __init__(self, record_name, serial, name, altLoc, resName, chainID, resSeq, iCode, x, y, z, occupancy, tempFactor, element, charge):
        self.record_name = record_name
        self.serial = serial
        self.name = name
        self.altLoc = altLoc
        self.resName = resName
        self.chainID = chainID
        self.resSeq = resSeq
        self.iCode = iCode
        self.x = x
        self.y = y
        self.z = z
        self.occupancy = occupancy
        self.tempFactor = tempFactor
        self.element = element
        self.charge = charge

    def to_string(self):
        return str(f'{self.record_name=}\n{self.serial=}\n{self.name=}\n{self.altLoc=}\n{self.resName=}\n{self.chainID=}\n{self.resSeq=}\n{self.iCode=}\n{self.x=}\n{self.y=}\n{self.z=}\n{self.occupancy=}\n{self.tempFactor=}\n{self.element=}\n{self.charge=}')

    def get_ID(self):
        return (self.chainID, self.resSeq)
