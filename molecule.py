"""
Function:
Author: Luke Bartholomew
Edits:
"""
import re
class Molecule():
    def __init__(self, chemical_form) -> None:
        self.chemical_form = chemical_form
        self.primary_elements = re.findall('[A-Z][^A-Z]*', chemical_form)
        self.base_representation = {}
        for element in self.primary_elements:
            m = re.search(r'\d+$', element)
            if m is not None:
                num_digits = len(m.group())
                base_element_name = element[:len(element) - num_digits]
                self.base_representation[base_element_name] = int(m.group())
            else:
                self.base_representation[element] = 1
