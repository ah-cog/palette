from pydub import AudioSegment
from pydub.silence import split_on_silence

import math

filename = "./data/minsky/audio/marvin-minsky-stories.wav"
segment_length_seconds = 30

# Open the video file with the specified filename
print "Opening video file...",
sound = AudioSegment.from_file(filename)
print "Done."

ten_seconds = segment_length_seconds * 1000
segment_count = int(math.ceil(len(sound) / (1.0 * ten_seconds)))
# first_10_seconds = sound[:ten_seconds]

for i in range(0, segment_count):

    start = i * ten_seconds
    end = (i + 1) * ten_seconds

    print "Extracting seconds " + str(start) + " to " + str(end) + " of " + str((len(sound) / 1000.0)) + " seconds (segments: " + str(segment_count) + ")...",
    segment = sound[start:end]
    print "Done."

    print "Saving to file...",
    segment.export("./data/minsky/clips/{0}.wav".format(i), format="wav")
    print "Done."


# chunks = split_on_silence(sound,
#     # must be silent for at least half a second
#     min_silence_len=500,
#
#     # consider it silent if quieter than -16 dBFS
#     silence_thresh=-16
# )
#
# for i, chunk in enumerate(chunks):
#     chunk.export("/path/to/ouput/dir/chunk{0}.wav".format(i), format="wav")
