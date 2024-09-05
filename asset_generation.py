# inspired by Jude Markabawi's code (posted in #game1-sprite-based in the Discord server)
# Also referenced PIL tutorial at https://pillow.readthedocs.io/en/stable/handbook/tutorial.html

from PIL import Image


artList = ["dirt1", "dirt2", "dirt3", "dirt4", "dryplant1", "dryplant2",
           "dyingplant1", "dyingplant2", "healthyplant1", "healthyplant2",
           "player1", "player2"]

def getPalette(imgData):
    return list(set(imgData))

def filterTransparent(imgData):
    def filterColor(rgba):
        r, g, b, a = rgba[0], rgba[1], rgba[2], rgba[3]
        if r == 255 and g == 255 and b == 255:
            return (0, 0, 0, 0)
        if r == 0 and g == 0 and b == 0:
            return (0, 0, 0, 0)
        return(r, g, b, a)
    return list(map(filterColor, imgData))

def getPaletteTable(imgDataList):
    paletteList = list(map(lambda imgData : getPalette(imgData), imgDataList))
    seen = []
    for palette in paletteList:
        if palette not in seen:
            seen.append(palette)
    return seen


def getPath(path):
    return "art/" + path + ".png"

paths = map(lambda title : getPath(title), artList)
imgDataList = list(map(lambda path : Image.open(path).getdata(), paths))

# unencoded list of tiles
filteredImgDataList = list(map(lambda imgData : filterTransparent(imgData), imgDataList))

# final palette table
paletteTable = getPaletteTable(filteredImgDataList)