from pathlib import Path
from typing import List


def tail(n: int, filepath: Path):
    """
    Works similarly to Unix's "tail -n" command:
    - Read in the file ("filepath").
    - Parse it into a list of lines, stripping trailing newlines.
    - Return the last "n" lines.
    """

    with open(filepath) as fileObject:
        lines = fileObject.readlines()

    # Use slicing to return the last "n" lines
    result = [line.rstrip() for line in lines[-abs(n):]]

    #return result[-n:]
    return '\n'.join(result)


if __name__ == '__main__':
    # This allows the script to be run from the command line with an argument
    import sys
    print(tail(int(sys.argv[1]), sys.argv[2]))

