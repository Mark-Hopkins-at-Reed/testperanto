##
# morphology.py
# Tools for generating word morphology.
##

from abc import ABC, abstractmethod

class Morpher(ABC):
    """Modifies a word stem to express syntactic properties. Abstract class.

    Methods
    -------
    morph(stem, properties)
        Returns a declension of the word stem based on provided syntactic properties.
    """

    def morph(self, word, properties):
        """Returns a declension of the word stem based on provided syntactic properties.

        Parameters
        ----------
        word : str
            The original word stem
        properties: dict
            Maps (string) syntactic properties to their values

        Returns
        -------
        str
            A declension of the word stem based on the provided syntactic properties
        """


class SuffixMorpher(Morpher):
    """Adds a suffix to a word stem to express syntactic properties.

    To initialize, we provide a list of property names, and a "suffix map" that
    associates a suffix with tuples of corresponding property values.

    For instance, German adjectives have suffixes based on the gender and case
    of the noun they modify. To build a SuffixMorpher for this, we can do the
    following:
        morpher = SuffixMorpher(property_names=('GENDER', 'CASE'),
                                suffix_map={('m', 'acc'): 'en',
                                            ('f', 'acc'): 'e',
                                            ('n', 'acc'): 'es',
                                            ('m', 'dat'): 'em',
                                            ('f', 'dat'): 'er',
                                            ('n', 'dat'): 'em'})

    Then:
        result = morpher.morph('rot', {'GENDER': 'n', 'CASE': 'acc'})
    returns 'rotes', and:
        result = morpher.morph('rot', {'GENDER': 'm', 'CASE': 'dat'})
    returns 'rotem'.

    Methods
    -------
    morph(stem, properties)
        Appends a suffix to the word stem based on provided syntactic properties.
    """

    def __init__(self, property_names, suffix_map):
        """
        Parameters
        ----------
        property_names : list[str]
            Names of the syntactic properties used to determine the suffix
        suffix_map: dict
            Maps a tuple of property values (corresponding to property_names) to a
            corresponding suffix
        """

        self.property_names = property_names
        self.suffix_map = suffix_map

    def morph(self, word, properties):
        """Appends a suffix to the word stem based on provided syntactic properties.

        Parameters
        ----------
        word : str
            The original word stem
        properties: dict
            Maps (string) syntactic properties to their values

        Returns
        -------
        str
            A declension of the word stem based on the provided syntactic properties
        """
        value = tuple([properties[p] for p in self.property_names])
        suffix = self.suffix_map[value]
        return word + suffix

class PrefixMorpher(Morpher):

    def __init__(self, property_names, prefix_map):
        """
        Parameters
        ----------
        property_names : list[str]
            Names of the syntactic properties used to determine the suffix
        prefix_map: dict
            Maps a tuple of property values (corresponding to property_names) to a
            corresponding suffix
        """

        self.property_names = property_names
        self.prefix_map = prefix_map

    def morph(self, word, properties):
        """Prepends a prefix to the word stem based on provided syntactic properties.

        Parameters
        ----------
        word : str
            The original word stem
        properties: dict
            Maps (string) syntactic properties to their values

        Returns
        -------
        str
            A declension of the word stem based on the provided syntactic properties
        """
        value = tuple([properties[p] for p in self.property_names])
        prefix = self.prefix_map[value]
        return prefix + word



##
# Some example Morphers
##

class EnglishVerbMorpher(Morpher):
    def __init__(self):
        self.base_morpher = SuffixMorpher(property_names=('PERSON', 'COUNT', 'TENSE', 'POLARITY'),
                                          suffix_map={('1', 'sng', 'present', 'pos'): '',
                                                      ('1', 'plu', 'present', 'pos'): '',
                                                      ('1', 'sng', 'perfect', 'pos'): 'd',
                                                      ('1', 'plu', 'perfect', 'pos'): 'd',
                                                      ('3', 'sng', 'present', 'pos'): 's',
                                                      ('3', 'plu', 'present', 'pos'): '',
                                                      ('3', 'sng', 'perfect', 'pos'): 'd',
                                                      ('3', 'plu', 'perfect', 'pos'): 'd',
                                                      ('1', 'sng', 'present', 'neg'): '',
                                                      ('1', 'plu', 'present', 'neg'): '',
                                                      ('1', 'sng', 'perfect', 'neg'): '',
                                                      ('1', 'plu', 'perfect', 'neg'): '',
                                                      ('3', 'sng', 'present', 'neg'): '',
                                                      ('3', 'plu', 'present', 'neg'): '',
                                                      ('3', 'sng', 'perfect', 'neg'): '',
                                                      ('3', 'plu', 'perfect', 'neg'): ''})
        self.negation_morpher = PrefixMorpher(property_names=('PERSON', 'COUNT', 'TENSE', 'POLARITY'),
                                              prefix_map={  ('1', 'sng', 'present', 'pos'): '',
                                                            ('1', 'plu', 'present', 'pos'): '',
                                                            ('1', 'sng', 'perfect', 'pos'): '',
                                                            ('1', 'plu', 'perfect', 'pos'): '',
                                                            ('3', 'sng', 'present', 'pos'): '',
                                                            ('3', 'plu', 'present', 'pos'): '',
                                                            ('3', 'sng', 'perfect', 'pos'): '',
                                                            ('3', 'plu', 'perfect', 'pos'): '',
                                                            ('1', 'sng', 'present', 'neg'): 'do not ',
                                                            ('1', 'plu', 'present', 'neg'): 'do not ',
                                                            ('1', 'sng', 'perfect', 'neg'): 'did not ',
                                                            ('1', 'plu', 'perfect', 'neg'): 'did not ',
                                                            ('3', 'sng', 'present', 'neg'): 'does not ',
                                                            ('3', 'plu', 'present', 'neg'): 'do not ',
                                                            ('3', 'sng', 'perfect', 'neg'): 'did not ',
                                                            ('3', 'plu', 'perfect', 'neg'): 'did not '})

    def morph(self, word, properties):
        suffixed = self.base_morpher.morph(word, properties)
        negated = self.negation_morpher.morph(suffixed, properties)
        return negated


class EnglishNounMorpher(Morpher):
    def __init__(self):
        self.base_morpher = SuffixMorpher(property_names=('COUNT',),
                                          suffix_map={('sng',): '', ('plu',): 's'})

    def morph(self, word, properties):
        return self.base_morpher.morph(word, properties)


class JapaneseVerbMorpher(Morpher):
    def __init__(self):
        self.base_morpher = SuffixMorpher(property_names=('PERSON', 'COUNT', 'TENSE'),
                                          suffix_map={('1', 'sng', 'present'): 'masu',
                                                      ('1', 'plu', 'present'): 'masu',
                                                      ('1', 'sng', 'perfect'): 'mashita',
                                                      ('1', 'plu', 'perfect'): 'mashita',
                                                      ('3', 'sng', 'present'): 'masu',
                                                      ('3', 'plu', 'present'): 'masu',
                                                      ('3', 'sng', 'perfect'): 'mashita',
                                                      ('3', 'plu', 'perfect'): 'mashita'})

    def morph(self, word, properties):
        return self.base_morpher.morph(word, properties)
