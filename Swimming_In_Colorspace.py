import numpy
from PIL import Image
import random
import pytumblr # Tumblr
import pytz, datetime # Time
import os
import time, threading
import math

# TODO:
# - Get post IDs and dates for blog
# - Delete post ID range
# - Delete posts after date
# - Edit tags for post

# Connect to Tumblr
tumblr_title = "swimming-in-colorspace"
tumblr_post_frequency = 2 # seconds

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

output_image_filename = "./data/Voronoi.png"
output_image_width = 2048
output_image_height = 2048

def voronoi(points,shape=(output_image_width,output_image_height)):
    depth_map = numpy.ones(shape,numpy.float)*1e308
    color_map = numpy.zeros(shape,numpy.int)

    def hypot(X,Y):
        return (X-x)**2 + (Y-y)**2

    for i,(x,y) in enumerate(points):
        paraboloid = numpy.fromfunction(hypot,shape)
        color_map = numpy.where(paraboloid < depth_map,i+1,color_map)
        depth_map = numpy.where(paraboloid < depth_map,paraboloid,depth_map)

    # for (x,y) in points:
    #     color_map[x-1:x+2,y-1:y+2] = 0

    return color_map

color_palette = []
def draw_map(color_map):
    shape = color_map.shape

    # palette = numpy.array(color_palette)
    palette = numpy.array(color_palette)

    color_map = numpy.transpose(color_map)
    output_image_pixels = numpy.empty(color_map.shape + (4,), numpy.int8)

    output_image_pixels[:,:,3] = (palette[color_map]>>0)  & 0xFF
    output_image_pixels[:,:,2] = (palette[color_map]>>8)  & 0xFF
    output_image_pixels[:,:,1] = (palette[color_map]>>16) & 0xFF
    output_image_pixels[:,:,0] = (palette[color_map]>>24) & 0xFF

    image = Image.frombytes("RGBA", shape, output_image_pixels)
    image.save(output_image_filename)

up_step_size = 0.08
down_step_size = 0.1
step_direction = -1
step_size = up_step_size

iteration_count = 0
point_count_input = -1

def execute():
    global point_count_input
    global step_direction
    global step_size
    global up_step_size
    global down_step_size
    global iteration_count

    # Print iteration information
    print "Iteration %s" % iteration_count

    # Update step direction (up or down)
    if step_direction == 1 and point_count_input > 1.0:
        step_size = down_step_size # downstep
        step_direction = step_direction * -1
    elif step_direction == -1 and point_count_input < abs(down_step_size):
        point_count_input = 0.27
        step_size = up_step_size # upstep
        step_direction = step_direction * -1

    # Generate number of points
    print "Generating number of cells",
    # (no. 2) number_of_cells = range(0,random.randint(2,random.randint(3,8)) + 1)
    #point_count_input = point_count_input + 0.01
    #number_of_cells =range(0,int(200 * abs(math.sin(point_count_input)) + 2))
    point_count_input = point_count_input + step_direction * step_size
    number_of_cells = range(0,int(math.pow(500, point_count_input)))
    print "(Input: %s, Step: %s, Count: %s)" % (point_count_input, step_direction * step_size, len(number_of_cells))

    r = lambda: random.randint(50,255)

    # Generate color palette (random)
    print "Generating color palette"
    del color_palette[:]
    for i in number_of_cells:
        hex_color_string = '0x%02X%02X%02XFF' % (r(),r(), r())
        color = int(hex_color_string, 0)
        color_palette.append(color)

    # Generate list of points for vertices of Voronoi diagram
    points = []
    for i in range(0, len(number_of_cells) - 1):
        points.append([random.randint(0, output_image_width), random.randint(0,output_image_height)])

    # Generate Voronoi diagram with color palette
    draw_map(voronoi(points))
    # draw_map(voronoi(([randint(2048,2048),randint(2048,2048)],[randint(2048,2048),randint(2048,2048)],[randint(2048,2048),randint(2048,2048)],[randint(2048,2048),randint(2048,2048)],[randint(2048,2048),randint(2048,2048)])))

    # Post to Tumblr
    client.create_photo(tumblr_title,
                        state="published",
                        # date=post_time,
                        # tags=[hex_color_tag],
                        data=output_image_filename)
    print "Created Tumblr post"

    # Print progress
    print "Uploaded image to Tumblr\n"

    iteration_count = iteration_count + 1

    threading.Timer(tumblr_post_frequency, execute).start()

execute()

if __name__ == '__main__':
    point_count_input = 0.00
    execute()
