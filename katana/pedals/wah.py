from .pedal import BasePedal
from enum import IntEnum

class WahEnum(IntEnum):
    pass

class WahType(WahEnum):
    DEFAULT = 0
    WAH = 0
    PEDAL_BEND = 1
    WAH_95E = 2

class WahSubType(WahEnum):
    DEFAULT = 0
    CRY_WAH = 0
    VO_WAH = 1
    FAT_WAH = 2
    LIGHT_WAH = 3
    SEVEN_STRING_WAH = 4
    RESO_WAH = 5

class Wah(BasePedal):

    CHAIN_POS = [11]

    def __init__(self,
                _type: WahEnum = WahType.DEFAULT,
                on: bool = True,
                evh95_direct_mix: int = 0,
                evh95_effect_level: int = 0,
                evh95_pedal_max: int = 0,
                evh95_pedal_min: int = 0,
                evh95_position: int = 0,
                pedal_bend_direct_mix: int = 0,
                pedal_bend_effect_level: int = 100,
                pedal_bend_pitch: int = 36,
                pedal_bend_position: int = 0,
                position: int = 0,
                wah_direct_mix: int = 0,
                wah_effect_level: int = 100,
                wah_pedal_max: int = 100,
                wah_pedal_min: int = 0,
                wah_position: int = 100
                # wah_type: int = 0,
    ):
        super().__init__('pedal_fx', on)

        if(type(_type) is WahSubType):
            self.type = WahType.DEFAULT
            self.wah_type = _type
        else:
            self.type = _type
            self.wah_type = WahSubType.DEFAULT

        self.evh95_direct_mix = evh95_direct_mix
        self.evh95_effect_level = evh95_effect_level
        self.evh95_pedal_max = evh95_pedal_max
        self.evh95_pedal_min = evh95_pedal_min
        self.evh95_position = evh95_position
        self.pedal_bend_direct_mix = pedal_bend_direct_mix
        self.pedal_bend_effect_level = pedal_bend_effect_level
        self.pedal_bend_pitch = pedal_bend_pitch
        self.pedal_bend_position = pedal_bend_position
        self.position = position
        self.wah_direct_mix = wah_direct_mix
        self.wah_effect_level = wah_effect_level
        self.wah_pedal_max = wah_pedal_max
        self.wah_pedal_min = wah_pedal_min
        self.wah_position = wah_position