from reaction import Reaction
from molecule import Molecule
from determine_stoichiometric_coefficients import SystemOfReactions

H2 = Molecule(chemical_form = "H2")
O2 = Molecule(chemical_form = "O2")
OH = Molecule(chemical_form = "OH")

r = Reaction(reactants = [H2, O2], products = [OH])

S = SystemOfReactions()
S.add_reaction(reaction = r)
S.solve_for_coefficients()
print("reactants stoichiometric coefficients: ", r.reactants_stoichiometric_coefficients)
print("products stoichiometric coefficients: ", r.products_stoichiometric_coefficients)
