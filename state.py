# this is the state file for the game fdtheboardgame


from dataclasses import dataclass, field
from enum import Enum 

class Tires(Enum):
    SOFT = "soft"
    MEDIUM = "medium"
    HARD = "hard"


@dataclass
class Car:
    name: str
    tires: Tires
    pitted_this_lap: bool = False
    finished: bool = False 
    lap: int = 1
    position: int = 1
    wear: int = 0 
    damage: int = 0
    tires_used: list = field(default_factory=list) #initalizs a list per object created once called
    hand: list = field(default_factory=list) #initalizs a list per object created once called 

    def __post_init__(self):
        self.tires_used.append(self.tires)


    
if __name__ == "__main__":

    car = Car("david", Tires.HARD)
    print(car)