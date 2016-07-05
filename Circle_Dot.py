from PIL import Image, ImageDraw # Images

import pytumblr # Tumblr

import pytz, datetime # Time

import os

import random

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
img = Image.new( 'RGB', (2048,2048), "white") # create a new black image
# img = Image.new( 'RGB', (128,128), "white") # create a new black image
pixels = img.load() # create the pixel map

# for i in range(img.size[0]):    # for every pixel:
#     for j in range(img.size[1]):
#         pixels[i,j] = (i, j, 100) # set the colour accordingly

draw = ImageDraw.Draw(img)
draw.line((0, 0) + img.size, fill=128)
draw.line((0, img.size[1], img.size[0], 0), fill=128)

# Generate rectange image for each color point in RGB color space
#
# (0, 72, 34)
# Jan 1st, 1970 12:02:29am
#
for b in range(0, 255):
    for g in range(0, 255):
        for r in range(0, 255):

            # Draw rectangle and save in a file
            draw.rectangle([(0, 0), (img.size[0], img.size[1])], fill=(255, 255, 255))

            rnd = lambda: random.randint(0,255)
            radius = 400
            x_position = random.randint(radius, img.size[0] - (radius))
            y_position = random.randint(radius, img.size[1] - (radius))
            draw.ellipse((x_position-radius, y_position-radius, x_position+radius, y_position+radius), fill=(rnd(),rnd(),rnd()))

            radius = 25
            x_position = (radius / 2.0) + random.randint(0,img.size[0] - (radius))
            y_position = (radius / 2.0) + random.randint(0,img.size[1] - (radius))
            draw.ellipse((x_position-radius, y_position-radius, x_position+radius, y_position+radius), fill=(rnd(),rnd(),rnd()))

            image_filename = "./Circle_And_Dot/" + str(r) + "_" + str(g) + "_" + str(b) + ".png"
            img.save(image_filename, "PNG")

            # Generate timestamp (index as seconds since January 1, 1970)
            # local = pytz.timezone ("America/New_York") # Nearest to Bell Labs in New Jersey
            # local = pytz.timezone ("GMT") # Baseline for UNIX time
            # # naive = datetime.datetime.strptime ("2001-2-3 10:11:12", "%Y-%m-%d %H:%M:%S")
            # naive = datetime.datetime.fromtimestamp(
            #         int("%s" % (r * 255 + g * 255 + b))
            #     ).strftime('%Y-%m-%d %H:%M:%S')
            # naive = datetime.datetime.strptime (naive, "%Y-%m-%d %H:%M:%S")
            # local_dt = local.localize(naive, is_dst=None)
            # utc_dt = local_dt.astimezone (pytz.utc)
            unix_time = datetime.datetime.utcfromtimestamp(r * 255 + g * 255 + b)
            post_time = unix_time.strftime('%Y-%m-%d %H:%M:%S')
            print unix_time
            print post_time
            # print naive

            # Generate tag for Tumblr post
            hex_color_tag = "%02x%02x%02x" % (r, g, b)
#            timestamp_tag = "%s" % (unix_time)


            # Post to Tumblr
#             client.create_photo("circle-and-dot",
#                                 state="published",
# #                                date=post_time,
#                                 tags=[hex_color_tag],
#                                 data=image_filename)

            # Print progress
            print "Uploaded to Tumblr (%s, %s, %s)" % (r, g, b)

        for r in range(0, 255):
            # Delete the saved file
            try:
                os.remove(image_filename)
            except OSError:
                pass

del draw

img.show()
