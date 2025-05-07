from pedalboard import Pedalboard, Reverb
from pedalboard.io import AudioFile
import soundfile as sf
import pyrubberband as pyrb

y , sr = sf.read('/Users/haziq/Desktop/SlowedNReverbify/test1.mp3')
y_stretch = pyrb.time_stretch(y, sr, 0.85)
sf.write("Slow.wav", y_stretch, sr, format='wav')
f, fa = sf.read('/Users/haziq/Desktop/SlowedNReverbify/final.wav')
f_shift = pyrb.pitch_shift(f, fa, -2)
sf.write("PitchShifted.wav", f_shift, sr, format='wav')
print("Done with slow")


reverb = Pedalboard([Reverb(room_size=0.1)])

with AudioFile('/Users/haziq/Desktop/SlowedNReverbify/PitchShifted.wav') as f:
    with AudioFile('/Users/haziq/Desktop/SlowedNReverbify/final.mp3', 'w', f.samplerate, f.num_channels) as o:
   
    # Read one second of audio at a time, until the file is empty:
        while f.tell() < f.frames:
            chunk = f.read(int(f.samplerate))

            reverbed = reverb(chunk, f.samplerate, reset=False)
            o.write(reverbed)
            # pedalboard.MP3Compressor()

    print("Done with Reverb")
