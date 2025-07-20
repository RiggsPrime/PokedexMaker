from graphics import *
import math

from PIL import Image as Image_PIL

pokeimg = input("input file name: ")
#dex = input("box style: ")
off = input("input sprite Y-offset (leave blank for 0): ")
offset = 0
if off != "":
	offset = int(off)
types = input("input type(s) seperated by space: ").split(" ")
pokename = input("input name: ")
pokenum = input("input (3-digit) pokedex number: ")
outputAs = input("output file name: ")

typesColors = {
	"Normal": [232,232,216],
	"Fire": [254,209,180],
	"Water": [200, 216, 248],
	"Grass": [216, 240, 192],
	"Electric": [255,253,202],
	"Ice": [192, 248, 248],
	"Psychic": [248, 152, 216],
	"Fighting": [248, 168, 168],
	"Poison": [235, 194, 245],
	"Bug": [216, 224, 200],
	"Ground": [227, 217, 157],
	"Rock": [216, 200, 144],
	"Steel": [219, 219, 219],
	"Ghost": [208, 176, 248],
	"Dark": [184, 176, 168],
	"Dragon": [170, 194, 244],
	"Fairy": [255, 212, 255],
	"Flying": [168, 225, 242],
	"Unknown": [138, 216, 192]
}

baseColors = {
	"Normal": [184,184,168],
	"Fire": [248, 144, 48],
	"Water": [146, 202, 248],
	"Grass": [144, 232, 128],
	"Electric": [224,224,0],
	"Ice": [48, 216, 208],
	"Psychic": [248, 56, 168],
	"Fighting": [248, 112, 112],
	"Poison": [224, 144, 248],
	"Bug": [160, 200, 136],
	"Ground": [213, 197, 108],
	"Rock": [200, 160, 72],
	"Steel": [184, 184, 208],
	"Ghost": [168, 112, 248],
	"Dark": [144, 136, 136],
	"Dragon": [48, 112, 192],
	"Fairy": [255, 151, 226],
	"Flying": [122, 197, 205],
	"Unknown": [40, 174, 132]
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
