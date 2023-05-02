from reaction import Reaction
from molecule import Molecule
from determine_stoichiometric_coefficients import SystemOfReactions
from bulk_reaction import bulk_reaction

H2 = Molecule(chemical_form = "H2")
O2 = Molecule(chemical_form = "O2")
C = Molecule(chemical_form = "C")
H2O = Molecule(chemical_form = "H2O")
CO2 = Molecule(chemical_form = "CO2")
O = Molecule(chemical_form = "O")

br = bulk_reaction(species = [H2, O2, C, H2O, CO2, O])

for i in br.species:
    print(i.base_representation)

"""
r = Reaction(reactants = [H2, O2], products = [OH])

S = SystemOfReactions()
S.add_reaction(reaction = r)
S.solve_for_coefficients()
print("reactants stoichiometric coefficients: ", r.reactants_stoichiometric_coefficients)
print("products stoichiometric coefficients: ", r.products_stoichiometric_coefficients)
"""
