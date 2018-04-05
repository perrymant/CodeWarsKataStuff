notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def chords(root):
  rootIndex = notes.index(root)
  major = [notes[rootIndex], notes[(rootIndex+4)%12], notes[(rootIndex+7)%12]]
  minor = [notes[rootIndex], notes[(rootIndex+3)%12], notes[(rootIndex+7)%12]]
  return [major, minor]
