#!/usr/bin/env python3

import sys
from chords import chords, normalize

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
    all_lines = [construct_fretboard(norm) for _, norm in chords]
    name_line = '   '.join(name.center(6) for name, _ in chords)
    separator_line = '   '.join('------' for _ in chords)
    string_line = '   '.join('EADGBe' for _ in chords)

    print(name_line)
    print(separator_line)
    print(string_line)

    for i in range(len(all_lines[0])):
        print('   '.join(chord[i] for chord in all_lines))

def interactive():
    print("CHORDMAND interactive mode")
    chords = input("Enter chords (separated by spaces): ").split()
    pairs = [(name, normalize(name)) for name in chords]
    print_fretboards(pairs)

def main(argv):
    if (len(argv) == 1) or ("--interactive" in argv):
        interactive()
    else:
        chords = argv[1:]
        pairs = [(name, normalize(name)) for name in chords]
        print_fretboards(pairs)
    return 0


if __name__ == '__main__':
    main(sys.argv)
