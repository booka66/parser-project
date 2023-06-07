from models.atom import *
from models.amino_acid import *
from models.atom_group import *
from models.chain import *
from models.group import *


def parse_atoms(line, groups):
    data = {
        "record_name": line[0:6].strip(),
        "serial": int(line[6:11].strip()),
        "name": line[12:16].strip(),
        "altLoc": line[16].strip(),
        "resName": line[17:20].strip(),
        "chainID": line[21].strip(),
        "resSeq": int(line[22:26].strip()),
        "iCode": line[26].strip(),
        "x": float(line[30:38].strip()),
        "y": float(line[38:46].strip()),
        "z": float(line[46:54].strip()),
        "occupancy": float(line[54:60].strip()),
        "tempFactor": float(line[60:66].strip()),
        "element": line[76:78].strip(),
        "charge":  line[78:80].strip()
    }
    groups.append(Atom(**data))


def parse_group(chainID, resSeq, current_atom, group):
    is_complete = False
    prev_ID = None
    if resSeq == None:
        chainID, resSeq = current_atom.get_ID()
        if current_atom.record_name == "ATOM":
            group.amino_acids[(chainID, resSeq)] = AminoAcid(
                current_atom.resName, current_atom.chainID)
            group.amino_acids[(chainID, resSeq)].add_atom(current_atom)
        else:
            group.atom_groups[(chainID, resSeq)] = AtomGroup(
                current_atom.resName, current_atom.chainID)
            group.atom_groups[(chainID, resSeq)].add_atom(current_atom)
    elif resSeq == current_atom.resSeq:
        if current_atom.record_name == "ATOM":
            group.amino_acids[(chainID, resSeq)].add_atom(current_atom)
        else:
            group.atom_groups[(chainID, resSeq)].add_atom(current_atom)
    elif resSeq != current_atom.resSeq:
        is_complete = True
        prev_ID = (chainID, resSeq)
        chainID, resSeq = current_atom.get_ID()
        if current_atom.record_name == "ATOM":
            group.amino_acids[(chainID, resSeq)] = AminoAcid(
                current_atom.resName, current_atom.chainID)
            group.amino_acids[(chainID, resSeq)].add_atom(current_atom)
        else:
            group.atom_groups[(chainID, resSeq)] = AtomGroup(
                current_atom.resName, current_atom.chainID)
            group.atom_groups[(chainID, resSeq)].add_atom(current_atom)
    return chainID, resSeq, is_complete, prev_ID


def parse_chains(current_group, chains):
    chainID = current_group.formula[0].chainID
    if chainID not in chains:
        chains[chainID] = Chain(chainID)
        chains[chainID].add_group(current_group)
    else:
        chains[chainID].add_group(current_group)


def is_atom_header(header):
    return True if header == "ATOM" else False


def is_hetatm_header(header):
    return True if header == "HETATM" else False


def run(file_name):
    atoms = []
    group = Group()
    chains = {}
    chainID, resSeq = None, None
    prev_record = None
    with open(file_name, 'r',) as file:
        for line in file:
            if is_atom_header(line[0:6].strip()) or is_hetatm_header(line[0:6].strip()):
                parse_atoms(line, atoms)
                current_atom = atoms[-1]
                chainID, resSeq, is_complete, prev_ID = parse_group(
                    chainID, resSeq, current_atom, group)

                if is_complete:
                    if prev_record == "ATOM":
                        current_group = group.amino_acids[prev_ID]
                    else:
                        current_group = group.atom_groups[prev_ID]
                    parse_chains(current_group, chains)

                prev_record = current_atom.record_name
    return atoms, group, chains
