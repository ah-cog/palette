from PIL import Image, ImageDraw

import pytumblr

import os

# Connect to Tumblr

# Authorization information
consumer_key = 'pA9FeSm9NZR9TyKdKR0SigFE2EXgLirTnKBc4s67LabGL3raoS'
consumer_secret = 'R3TReZ9sA7h04lkJdTskJNBsR4ycZc0jhsCHXAGF2oxOx6MeqZ'
oauth_token = 'qvtcaalyQaoywuwBvqVZ3RYtqWkDqfN1f3lXBNOyjrwi3uJaeX'
oauth_secret = '3eUIJCneaNrBCVx8Nrl55uu8yxgTYQyFlNp7AeTwfBs7wEcYke'

# Authenticate with Tumblr
client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    oauth_token,
    oauth_secret,
)

# Create and upload images

# Tried this size first. Took too long doing serial processing.
# img = Image.new( 'RGB', (2048,2048), "white") # create a new black image
# img = Image.new( 'RGB', (512,512), "white") # create a new black image
img = Image.new( 'RGB', (128,128), "white") # create a new black image
pixels = img.load() # create the pixel map

# for i in range(img.size[0]):    # for every pixel:
#     for j in range(img.size[1]):
#         pixels[i,j] = (i, j, 100) # set the colour accordingly

draw = ImageDraw.Draw(img)
draw.line((0, 0) + img.size, fill=128)
draw.line((0, img.size[1], img.size[0], 0), fill=128)

# Generate rectange image for each color point in RGB color space
for r in range(0, 255):
    for g in range(0, 255):
        for b in range(0, 255):

            # Draw rectangle and save in a file
            draw.rectangle([(0, 0), (img.size[0], img.size[1])], fill=(r, g, b))
            image_filename = "./Colorspace_Indices/" + str(r) + "_" + str(g) + "_" + str(b) + ".png"
            img.save(image_filename, "PNG")

            # Generate tag for Tumblr post
            hex_color_tag = "%02x%02x%02x" % (r, g, b)

            # Generate timestamp (index as seconds since January 1, 1970)
            # TODO:

            # Post to Tumblr
            client.create_photo("colorspace-discrete", state="published", tags=[hex_color_tag], data=image_filename)

            # Print progress
            print "Uploaded to Tumblr (%s, %s, %s)" % (r, g, b)

            # Delete the saved file
            try:
                os.remove(image_filename)
            except OSError:
                pass

del draw

img.show()
