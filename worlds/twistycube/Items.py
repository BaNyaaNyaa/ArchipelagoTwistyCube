import typing


from BaseClasses import Item, ItemClassification
from typing import Optional
from .Puzzle import CubePuzzle

class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    classification: ItemClassification

class TwistyCubeItem(Item):
    game: str = "Twisty Cube"

    def __init__(self, name: str, classification: ItemClassification, code: Optional[int],player: int):
        self.name = name
        self.classification = classification
        self.player = player
        self.code = code
        self.location = None

largest_cube = CubePuzzle(CubePuzzle.MAX_SIZE)

all_items = largest_cube.get_items()
item_groups = largest_cube.get_item_groups()

item_table = {}
for i, item in enumerate(all_items):
    item_table[item] = ItemData(267782000 + i, ItemClassification.progression)
  
item_table["filler"] = ItemData(267781999, ItemClassification.filler)

