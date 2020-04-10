from enum import IntEnum

from .. import FXPedal, FXType

class DC30Type(IntEnum):
    DEFAULT = 0
    CHORUS = 0
    ECHO = 1

class DC30(FXPedal):

    FX_TYPE = FXType.DC30

    def __init__(self,
                _type : DC30Type = DC30Type.DEFAULT,
                chorus_intensity: int = 0,
                echo_intensity: int = 0,
                echo_repeat_rate_h: int = 0,
                echo_repeat_rate_l: int = 40,
                echo_repeat_rate: int = 400,
                echo_volume: int = 0,
                input_volume: int = 0,
                output: int = 0,
                tone: int = 0,
                **kwargs
    ):
        super().__init__('dc30')
        self.selector = _type
        self.chorus_intensity = chorus_intensity
        self.echo_intensity = echo_intensity
        self.echo_repeat_rate_h = echo_repeat_rate_h
        self.echo_repeat_rate_l = echo_repeat_rate_l
        self.echo_repeat_rate = echo_repeat_rate
        self.echo_volume = echo_volume
        self.input_volume = input_volume
        self.output = output
        self.tone = tone
        