# Reads lines from .txt files in a folder and copies them into a single file.

import os

output_file_name = "./data/minsky/transcripts/transcript.txt"
segment_count = 689

# Delete the output file if it already exists
try:
    os.remove(output_file_name)
except OSError:
    pass

# Create the output file
output_file = open(output_file_name, "a")

for i in range(0, segment_count):

    # Compute name of source file to read
    segment_name = "{0}".format(i)
    input_file_name = "./data/minsky/transcripts/" + segment_name + ".txt"

    # Read lines from source file and write them to the destination file
    if os.path.isfile(input_file_name):
        with open(input_file_name, "r") as input_file:
            for line in input_file:
                output_file.write("%s\n" % line)
    else:
        # If the input file doesn't exist, write an empty line
        output_file.write("\n")

# Close output file
output_file.close()
