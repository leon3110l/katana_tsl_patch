from ..wah import WahSubType
from ..pedal import FXType, FXPedal

class PedalWah(FXPedal):

    FX_TYPE = FXType.PEDAL_WAH

    def __init__(self,
                _type: WahSubType = WahSubType.DEFAULT,
                direct_mix: int = 0,
                effect_level: int = 100,
                pedal_max: int = 100,
                pedal_min: int = 0,
                pedal_pos: int = 100,
                **kwargs
    ):
        super().__init__('sub_wah')
        self.type = _type
        self.direct_mix = direct_mix
        self.effect_level = effect_level
        self.pedal_max = pedal_max
        self.pedal_min = pedal_min
        self.pedal_pos = pedal_pos