def split_before_uppercases(formula):
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

def split_at_digit(formula):
    for i in range(len(formula)):
        if formula[i].isdigit():
            return formula[:i], int(formula[i:])
    
    return formula, 1

def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.  
    Example: 'H2O' → {'H': 2, 'O': 1}"""

    # Step 1: Initialize an empty dictionary to store atom counts
    atom_dict = {}

        # Step 2: Update the dictionary with the atom name and count
    mol = split_before_uppercases(molecular_formula)
    for i in mol:
        atom, num = split_at_digit(i)
        atom_dict[atom] = num
    
    return atom_dict
    

def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
