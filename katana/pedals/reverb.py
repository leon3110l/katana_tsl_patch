from .pedal import BasePedal
from enum import IntEnum

class ReverbType(IntEnum):
    DEFAULT = 4
    AMBIENCE = 0
    ROOM = 1
    HALL_1 = 2
    HALL_2 = 3
    PLATE = 4
    SPRING = 5
    MODULATE = 6

class Reverb(BasePedal):

    CHAIN_POS = [9]

    def __init__(self,
                _type: ReverbType = ReverbType.DEFAULT,
                on: bool = True,
                density: int = 5,
                direct_mix: int = 100,
                effect_level: int = 44,
                high_cut: int = 8,
                low_cut: int = 14,
                pre_delay_h: int = 0,
                pre_delay_l: int = 60,
                pre_delay: int = 60,
                spring_sens: int = 50,
                time: int = 4
    ):

        super().__init__('reverb', on)
        self.type = _type
        self.density = density
        self.direct_mix = direct_mix
        self.effect_level = effect_level
        self.high_cut = high_cut
        self.low_cut = low_cut
        self.pre_delay_h = pre_delay_h
        self.pre_delay_l = pre_delay_l
        self.pre_delay = pre_delay
        self.spring_sens = spring_sens
        self.time = time