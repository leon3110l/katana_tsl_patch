from ..booster import BoosterType
from ..pedal import FXType, FXPedal

class Booster(FXPedal):

    FX_TYPE = FXType.DISTORTION

    def __init__(self,
                _type: BoosterType = BoosterType.DEFAULT,
                on: bool = True,
                bottom: int = 50,
                direct_mix: int = 0,
                drive: int = 20,
                effect_level: int = 56,
                solo_level: int = 50,
                solo_sw: int = 0,
                tone: int = 46,
                **kwargs
    ):
        super().__init__('sub_od_ds')
        self.type = _type
        self.bottom = bottom
        self.direct_mix = direct_mix
        self.drive = drive
        self.effect_level = effect_level
        self.solo_level = solo_level
        self.solo_sw = solo_sw
        self.tone = tone