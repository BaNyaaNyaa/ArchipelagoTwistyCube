from collections import defaultdict
from enum import StrEnum

# List of possible colors
class Color(StrEnum):
    WHITE = 'White'
    YELLOW = 'Yellow'
    RED = 'Red'
    ORANGE = 'Orange'
    BLUE = 'Blue'
    GREEN = 'Green'

# Generates the properties, like items shuffle, for the cube
class CubePuzzle:
    MAX_SIZE = 4

    def __init__(self, size: int):
        self.size = size
        self.colors = list(Color)
    
    # Get all the items associated to this cube
    def get_items(self) -> list[str]:
        items = []
        for i in range(1, self.size*self.size+1):
            for color in self.colors:
                items.append(f"{color.value} Sticker #{i}")
        return items

    # Get the item groups for this cube
    def get_item_groups(self) -> dict[str, list[str]]:
        groups = defaultdict(list)
        for item in self.get_items():
            color = item.split(' ', 2)[0]
            groups[color].append(item)
        # Converts to a regular dict because I'm not sure if defaultdict can cause issues with the randomizer
        return dict(groups)
    
    # Returns a map containing the permutation of the color layout
    # If has_random_layout is false, returns the identity permutation (Each color maps to itself)
    def get_color_permutation(self, has_random_layout: bool) -> dict[str, str]:
        side_keys = self.colors.copy
        side_values = side_keys.copy()
        if has_random_layout:
            self.random.shuffle(side_values)
        return dict(zip(side_keys, side_values))