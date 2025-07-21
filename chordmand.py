#!/usr/bin/env python3

import sys

notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

flat_to_sharp = {
    'Db': 'C#',
    'Eb': 'D#',
    'Gb': 'F#',
    'Ab': 'G#',
    'Bb': 'A#'
}

chords = {
    'C':  "x32010",
    'C#': "x46664",
    'D':  "xx0232",
    'D#': "x68886",
    'E':  "022100",
    'F':  "133211",
    'F#': "244322",
    'G':  "320003",
    'G#': "466544",
    'A':  "x02220",
    'A#': "x13331",
    'B':  "x24442",

    'Cm':  "x35543",
    'C#m': "x46654",
    'Dm':  "xx0231",
    'D#m': "x68876",
    'Em':  "022000",
    'Fm':  "133111",
    'F#m': "244222",
    'Gm':  "355333",
    'G#m': "466444",
    'Am':  "x02210",
    'A#m': "x13321",
    'Bm':  "x24432",
}


def print_fretboard(chord):
    fretboard = [['|' for _ in range(6)] for _ in range(8)]
    pattern = chords[chord]
    for string, fret in enumerate(pattern):
        if fret != '0':
            if fret == 'x':
                for row in fretboard:
                    row[string] = '‡'
            else:
                fretboard[int(fret)-1][string] = '●'
    print(f"\n{chord}")
    print("------")
    print("EADGBe")
    # print("EADGBe")
    for fret in fretboard:
        print(''.join(map(str, fret)))
    print("\n")

def print_fretboards(chords):
    for chord in chords:
        print_fretboard(chord)

def interactive():
    print("CHORDMAND interactive mode!")
    chord = input("Enter a chord: ")
    if 'b' in chord:
        flat = True
        chord = flat_to_sharp[chord]
    print_fretboard(chord)

def main(argv):
    if (len(argv) == 1) or ("--interactive" in argv):
        interactive()
    else:
        chords = argv[1:]
        for chord in chords:
            if 'b' in chord:
                flat = True
                chord = flat_to_sharp[chord]
        print_fretboards(chords)
    return 0


if __name__ == '__main__':
    main(sys.argv)
