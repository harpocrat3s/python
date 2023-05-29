def wc(file_):
    """
    This function accepts an absolute file path/name as input,
    then computes the number of lines, words and characters contained in the file.
    It returns a string of these counts along with the file name,
    in the same format as the wc command on Mac OS. Example:
    "       4      69     448 test.txt"
    """

    # Initialize word and character counters
    words = 0
    characters = 0

    # Open the file and read its contents into a list of strings
    with open(file_) as fileObject:
        lines = fileObject.readlines()

    # Count the number of lines, words, and characters in the file
    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    num_chars = sum(len(line) for line in lines)

    # Format the output string with the counts and file name
    result = f"{str(num_lines).rstrip().rjust(8)}{str(num_words).rjust(8)}{str(num_chars).rjust(8)} {file_}"

    return result


if __name__ == '__main__':
    # This allows the script to be run from the command line with an argument
    import sys
    print(wc(sys.argv[1]))
