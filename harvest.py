############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)
        

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types.
    code, first_harvest, color, is_seedless, is_bestseller, name
    """

    all_melon_types = []

    musk = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    cas = MelonType("cas", 2003, "orange", False, False, "Casaba")
    cren = MelonType("cren", 1996, "green", False, False, "Crenshaw")
    yw = MelonType("yw", 2013, "yellow", False, True, "Yellow Watermelon")

    musk.add_pairing("mint")
    cas.add_pairing("strawberries")
    cas.add_pairing("mint")
    cren.add_pairing("proscuitto")
    yw.add_pairing("ice cream")

    all_melon_types.append(musk)
    all_melon_types.append(cas)
    all_melon_types.append(cren)
    all_melon_types.append(yw)

    return all_melon_types

melon_types = make_melon_types()
print(melon_types)

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f'{melon.name} pairs with')
        for i in range(len(melon.pairings)):
            print(melon.pairings[i])


print_pairing_info(melon_types)

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}

    for melon in melon_types:
        melon_dict[melon.code] = [melon.code, melon.first_harvest, melon.color, 
            melon.is_seedless, melon.is_bestseller, melon.name]

make_melon_type_lookup(melon_types)



############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



