import time
import sounddevice as sd

duration=5
myrecording = sd.rec(int(duration * 44100),samplerate=44100, channels=1, dtype='int16')

sd.wait()

time.sleep(20)

print('I am playing now')

sd.play(myrecording)

sd.wait()

print('Done')
