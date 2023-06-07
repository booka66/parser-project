import parser
from models.group import *


def choose_file():
    file_name = None
    while file_name == None:
        selection = input(
            "Select a file:\n1a3n   [1]\n1buy   [2]\n1x8y   [3]\n5u59   [4]\n")
        if selection == "1":
            file_name = "1a3n"
            break
        elif selection == "2":
            file_name = "1buy"
            break
        elif selection == "3":
            file_name = "1x8y"
            break
        elif selection == "4":
            file_name = "5u59"
            break
        else:
            print("Invalid selection.\n")
    return "data/" + file_name + ".pdb"


def view_chain(chains):
    chainID = None
    while chainID == None:
        chainID = input("Enter a chainID to view: ")
        if chainID in chains:
            print(f"Chain {chainID}:")
            for group in chains[chainID].sequence:
                print(f"{group.name}: ", end="")
                for atom in group.formula:
                    print(f"{atom.name} ", end="")
                print()
        else:
            print("Invalid chainID.")
            chainID = None


def main():
    atoms, group, chains = parser.run(choose_file())
    print("\nAmino Acids:")
    for i in group.amino_acids:
        print(
            f"{group.amino_acids[i].name}: {group.amino_acids[i].associated_chainID}")
    print("\nAtom Groups:")
    for i in group.atom_groups:
        print(
            f"{group.atom_groups[i].name}: {group.atom_groups[i].associated_chainID}")
    print("\nChains:")
    for chain in chains:
        print(f"{chains[chain].chainID}")
    print(f"\n{len(atoms)} Atoms")
    view_chain(chains)


if __name__ == "__main__":
    main()
