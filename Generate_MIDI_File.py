from mido.midifiles import MidiTrack, MidiFile
import mido

with MidiFile() as mid:
    track = MidiTrack()
    mid.tracks.append(track)

    track.append(mido.Message('program_change', program=12, time=0))

    # Note
    track.append(mido.Message('note_on', note=64, velocity=64, time=32))
    track.append(mido.Message('note_off', note=64, velocity=127, time=1000))

    track.append(mido.Message('note_on', note=64, velocity=64, time=32))
    track.append(mido.Message('note_off', note=64, velocity=127, time=32))
    track.append(mido.Message('note_on', note=64, velocity=64, time=32))
    track.append(mido.Message('note_off', note=64, velocity=127, time=32))
    track.append(mido.Message('note_on', note=64, velocity=64, time=32))
    track.append(mido.Message('note_off', note=64, velocity=127, time=32))
    track.append(mido.Message('note_on', note=64, velocity=64, time=32))
    track.append(mido.Message('note_off', note=64, velocity=127, time=32))
    track.append(mido.Message('note_on', note=64, velocity=64, time=32))
    track.append(mido.Message('note_off', note=64, velocity=127, time=32))
    track.append(mido.Message('note_on', note=64, velocity=64, time=32))
    track.append(mido.Message('note_off', note=64, velocity=127, time=1000))

    # Pause
    track.append(mido.Message('note_on', note=64, velocity=64, time=32))
    track.append(mido.Message('note_off', note=64, velocity=127, time=32))

    mid.save('new_song.mid')
