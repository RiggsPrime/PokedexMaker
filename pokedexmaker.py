from graphics import *
import math

from PIL import Image as Image_PIL

pokefoldername = input("input pokemon name (lowercase): ")
pokeimg = ("pokemon/") + pokefoldername + ("/front.png")
#dex = input("box style: ")
offset = 0
types = input("input type(s) seperated by space (lowercase): ").split(" ")
pokename = pokefoldername.capitalize()
pokenum = input("input (3-digit) pokedex number: ")
outputAs = ("capdex/") + pokenum + ("_") + pokefoldername + (".png")

typesColors = {
	"normal": [232,232,216],
	"fire": [254,209,180],
	"water": [200, 216, 248],
	"grass": [216, 240, 192],
	"electric": [255,253,202],
	"ice": [192, 248, 248],
	"psychic": [248, 152, 216],
	"fighting": [248, 168, 168],
	"poison": [235, 194, 245],
	"bug": [216, 224, 200],
	"ground": [227, 217, 157],
	"rock": [216, 200, 144],
	"steel": [219, 219, 219],
	"ghost": [208, 176, 248],
	"dark": [184, 176, 168],
	"dragon": [170, 194, 244],
	"fairy": [255, 212, 255],
	"flying": [168, 225, 242],
	"unknown": [138, 216, 192]
}

baseColors = {
	"normal": [184,184,168],
	"fire": [248, 144, 48],
	"water": [146, 202, 248],
	"grass": [144, 232, 128],
	"electric": [224,224,0],
	"ice": [48, 216, 208],
	"psychic": [248, 56, 168],
	"fighting": [248, 112, 112],
	"poison": [224, 144, 248],
	"bug": [160, 200, 136],
	"ground": [213, 197, 108],
	"rock": [200, 160, 72],
	"steel": [184, 184, 208],
	"ghost": [168, 112, 248],
	"dark": [144, 136, 136],
	"dragon": [48, 112, 192],
	"fairy": [255, 151, 226],
	"flying": [122, 197, 205],
	"unknown": [40, 174, 132]
}

def fill(output, color):
	for y in range(output.getHeight()):
		for x in range(output.getWidth()):
			output.setPixel(x, y, color_rgb(color[0],color[1],color[2]))

def replaceGround(output, color):
	for y in range(output.getHeight()):
		for x in range(output.getWidth()):
			if(output.getPixel(x, y) == [184,184,168]):
				output.setPixel(x, y, color_rgb(color[0],color[1],color[2]))

def layerOver(image, output, firstpos, ignoredColor):
	for y in range(image.getHeight()):
		for x in range(image.getWidth()):
			if(image.getPixel(x, y) != ignoredColor):
				output.setPixel(firstpos[0]+x, firstpos[1]+y, color_rgb(image.getPixel(x, y)[0],image.getPixel(x, y)[1],image.getPixel(x, y)[2]))


# win = GraphWin("Pokedex Maker", 100, 116)
#win.setBackground(color_rgb(typesColors[types[0]][0], typesColors[types[0]][1], typesColors[types[0]][2]))
box = Image(Point(50,58), "Text/Pokedex.gif")
sprite = Image(Point(50,58), pokeimg)
palette_data = Image_PIL.open(pokeimg).getpalette() # Uses PIL library to grab sprite palette
transparent_color = palette_data[:3] # Truncates the palette data list to the first 3 colors, aka Index 0 of a sprite

output = Image(Point(50, 58),100, 116)


fill(output, typesColors[types[0]])
layerOver(box, output, [0,0], [0,0,0])
replaceGround(output, baseColors[types[0]])
layerOver(sprite, output, [18,26+offset], transparent_color)

if len(types) == 1:
	type1 = Image(Point(50, 58), "Text/Type_"+types[0]+".gif")
	layerOver(type1, output, [28,99], transparent_color)
else:
	type1 = Image(Point(50, 58), "Text/Type_"+types[0]+".gif")
	layerOver(type1, output, [1,99], transparent_color)
	type2 = Image(Point(50, 58), "Text/Type_"+types[1]+".gif")
	layerOver(type2, output, [51,99], transparent_color)

nameX = 36
prevLen = 0
Letters = []
Numbers = []
for x in range(len(pokename)):
	if pokename[x].isupper():
		Letters.append(Image(Point(36,8), "Text/Capital_"+pokename[x]+".gif"))
	else:
		Letters.append(Image(Point(36,8), "Text/Lower_"+pokename[x].capitalize()+".gif"))
	nameX += prevLen + math.ceil(Letters[x].getWidth()/2.0)
	prevLen = + math.floor(Letters[x].getWidth()/2.0)
	layerOver(Letters[x], output, [nameX,1], [0,0,0])
	Letters[x].move(nameX-36,0)
	#Letters[x].draw(win)

# output.draw(win)

for x in range(3):
	Numbers.append(Image(Point(15+(x*6),8), "Text/Number_"+pokenum[x]+".gif"))
	layerOver(Numbers[x], output, [12+(x*6),3], [0,0,0])
	#Numbers[x].draw(win)

output.save(outputAs)

# win.getMouse()
