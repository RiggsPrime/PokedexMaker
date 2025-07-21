import os
import re
from PIL import Image

dex_image_size = (100, 116)

def create_image_grid(input_folder, output_file, columns, thumb_size=dex_image_size, padding=5):
    # Get image files
    def extract_number(filename):
        # Extracts the first group of digits found in the filename
        match = re.search(r'\d+', filename)
        return int(match.group()) if match else float('inf')

    image_files = sorted(
        [f for f in os.listdir(input_folder)
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))],
        key=extract_number
    )
    
    if not image_files:
        print("No images found in the folder.")
        return

    # Load and optionally resize all images
    images = [Image.open(os.path.join(input_folder, f)).convert("RGB").resize(thumb_size)
              for f in image_files]
    
    rows = (len(images) + columns - 1) // columns

    # Create new blank image
    grid_width = columns * thumb_size[0] + (columns - 1) * padding
    grid_height = rows * thumb_size[1] + (rows - 1) * padding
    new_im = Image.new('RGB', (grid_width, grid_height), (255, 255, 255))  # White background

    # Paste images
    for index, im in enumerate(images):
        row = index // columns
        col = index % columns
        x = col * (thumb_size[0] + padding)
        y = row * (thumb_size[1] + padding)
        new_im.paste(im, (x, y))

    new_im.save(output_file)
    print(f"Saved grid image as {output_file}")


folder_path = input("Enter path to folder with images: ").strip()
columns = int(input("Enter number of columns: "))
output_path = input("Enter output image filename (e.g., grid.jpg): ").strip()
create_image_grid(folder_path, output_path, columns)
