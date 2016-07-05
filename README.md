# Factory

I wrote these scripts to do my work for me.

# Projects

Listed in order from most to least recent.

- [Mindspiders](https://soundcloud.com/mokogobo/mindspiders)
- Circle and Dot (In Progress)
- [Swimming in Colorspace](http://swimming-in-colorspace.tumblr.com/)
- [Colorspace Discrete](http://colorspace-discrete.tumblr.com/)

# Dependencies

**Colorspace_Discrete.py** and **Swimming_In_Colorspace.py** depend on
[scikit-image](http://scikit-image.org/). I got up and running quickly
with the help of Emmanuelle Gouillart's
[image processing tutorial](http://www.scipy-lectures.org/packages/scikit-image/)
on [Scipy Lecture Notes](http://www.scipy-lectures.org/index.html).

**Pitch_Classifier.py** detects the pitch and pitch duration, stores the
start time of detected pitch, and records the confidence of  
of each detection. It depends on [Aubio](https://aubio.org/) for pitch level and
duration extraction and [MIDO](https://mido.readthedocs.io/) for synthesizing
MIDI files.

**Pitch_To_MIDI.py** generates a MIDI file (.mid) for the text file of pitches,
etc. produced by Pitch_Classifier.py.

To convert run it:

```
python Pitch_To_MIDI.py ./Content/minsky/clips/44.wav
```

**MIDI_to_Sheet_Music.py** generates the printable sheet music from a
given MIDI file (.mid). The script depends on the
[Abjad](http://www.projectabjad.org/) Python library to generate the music
notation and the [LilyPond](http://lilypond.org/index.html) LaTeX
package to generate the sheet music documents (.pdf).

**Generate_Speech.py** depends on [pyttsx](https://github.com/parente/pyttsx).

**Monitor_Speech.py** depends on:
[SpeechRecognition](https://pypi.python.org/pypi/SpeechRecognition/)
([GitHub](https://github.com/Uberi/speech_recognition)).

It also depends on pyaudio. I used a workaround to install it described on
[StackExchange](http://stackoverflow.com/questions/33513522/when-installing-pyaudio-pip-cannot-find-portaudio-h-in-usr-local-include).
As suggested by the post, I used the following command:

````
pip install --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' pyaudio
```

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
