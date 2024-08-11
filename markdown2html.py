#!/usr/bin/python3
''' Write a script markdown2html.py that takes an argument 2 strings:
    First argument is the name of the Markdown file
    Second argument is the output file name
'''

import sys
import os.path
import re
import hashlib
if __name__=='__main__' :
    
    if len(sys.argv) !=3 :
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    filname_input=sys.argv[1]
    filename_outbut=sys.argv[2]
    if not os.path.exists(filname_input) :
        print(f"Missing {filname_input}",file=sys.stderr )
        sys.exit(1)
    else:
        print("")

