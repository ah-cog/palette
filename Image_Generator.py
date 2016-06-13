from PIL import Image, ImageDraw

img = Image.new( 'RGB', (2048,2048), "white") # create a new black image
pixels = img.load() # create the pixel map

# for i in range(img.size[0]):    # for every pixel:
#     for j in range(img.size[1]):
#         pixels[i,j] = (i, j, 100) # set the colour accordingly

draw = ImageDraw.Draw(img)
draw.line((0, 0) + img.size, fill=128)
draw.line((0, img.size[1], img.size[0], 0), fill=128)

# Generate rectange image for each color point in RGB color space
for r in range(255):
    for g in range(255):
        for b in range(255):
            draw.rectangle([(0, 0), (img.size[0], img.size[1])], fill=(r, g, b))
            img.save("./Colorspace_Indices/" + str(r) + "_" + str(g) + "_" + str(b) + ".png", "PNG")

del draw

img.show()
