from .pedal import BasePedal
from enum import IntEnum

class VolumeType(IntEnum):
    DEFAULT = 0

class Volume(BasePedal):

    CHAIN_POS = [12]

    def __init__(self,
                _type: VolumeType = VolumeType.DEFAULT,
                on: bool = True,
                level: int = 100,
                volume_curve: int = 0,
                volume_max: int = 0,
                volume_min: int = 0,
                **kwargs
    ):
        super().__init__('foot_volume', on)
        self.type = _type
        self.level = level
        self.volume_curve = volume_curve
        self.volume_max = volume_max
        self.volume_min = volume_min