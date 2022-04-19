# Pokedex Maker

The PokedexMaker is a special tool I've made to make small boxes used for Fakemon Showcase.

## How to use the program
1. Make sure you have installed Python3.
2. Get a 64x64 sprite of the Pokemon.
3. Set the background/transparency color to rgb(153,0,0). (The transparency color can be customized see: Customization section below).
4. For macs, convert the file to .gif (Simply renaming it will not work).
5. Move the file to the folder with the python file or subfolder of that.
6. Open Command Prompt (Windows)/Terminal (Mac).
7. Navigate to your file in Command Prompt/Terminal. Easiest way would be to type `cd ` and then paste the folder name. (e.g. `cd C:\Users\User\Downloads\PokedexMaker`)
8. Run the file with `py PokedexMaker.py` or `python PokedexMaker.py` depending on what your system uses.
9. The file will ask for the following info:
	1. **input file name**: type `filename.format` if the file is in the same folder as the program. If it is a subfolder, type `SubfolderName/filename.format`.
	2. **input sprite Y-offset (leave blank for 0)**: For how many pixels down you want to shift your sprite. Negative numbers shifts the sprite up.
	3. **input type(s) seperated by space**: Also ensure they are capitalized. For adding custom types, see the Customization section below.
	4. **input name**: Inout the Name of the Fakemon. As Romhacks are limited to 10 characters, the display for the most part, is as well. Numbers and special characters currently don't work.
	5. **input (3-digit) pokedex number**: Self Explanitory. Must be 3 numbers.
	6. **output file name**: Same format as input file name.
10. Click the preview window to close.
11. If you wish to make another in the same session, skip to step 8.

## Customization
* **Change the Transparency Color**: Open PokedexMaker.py in a text editor and replace every instance of [153,0,0] with [r,g,b] of your desired transparency color.
* **Add a New Type**:  Open PokedexMaker.py in a text editor and navigate to the list called "typesColors" add a comma after `"Unknown": [138, 216, 192]` (or the last item on the list if you've added one already). After that, on a new line add `"TypeName": [r, g, b]` of your desired Type Name and rgb values of your background colors respectively. Do the same with the "baseColors" list for the color of the circular platform below the Pokemon. Finally, for the type graphic, convert the image to a gif move it to the Text subfolder. It should be names `Type_TypeName.gif`.