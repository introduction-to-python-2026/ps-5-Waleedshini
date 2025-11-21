def split_before_uppercases(formula):
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
    
    return elements_lst

def split_at_digit(formula):
    for i in range(1, len(formula)):
        if formula[i].isdigit():
            return formula[:i], int(formula[i:])
    return formula, 1 


def count_atoms_in_molecule(molecular_formula):
    atom_lst = {}
    for atom in split_before_uppercases(molecular_formula):
        atom_name, atom_count = split_at_digit(atom)
        if atom_name in atom_lst:
          atom_lst[atom_name] += atom_count
        else:
         atom_lst[atom_name] = (atom_count)
    return atom_lst


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
