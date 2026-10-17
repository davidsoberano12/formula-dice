from enum import Enum


class Tires(Enum):
	SOFT = "soft"
	MEDIUM = "medium"
	HARD = "hard"


# Each compound has ten cards: two copies of each value in its range.
COMPOUNDS = {
	Tires.SOFT: {"hand": [value for value in range(5, 10) for _ in range(2)], "wear_limit": 8},
	Tires.MEDIUM: {"hand": [value for value in range(4, 9) for _ in range(2)], "wear_limit": 12},
	Tires.HARD: {"hand": [value for value in range(3, 8) for _ in range(2)], "wear_limit": 18},
}
