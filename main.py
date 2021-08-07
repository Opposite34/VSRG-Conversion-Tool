from converter import *

gamelist = ["osu", "sm", "qua", "bms"]

filepath = str(input("Path to file: "))

print("Which game you want to convert to? (Type the number)")

game = int(input("1.osu!mania, 2.StepMania, 3.Quaver, 4.BMS, 5.all: "))

game_out = ""

if game == 1:
    game_out = ["osu"]

elif game == 2:
    game_out = ["sm"]

elif game == 3:
    game_out = ["qua"]

elif game == 4:
    game_out = ["bms"]

elif game == 5:
    game_out = gamelist

c = VSRGConverter(filepath)

for game in game_out:
    if not c.game == game:
        c.convert(game)
        c.write()
    
    else:
        print(f"Skipping conversion to {game} as the original file is from that game")

print("Done")