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
        print(f'{melon.name} pairs with {" & ".join(melon.pairings)}')
        # for i in range(len(melon.pairings)):
        #     print(melon.pairings[i])

print_pairing_info(melon_types)

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of MelonType by code."""

    melon_dict = {}

    for melon in melon_types:
        melon_dict[melon.code] = melon

    return melon_dict

melon_dict = make_melon_type_lookup(melon_types)

print(melon_dict)

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""
    def __init__(self, melon_type, shape_rating, color_rating, harvested_from, harvested_by):

        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from = harvested_from
        self.harvested_by = harvested_by


    def is_sellable(self):
        """ shape and color must be > 5 | harvested_from != Field 3"""

        if self.shape_rating > 5 and self.color_rating > 5 and self.harvested_from != 3:
            return True
        else:
            return False



def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melon_1 = Melon(melon_types["yw"], 8, 7, 2, "Sheila")
    melon_2 = melon(melon_types["yw"], 3, 4, 2, "Sheila")
    melon_3 = melon(melon_types["yw"], 9, 8, 3, "Sheila")
    melon_4 = melon(melon_types["cas"], 10, 6, 35,"Sheila")
    melon_5 = melon(melon_types["cren"], 8, 9, 35,"Michael")
    melon_6 = melon(melon_types["cren"], 8, 2, 35,"Michael")
    melon_7 = melon(melon_types["cren"], 2, 3, 4, "Michael")
    melon_9 = melon(melon_types["yw"], 7, 10, 3, "Sheila")



def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



