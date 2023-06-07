class AminoAcid:
    def __init__(self, name, associated_chainID):
        self.name = name
        self.associated_chainID = associated_chainID
        self.formula = []

    def add_atom(self, atom):
        self.formula.append(atom)
