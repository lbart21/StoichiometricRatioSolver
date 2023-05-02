class BulkReaction():
    def __init__(self, species) -> None:
        """
        species = [molecule_1, molecule_2, ..., molecule_n]
        """
        self.species = species
        self.species_names = []
        self.elements = []
        for spcs in species:
            self.species_names.append(spcs.chemical_form)
            for base_element in spcs.base_representation.keys():
                #print(base_element, spcs.base_representation[base_element])
                if base_element not in self.elements:
                    self.elements.append(base_element)
        #print(self.elements)
        for spcs in self.species:
            for base_element in self.elements:
                if base_element not in spcs.base_representation.keys():
                    spcs.base_representation[base_element] = 0
        