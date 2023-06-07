class Chain:
    def __init__(self, chainID):
        self.chainID = chainID
        self.sequence = []

    def add_group(self, group):
        self.sequence.append(group)
