from enum import IntEnum

class Pedal():

    def __init__(self, tsl_string: str, on: bool = True):
        self.on_off = on
        self._tsl_string = tsl_string

    def _set_tsl_string(self, s: str):
        self._tsl_string = s
    def _get_tsl_string(self):
        out = self._tsl_string
        return out

    def to_dict(self):
        out = {}

        for key, value in self._get_items().items():
            out[self._get_tsl_string() + '_' + key] = value
        
        return out
    
    def _get_items(self):
        out = {}

        for key, value in self.__dict__.items():
            if(not key.startswith('_')):
                out[key] = self._filter_value(value)

        return out

    def _filter_value(self, value: int):
        if(type(value) is bool):
            return 1 if value is True else 0 # can be done better I think
        return value


class FXType(IntEnum):
    DEFAULT = 21
    TOUCH_WAH = 0
    AUTO_WAH = 1
    PEDAL_WAH = 2 # pass wah pedal to pedal argument
    COMPRESSOR = 3
    LIMITER = 4
    DISTORTION = 5 # pass ds pedal to pedal argument
    GRAPHIC_EQ = 6 # pass eq pedal to pedal argument
    PARAMETRIC_EQ = 7 # pass eq pedal to pedal argument
    TONE_MODIFY = 8
    GUITAR_SIM = 9
    SLOW_GEAR = 10
    DEFRETTER = 11
    WAVE_SYNTH = 12
    SITAR_SIM = 13
    OCTAVE = 14
    PITCH_SHIFTER = 15
    HARMONIST = 16
    SOUND_HOLD = 17
    ACU_PROCESSOR = 18
    PHASER = 19
    FLANGER = 20
    TREMOLO = 21
    ROTARY_1 = 22
    UNI_V = 23
    PAN = 24
    SLICER = 25
    VIBRATO = 26
    RING_MODULATE = 27
    HUMANIZER = 28
    TWO_BY_TWO_CHORUS = 29
    SUB_DELAY = 30
    AC_GUITAR_SIM = 31
    ROTARY_2 = 32
    TERA_ECHO = 33
    OVER_TONE = 34
    PHASER_90E = 35
    FLANGER_117E = 36
    WAH_95E = 37 # pass wah pedal to pedal argument
    DC30 = 38
    HEAVY_OCTIVE = 39

class FXPedal(Pedal):
    FX_TYPE = FXType.DEFAULT

    def __init__(self,
                tsl_string: str,
                **kwargs
    ):
        super().__init__(tsl_string, True)
        del self.on_off

class BasePedal(Pedal):

    CHAIN_POS = [0]

    def __init__(self, tsl_string: str, on: bool = True):
        super().__init__(tsl_string, on)
        self._num = 0

    def get_chain_index(self):
        return self.CHAIN_POS[self._num]

    def _get_tsl_string(self):
        out = self._tsl_string
        if(self._num):
            out += str(self._num)
        return out