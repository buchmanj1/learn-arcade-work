import re


# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def main():
    """ Read in lines from a file """

    # Open the file for reading, and store a pointer to it in the new
    # variable "file"
    my_file = open("dictionary.txt")

    # Create an empty list to store our names
    dictionary_list = []

    # Loop through each line in the file like a list
    for line in my_file:
        # Remove any line feed, carriage returns or spaces at the end of the line
        line = line.strip()

        # Add the name to the list
        dictionary_list.append(line)

    my_file.close()

    my_file = open("AliceInWonderLand200.txt")

    for line in my_file:
        word_list = split_line(line)
        for word in word_list:
            # --- Linear search
            key = word.upper()

            # Start at the beginning of the list
            current_list_position = 0

            # Loop until you reach the end of the list, or the value at the
            # current position is equal to the key
            while current_list_position < len(word_list) and word_list[current_list_position] != key:
                # Advance to the next item in the list
                current_list_position += 1

            if current_list_position < len(word_list):
                print(key, "is at position", current_list_position)

    my_file.close()



main()
