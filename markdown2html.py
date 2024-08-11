#!/usr/bin/python3

"""
markdown2html.py: A script to convert a Markdown file to an HTML file.

Usage:
    ./markdown2html.py <input_markdown_file> <output_html_file>

Arguments:
    input_markdown_file    The path to the input Markdown file.
    output_html_file       The path to the output HTML file.

If the number of arguments is less than 2:
    Print "Usage: ./markdown2html.py README.md README.html" in STDERR and exit with status 1.

If the Markdown file doesn’t exist:
    Print "Missing <filename>" in STDERR and exit with status 1.

If successful:
    Print nothing and exit with status 0.
"""

import sys
import os
import markdown

def markdown_to_html(input_file, output_file):
    """
    Converts a Markdown file to an HTML file.
    
    Parameters:
        input_file (str): The path to the input Markdown file.
        output_file (str): The path to the output HTML file.
    
    Returns:
        None
    """
    try:
        # Read the Markdown file
        with open(input_file, 'r') as md_file:
            markdown_content = md_file.read()

        # Convert Markdown to HTML
        html_content = markdown.markdown(markdown_content)

        # Write the HTML content to the output file
        with open(output_file, 'w') as html_file:
            html_file.write(html_content)

    except FileNotFoundError:
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    # Check if the input file exists
    if not os.path.exists(input_filename):
        print(f"Missing {input_filename}", file=sys.stderr)
        sys.exit(1)

    markdown_to_html(input_filename, output_filename)
    sys.exit(0)
