import sting_utils as string_u, equation_utils as equation_u 

def balance_reaction(reaction): #"Fe2O3 + H2 -> Fe + H2O"
    
    reactants, products = string_u.parse_chemical_reaction(reaction) # [""Fe2O3", "H2"], ["Fe", "H2O""]
    reactant_atoms = string_u.count_atoms_in_reaction(reactants) # [{"Fe":2, "O":1}, {"H":2}]
    product_atoms = string_u.count_atoms_in_reaction(products)

    equations, coefficients = equation_u.build_equations(reactant_atoms, product_atoms)
    coefficients = equation_u.my_solve(equations, coefficients) + [1]

    return coefficients 

