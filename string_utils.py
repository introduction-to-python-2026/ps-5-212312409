def split_befor_uppercases(formula):
    start = 0
    end = 1
    elements_lst = []

    if not formula:
        return elements_lst
        
    while end < len(formula):
        if formula[end].isupper():
        elements_lst.append(formula[start:end])
            start = end
        end+=1
        
    elements_lst.append(formula[start:])

    return element_lst

def split_at_digit(formula):
    for char_index, char in enumerate(formula):
        if char.isdigit():
            return formula[:char_index], int(formula[char_index:])
    return formula, 1
        
def count_atoms_in_molecule(molecular_formula):
    atom_dict = {}
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
