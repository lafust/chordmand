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


def construct_fretboard(chord):
    fretboard = [['|' for _ in range(6)] for _ in range(8)]
    pattern = chords[chord]
    for string, fret in enumerate(pattern):
        if fret != '0':
            if fret == 'x':
                for row in fretboard:
                    row[string] = '‡'
            else:
                fretboard[int(fret)-1][string] = '●'
    lines = [''.join(row) for row in fretboard]
    return lines

def print_fretboards(chords):
    all_lines = [construct_fretboard(chord) for chord in chords]
    name_line = '   '.join(chord.center(6) for chord in chords)
    separator_line = '   '.join('------' for _ in chords)
    string_line = '   '.join('EADGBe' for _ in chords)

    print(name_line)
    print(separator_line)
    print(string_line)

    for i in range(len(all_lines[0])):
        print('   '.join(chord[i] for chord in all_lines))

def interactive():
    print("CHORDMAND interactive mode")
    chords = input("Enter chords (separated by spaces): ")
    chords = chords.split()
    for chord in chords:
        if 'b' in chord:
            flat = True
            chord = flat_to_sharp[chord]
    print_fretboards(chords)

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
