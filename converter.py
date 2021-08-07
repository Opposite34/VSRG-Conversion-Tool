#osu!mania
from reamber.osu.OsuMap import OsuMap

from reamber.algorithms.convert.OsuToQua import OsuToQua
from reamber.algorithms.convert.OsuToSM import OsuToSM
from reamber.algorithms.convert.OsuToBMS import OsuToBMS

#StepMania
from reamber.sm.SMMapSet import SMMapSet

from reamber.algorithms.convert.SMToOsu import SMToOsu
from reamber.algorithms.convert.SMToQua import SMToQua
from reamber.algorithms.convert.SMToBMS import SMToBMS

#Quaver
from reamber.quaver.QuaMap import QuaMap

from reamber.algorithms.convert.QuaToOsu import QuaToOsu
from reamber.algorithms.convert.QuaToSM import QuaToSM
from reamber.algorithms.convert.QuaToBMS import QuaToBMS

#BMS
from reamber.bms.BMSMap import BMSMap

from reamber.algorithms.convert.BMSToOsu import BMSToOsu
from reamber.algorithms.convert.BMSToQua import BMSToQua
from reamber.algorithms.convert.BMSToSM import BMSToSM

class VSRGConverter:
    def __init__(self, filepath):

        if filepath[-3:] == ".sm":
            self.game = "sm"
        else:
            self.game = filepath[-3:]

        self.name = filepath[:-(len(self.game)+1)]
        self.map_in = self.game_check(filepath)
    
    def game_check(self, filepath):

        if self.game == "sm":

        #seems like SMMap doesn't have readFile method implemented
            map = SMMapSet.readFile(filepath)

        elif self.game == "osu":
            map = OsuMap.readFile(filepath)

        elif self.game == "qua":
            map = QuaMap.readFile(filepath)

        elif self.game == "bms":
            map = BMSMap.readFile(filepath)
        
        return map

    def convert(self, out_game):
        out_game = out_game.lower()

        if self.game == "sm":
            c = SMConverter(self.map_in)

        elif self.game == "osu":
            c = OsuConverter(self.map_in)

        elif self.game == "qua":
            c = QuaConverter(self.map_in)

        elif self.game == "bms":
            c = BMSConverter(self.map_in)

        self.map_out = c.convert(out_game)
        self.extension = f".{out_game}"

    def write(self):
        if self.game != "sm":
            self.map_out.writeFile(f"{self.name}{self.extension}")      
        else:
            for map in self.map_out:
                map.writeFile(f"{self.name}{self.extension}")

############################################################################

#Each of the converters
#Not optimal, but it'll do

#osu! converter
class OsuConverter:
    def __init__(self, map):
        self.map_in = map
        
    def convert(self, game):
        if game == "qua":
            out = OsuToQua.convert(self.map_in)
            self.extension = ".qua"

        elif game == "sm":
            out = OsuToSM.convert(self.map_in)
            self.extension = ".sm"

        elif game == "bms":
            out = OsuToBMS.convert(self.map_in)
            self.extension = ".bms"

        return out

#sm converter
class SMConverter:
    def __init__(self, map):
        self.map_in = map
    
    def convert(self, game):
        if game == "qua":
            out = SMToQua.convert(self.map_in)
            self.extension = ".qua"

        elif game == "osu":
            out = SMToOsu.convert(self.map_in)
            self.extension = ".osu"

        elif game == "bms":
            out = SMToBMS.convert(self.map_in)
            self.extension = ".bms"

        return out

#qua converter
class QuaConverter:
    def __init__(self, map):
        self.map_in = map
    
    def convert(self, game):
        if game == "sm":
            out = QuaToSM.convert(self.map_in)
            self.extension = ".sm"

        elif game == "osu":
            out = QuaToOsu.convert(self.map_in)
            self.extension = ".osu"

        elif game == "bms":
            out = QuaToBMS.convert(self.map_in)
            self.extension = ".bms"

        return out

#bms converter
class BMSConverter:
    def __init__(self, map):
        self.map_in = map
    
    def convert(self, game):
        if game == "sm":
            out = BMSToSM.convert(self.map_in)
            self.extension = ".sm"

        elif game == "osu":
            out = BMSToOsu.convert(self.map_in)
            self.extension = ".osu"

        elif game == "qua":
            out = BMSToQua.convert(self.map_in)
            self.extension = ".qua"

        return out

############################################################################