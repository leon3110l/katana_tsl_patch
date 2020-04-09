from enum import IntEnum

from ..pedal import FXPedal, FXType

class SoundHoldType(IntEnum):
    DEFAULT = 0

class SoundHold(FXPedal):

    FX_TYPE = FXType.SOUND_HOLD

    def __init__(self,
                _type : SoundHoldType = SoundHoldType.DEFAULT,
                effect_level: int = 50,
                hold: int = 0,
                rise_time: int = 50,
                **kwargs
    ):
        super().__init__('sound_hold')
        self.type = _type
        self.effect_level = effect_level
        self.hold = hold
        self.rise_time = rise_time