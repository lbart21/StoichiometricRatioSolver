"""
Function:
Author: Luke Bartholomew
Edits:
"""

class Reaction():
    def __init__(self, reactants, products) -> None:
        self.reactants = reactants
        self.products = products
        self.base_element_names = []
        self.reaction_string = ""
        
        self.reactants_molecule_names = []
        self.products_molecule_names = []

        for molecule in self.reactants:
            if molecule.chemical_form not in self.reactants_molecule_names:
                self.reactants_molecule_names.append(molecule.chemical_form)
            self.reaction_string += molecule.chemical_form + " + "
            for element in molecule.base_representation.keys():
                if element not in self.base_element_names:
                    self.base_element_names.append(element)
        self.reaction_string = self.reaction_string[:-3] #Trim off extra + symbol
        self.reaction_string += " => "
        for molecule in self.products:
            if molecule.chemical_form not in self.products_molecule_names:
                self.products_molecule_names.append(molecule.chemical_form)
            self.reaction_string += molecule.chemical_form + " + "
            for element in molecule.base_representation.keys():
                if element not in self.base_element_names:
                    self.base_element_names.append(element)
        self.reaction_string = self.reaction_string[:-3]
        for element in self.base_element_names:
            for molecule in self.reactants:
                if element not in molecule.base_representation.keys():
                    molecule.base_representation[element] = 0
            for molecule in self.products:
                if element not in molecule.base_representation.keys():
                    molecule.base_representation[element] = 0
        
        self.reactants_stoichiometric_coefficients = {name:0 for name in self.reactants_molecule_names}
        self.products_stoichiometric_coefficients = {name:0 for name in self.products_molecule_names}

