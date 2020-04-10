from .. import FXType, FXPedal
from enum import IntEnum

class GraphicEQType(IntEnum):
    DEFAULT = 0

class GraphicEQ(FXPedal):

    FX_TYPE = FXType.GRAPHIC_EQ

    def __init__(self,
                _type: GraphicEQType = GraphicEQType.DEFAULT,
                geq_125hz: int = 20,
                geq_16khz: int = 20,
                geq_1khz: int = 20,
                geq_250hz: int = 20,
                geq_2khz: int = 20,
                geq_31hz: int = 220,
                geq_4khz: int = 20,
                geq_500hz: int = 20,
                geq_62hz: int = 20,
                geq_8khz: int = 20,
                geq_level: int = 24,
                **kwargs
    ):
        super().__init__('graphic_eq')
        self['125hz'] = geq_125hz
        self['16khz'] = geq_16khz
        self['1khz'] = geq_1khz
        self['250hz'] = geq_250hz
        self['2khz'] = geq_2khz
        self['31hz'] = geq_31hz
        self['4khz'] = geq_4khz
        self['500hz'] = geq_500hz
        self['62hz'] = geq_62hz
        self['8khz'] = geq_8khz
        self['level'] = geq_level