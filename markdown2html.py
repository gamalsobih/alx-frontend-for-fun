#!/usr/bin/python3
'''
Write a script markdown2html.py that takes 2 arguments:
First argument is the name of the Markdown file.
Second argument is the output file name.
'''

import sys
import os.path

'''
Handle heading
'''
def heading(line):
    i = 0
    while i < len(line) and line[i] == "#":
        i += 1
    heading_level = i
    heading_content = line[i:].strip()
    return f"<h{heading_level}>{heading_content}</h{heading_level}>"

'''
Handle unordered list
'''
def ul_handle(line, start):
    content = line[1:].strip()  # Get the content of the list item
    if start == 0:
        return f"<ul>\n<li>{content}</li>"
    elif start == 1:
        return f"<li>{content}</li>"
    elif start == 2:
        return f"<li>{content}</li>\n</ul>"

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    filename_input = sys.argv[1]
    filename_output = sys.argv[2]

    if not os.path.exists(filename_input):
        print(f"Missing {filename_input}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(filename_input, "r") as file:
            with open(filename_output, "w") as output_file:
                start = 0
                for line in file:
                    line = line.rstrip()  # Remove trailing whitespace and newlines
                    if line.startswith("#"):
                        output_file.write(heading(line) + "\n")
                        start = 0  # Reset list handling if heading is found
                    elif line.startswith("-"):
                        if start == 0:  # Starting a new list
                            output_file.write(ul_handle(line, start) + "\n")
                            start = 1
                        elif start == 1:  # Continue existing list
                            output_file.write(ul_handle(line, start) + "\n")
                        # Peek the next line to check if it's not a list item
                        next_line = next(file, '').strip()
                        if not next_line.startswith("-"):
                            output_file.write(ul_handle(line, 2) + "\n")
                            start = 0  # Reset after closing the list
                    else:
                        if start == 1:  # Close the list if there's a non-list line
                            output_file.write("</ul>\n")
                            start = 0
                        output_file.write(line + "\n")  # Write other lines directly

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    sys.exit(0)
