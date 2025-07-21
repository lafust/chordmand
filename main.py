#!/usr/bin/env python3

"""
Chordmand Line Interface - a CLI tool to display guitar chord charts
-----------------------------------------------------------------------
Usage: python main.py [CHORDS...] [--interactive]

Positional arguments:
  CHORDS         One or more chord names (e.g. C Gb Am D# F#m)
                 Only uppercase chord names are supported.

Optional arguments:
  --interactive  Start an interactive session (ignores other arguments)

Examples:
  python main.py Em G D A
  python main.py --interactive
"""

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


def print_fretboards(pairs):
    all_lines = [construct_fretboard(norm) for _, norm in pairs]
    name_line = '   '.join(name.center(6) for name, _ in pairs)
    separator_line = '   '.join('------' for _ in pairs)
    string_line = '   '.join('EADGBe' for _ in pairs)

    print("\n")
    print(name_line)
    print(separator_line)
    print(string_line)
    for i in range(len(all_lines[0])):
        print('   '.join(chord[i] for chord in all_lines))
    print("\n")


def interactive():
    print("CHORDMAND interactive mode (type 'exit' to exit)")
    while True:
        input_chords = input("Enter chords (separated by spaces): ").split()
        if "exit" in input_chords:
            return
        pairs = [(name, normalize(name)) for name in input_chords]
        invalid = [name for name, norm in pairs if norm not in chords]
        if invalid:
            print(f"Unknown chords: {', '.join(invalid)}")
            return
        print_fretboards(pairs)


def main(argv):
    if "--help" in argv or "-h" in argv:
        print(__doc__)
    elif (len(argv) == 1) or ("--interactive" in argv):
        interactive()
    else:
        input_chords = argv[1:]
        pairs = [(name, normalize(name)) for name in input_chords]
        invalid = [name for name, norm in pairs if norm not in chords]
        if invalid:
            print(f"Unknown chords: {', '.join(invalid)}")
            return
        print_fretboards(pairs)
    return 0


if __name__ == '__main__':
    main(sys.argv)
