Oscar
=====


Numerical Pitch values
----------------------

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

Modes
-----

Get the notes in the D Locrian scale:

>>> import modes

>>> def scale(tonic, mode): return [name(value(tonic) + o) for o in mode]

>>> print scale("D", modes.LOCRIAN)
['D', 'Eb', 'F', 'G', 'Ab', 'Bb', 'C']

Or C Lydian:

>>> print scale("C", modes.LYDIAN)
['C', 'D', 'E', 'F#', 'G', 'A', 'B']

The modes are lists of circle-of-fifth intervals from the tonic:

>>> modes.LYDIAN
[0, 2, 4, 6, 1, 3, 5]

>>> modes.IONIAN
[0, 2, 4, -1, 1, 3, 5]

>>> modes.MIXOLYDIAN
[0, 2, 4, -1, 1, 3, -2]

>>> modes.DORIAN
[0, 2, -3, -1, 1, 3, -2]

>>> modes.AEOLIAN
[0, 2, -3, -1, 1, -4, -2]

>>> modes.PHRYGIAN
[0, -5, -3, -1, 1, -4, -2]

>>> modes.LOCRIAN
[0, -5, -3, -1, -6, -4, -2]


Intervals
---------

>>> def interval_above_C(pitch): return value(pitch) - value("C")

Perfect
~~~~~~~

>>> interval_above_C("F")
-1

>>> interval_above_C("C")
0

>>> interval_above_C("G")
1

Major
~~~~~

>>> interval_above_C("D")
2

>>> interval_above_C("A")
3

>>> interval_above_C("E")
4

>>> interval_above_C("B")
5

Minor
~~~~~

>>> interval_above_C("Db")
-5

>>> interval_above_C("Ab")
-4

>>> interval_above_C("Eb")
-3

>>> interval_above_C("Bb")
-2


Augmented
~~~~~~~~~

>>> interval_above_C("F#")
6

>>> interval_above_C("C#")
7

>>> interval_above_C("G#")
8

>>> interval_above_C("D#")
9

>>> interval_above_C("A#")
10

>>> interval_above_C("E#")
11

>>> interval_above_C("B#")
12

Diminished
~~~~~~~~~~

>>> interval_above_C("Dbb")
-12

>>> interval_above_C("Abb")
-11

>>> interval_above_C("Ebb")
-10

>>> interval_above_C("Bbb")
-9

>>> interval_above_C("Fb")
-8

>>> interval_above_C("Cb")
-7

>>> interval_above_C("Gb")
-6
