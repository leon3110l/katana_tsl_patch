from .. import FXType, FXPedal
from enum import IntEnum

class Wah95EType(IntEnum):
    DEFAULT = 0

class Wah95E(FXPedal):

    FX_TYPE = FXType.WAH_95E

    def __init__(self,
                _type: Wah95EType = Wah95EType.DEFAULT,
                direct_mix: int = 0,
                effect_level: int = 100,
                pedal_max: int = 100,
                pedal_min: int = 0,
                pedal_pos: int = 100,
                **kwargs
    ):
        super().__init__('wah95e')
        self.direct_mix = direct_mix
        self.effect_level = effect_level
        self.pedal_max = pedal_max
        self.pedal_min = pedal_min
        self.pedal_pos = pedal_pos