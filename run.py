import os
import sys
from unpack import WoWsUnpack

if __name__ == "__main__":
    print("Make sure the game path is valid!")
    print()
    print("Unpacking...")

    if os.path.exists('game.path'):
        with open('game.path', 'r') as f:
            path = f.read().strip()
        unpack = WoWsUnpack(path)

        try:
            unpack.unpackGameParams()
            unpack.decodeGameParams()

            # optional actions
            # unpack.decodeLanguages()
            # unpack.unpackGameIcons()
            # unpack.unpackGameMaps()
        except FileNotFoundError:
            print("Make sure the game path is valid. It should look like C:\Games\World_of_Warships")
            print("\nhttps://github.com/WoWs-Info/wows_gameparams")
            sys.exit(-1)
    else:
        with open('game.path', 'w') as f:
            print("Created game.path")
            print(
                "Please place your game path in it. It should look like C:\Games\World_of_Warships")
            print("\nhttps://github.com/WoWs-Info/wows_gameparams")
            sys.exit(-1)

    print("Done unpacking!")
    input("Press Enter to exit...")