"""
Function:
Author: Luke Bartholomew
Edits:
"""
from sympy import Matrix
import numpy as np

class SystemOfReactions():
    def __init__(self) -> None:
        self.reactions = [] 

    def add_reaction(self, reaction):
        self.reactions.append(reaction)

    def form_matrix_for_reactions(self, reaction):
        n_reactants = len(reaction.reactants)
        n_products = len(reaction.products)
        n_molecules = n_reactants + n_products
        n_equations = len(reaction.base_element_names)
        reaction_matrix = np.zeros((n_equations, n_molecules))
        for row_ind, element in enumerate(reaction.base_element_names):
            for col_ind, reactant in enumerate(reaction.reactants):
                reaction_matrix[row_ind][col_ind] = reactant.base_representation[element]
            for col_ind, product in enumerate(reaction.products):
                reaction_matrix[row_ind][col_ind + n_reactants] = -1 * product.base_representation[element]
        return reaction_matrix

    def solve_for_coefficients(self):
        for reaction in self.reactions:
            reaction_matrix = self.form_matrix_for_reactions(reaction = reaction)
            reaction_matrix = Matrix(reaction_matrix)
            null_space_of_reaction_matrix = reaction_matrix.nullspace()
            stoichiometric_coefficients = null_space_of_reaction_matrix[0]
            for null_space in null_space_of_reaction_matrix[1:]:
                stoichiometric_coefficients += null_space
            stoichiometric_coefficients = stoichiometric_coefficients.transpose().tolist()[0]
            print("For the reaction:", reaction.reaction_string)
            print("Stoichiometric Coefficients:")
            self.put_coefficients_into_reactions(reaction = reaction, coefficients = stoichiometric_coefficients)
            
    def put_coefficients_into_reactions(self, reaction, coefficients):
        n_reactants = len(reaction.reactants)
        for ind, molecule in enumerate(reaction.reactants):
            reaction.reactants_stoichiometric_coefficients[molecule.chemical_form] += coefficients[ind]
        for ind, molecule in enumerate(reaction.products):
            reaction.products_stoichiometric_coefficients[molecule.chemical_form] += coefficients[ind + n_reactants]
        print(reaction.reactants_stoichiometric_coefficients, reaction.products_stoichiometric_coefficients)
        
