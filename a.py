from PIL import Image

# Open the image file
image = Image.open("beautiful_woman.jpg")

# Resize the image to a smaller size to reduce the number of ASCII characters needed
image = image.resize((80, 80))

# Convert the image to grayscale and get the pixel values
pixels = image.convert('L').load()

# Define the ASCII characters to use and the corresponding color values
ascii_chars = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']
color_values = [0, 32, 64, 96, 128, 160, 192, 224, 255]

# Generate the color mapping by mapping pixel values to ASCII characters
color_mapping = {}
for i in range(80):
    for j in range(80):
        pixel_value = pixels[i, j]
        color_index = int((pixel_value / 256) * len(color_values))
        color_mapping[(i, j)] = ascii_chars[color_index]

# Write the color mapping to a text file
with open("color_info.txt", "w") as f:
    for i in range(80):
        for j in range(80):
            f.write(color_mapping[(i, j)])
        f.write('\n')
