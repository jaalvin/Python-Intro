#A script that reads a text file and counts how many lines and words are in the file

def count_lines_and_words(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
        print(f"Number of lines: {num_lines}")
        print(f"Number of words: {num_words}")
    except FileNotFoundError:
        print("The file was not found.")

# Replace 'yourfile.txt' with the path to your text file
count_lines_and_words('yourfile.txt')
