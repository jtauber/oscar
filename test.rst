
Convert letter+modifer pitch to numerical value based on circle-of-fifths:

>>> from pitch import value
>>> value("C")
1
>>> value("E")
5
>>> value("F#")
7
>>> value("Bb")
-1
>>> value("Abb")
-10
>>> value("Gx")
16

Convert circle-of-fifths-based numerical pitch to letter+modifier string:

>>> from pitch import name
>>> name(1)
'C'
>>> name(5)
'E'
>>> name(7)
'F#'
>>> name(-1)
'Bb'
>>> name(-10)
'Abb'
>>> name(16)
'Gx'

Get the notes in the D Locrian scale:

>>> import modes

>>> def scale(tonic, mode): return [name(value(tonic) + o) for o in mode]

>>> print scale("D", modes.LOCRIAN)
['D', 'Eb', 'F', 'G', 'Ab', 'Bb', 'C']