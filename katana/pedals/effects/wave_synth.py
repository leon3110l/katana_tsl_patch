from enum import IntEnum

from ..pedal import FXPedal, FXType

class WaveSynthType(IntEnum):
    DEFAULT = 0
    SAW = 0
    SQUARE = 1

class WaveSynth(FXPedal):

    FX_TYPE = FXType.WAVE_SYNTH

    def __init__(self,
                _type : WaveSynthType = WaveSynthType.DEFAULT,
                cutoff: int = 40,
                direct_mix: int = 0,
                filter_decay: int = 50,
                filter_depth: int = 50,
                filter_sens: int = 40,
                reso: int = 30,
                synth_level: int = 25,
                **kwargs
    ):
        super().__init__('wave_synth')
        self.wave = _type
        self.cutoff = cutoff
        self.direct_mix = direct_mix
        self.filter_decay = filter_decay
        self.filter_depth = filter_depth
        self.filter_sens = filter_sens
        self.reso = reso
        self.synth_level = synth_level