from enum import IntEnum

from ..pedal import FXPedal, FXType

class VibratoType(IntEnum):
    DEFAULT = 0

class Vibrato(FXPedal):

    FX_TYPE = FXType.VIBRATO

    def __init__(self,
                _type : VibratoType = VibratoType.DEFAULT,
                depth: int = 45,
                level: int = 50,
                rate: int = 80,
                rise_time: int = 0,
                trigger: int = 1,
                **kwargs
    ):
        super().__init__('vibrato')
        self.type = _type
        self.depth = depth
        self.level = level
        self.rate = rate
        self.rise_time = rise_time
        self.trigger = trigger