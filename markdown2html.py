#!/usr/bin/python3
'''
Write a script markdown2html.py that takes an argument 2 strings:
First argument is the name of the Markdown file
Second argument is the output file name
'''

import sys
import os.path

def heading(line):
    i = 0
    while i < len(line) and line[i] == "#":
        i += 1
    heading_level = i
    heading_content = line[i:].strip()
    return f"<h{heading_level}>{heading_content}</h{heading_level}>"

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    filname_input = sys.argv[1]
    filename_output = sys.argv[2]

    if not os.path.exists(filname_input):
        print(f"Missing {filname_input}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(filname_input, "r") as file:
            with open(filename_output, "w") as output_file:
                for line in file:
                    if line.strip().startswith("#"):
                        output_file.write(heading(line) + "\n")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    sys.exit(0)
