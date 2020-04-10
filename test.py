from katana import *
from katana.pedals.effects.booster import Booster as FXBooster

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