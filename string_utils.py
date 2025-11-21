def split_by_capitals(formula):
    split_formula = []
    start = 0
    end = 0   
    
    if formula == "":
      return split_formula

    for i in range(1, len(formula)):
        if formula[i].isupper():
            end = i
            split_formula.append(formula[start:end])
            start = end
    
    split_formula.append(formula[start:])
    return split_formula

def split_at_number(formula):
    for i in range(len(formula)):
        if formula[i].isdigit():
            return formula[:i], int(formula[i:])
    
    return formula, 1

def count_atoms_in_molecule(molecular_formula):

    # Step 1: Initialize an empty dictionary to store atom counts
    atom_dict = {}

    # Step 2: Update the dictionary with the atom name and count
    for atom in split_by_capitals(molecular_formula):
        atom_name, atom_count = split_at_number(atom)
        atom_dict[atom_name] = atom_count
    
    return atom_dict


def parse_chemical_reaction(reaction_equation):
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
