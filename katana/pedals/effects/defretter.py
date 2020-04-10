from enum import IntEnum

from .. import FXPedal, FXType

class DefretterType(IntEnum):
    DEFAULT = 0

class Defretter(FXPedal):

    FX_TYPE = FXType.DEFRETTER

    def __init__(self,
                _type : DefretterType = DefretterType.DEFAULT,
                attack:int = 70,
                depth:int = 0,
                direct_mix:int = 0,
                effect_level:int = 100,
                reso:int = 50,
                sens:int = 50,
                tone:int = 50,
                **kwargs
    ):
        super().__init__('defretter')
        self.type = _type
        self.attack = attack
        self.depth = depth
        self.direct_mix = direct_mix
        self.effect_level = effect_level
        self.reso = reso
        self.sens = sens
        self.tone = tone