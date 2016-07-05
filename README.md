# Factory

I wrote these scripts to do my work for me.

# Projects

Listed in order from most to least recent.

- [Mindspiders](https://soundcloud.com/mokogobo/mindspiders)
- Circle and Dot (In Progress)
- [Swimming in Colorspace](http://swimming-in-colorspace.tumblr.com/)
- [Colorspace Discrete](http://colorspace-discrete.tumblr.com/)

# Dependencies

The dependencies for **Colorspace Discrete** and **Swimming in Colorspace**:

- scikit-image [Tutorial](http://www.scipy-lectures.org/packages/scikit-image/)

**Pitch_Classifier.py** depends on [Aubio](https://aubio.org/) for pitch level and
duration extraction and [MIDO](https://mido.readthedocs.io/) for synthesizing
MIDI files.

**MIDI_to_Sheet_Music.py** depends on
[Abjad](http://www.projectabjad.org/) and
[LilyPond](http://lilypond.org/index.html) to generate sheet music.

Start by entering:

`python Pitch_To_MIDI.py ./data/mips/44.wav`

**Generate_Speech.py** depends on [pyttsx](https://github.com/parente/pyttsx).

**Monitor_Speech.py** depends on:
[SpeechRecognition](https://pypi.python.org/pypi/SpeechRecognition/)
([GitHub](https://github.com/Uberi/speech_recognition)).

It also depends on pyaudio. I used a workaround to install it described on
[StackExchange](http://stackoverflow.com/questions/33513522/when-installing-pyaudio-pip-cannot-find-portaudio-h-in-usr-local-include).
As suggested by the post, I used the following command:

`pip install --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' pyaudio`

pyaudio depends on [PortAudio](http://portaudio.com/). Instructions for installing
it are [here](http://portaudio.com/docs/v19-doxydocs/compile_mac_coreaudio.html).

I configured multiple speech recognition services. These are PocketSphinx,
[Wit.ai](https://wit.ai/), [IBM Speech to Text](http://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/speech-to-text.html).
Access tokens are required to use these services, with the exceptions of
PocketSphinx and Google. To obtain access tokens, sign up for the corresponding
service on its website.

Google can be used without access tokens because it offers a public service for
testing the functionality. Access tokens can be obtained to access more
functionality offered with the service.

Install PocketSphinx on macOS with `brew install cmu-pocketsphinx`.
PocketSphinx depends on [swig](http://macappstore.org/swig/).

# References

- [Marvin Minsky Stories](https://www.youtube.com/watch?v=xiUuQSCR4h8)
