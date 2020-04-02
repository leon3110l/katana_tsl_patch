# dont really know how imports work in python...
from katana.patch import Patch
from katana.pedals.amp import Amp, AmpType
from katana.pedals.fx import FX
from katana.pedals.effects.compressor import Compressor, CompressorType
from katana.pedals.wah import Wah, WahSubType
from katana.pedals.booster import Booster, BoosterType
from katana.pedals.ns import NoiseSuppressor
from katana.pedals.volume import Volume
from katana.pedals.eq import EQ
from katana.pedals.sr import SendReturn
from katana.pedals.delay import Delay
from katana.pedals.effects.booster import Booster as FXBooster
from katana.pedals.reverb import Reverb

import json


if __name__ == "__main__":
    katana = Patch("test", [
        # Wah(WahSubType.FAT_WAH),
        # Booster(BoosterType.LEAD_DS),
        # FX(Compressor()),
        NoiseSuppressor(),
        FXBooster(BoosterType.FAT_DS),
        # Volume(level=50),
        Amp(AmpType.CLEAN)
        # EQ(),
        # SendReturn(),
        # Delay(),
        # FX(FXBooster(BoosterType.FAT_DS)),
        # Delay(),
        # Reverb()
    ])
    print(json.dumps(katana.to_tsl(), indent=4))

    katana.save('dingesenzo.tsl')