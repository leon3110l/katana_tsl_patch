from enum import IntEnum

from ..pedal import FXPedal, FXType

class SlowGearType(IntEnum):
    DEFAULT = 0

class SlowGear(FXPedal):

    FX_TYPE = FXType.SLOW_GEAR

    def __init__(self,
                _type : SlowGearType = SlowGearType.DEFAULT,
                level: int = 60,
                rise_time: int = 50,
                sens: int = 45,
    ):
        super().__init__('slow_gear')
        self.type = _type
        self.level = level
        self.rise_time = rise_time
        self.sens = sens