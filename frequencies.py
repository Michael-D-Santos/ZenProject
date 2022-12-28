import os
import string
from collections import Counter

# Set the directory path
directory = "ZenDirectoryGoesHere"

# Initialize a list to store the words from all text files
all_words = []

# Read the list of stop words from its proper location
with open("stop_words.txt", "r") as f:
    stop_words = f.read().split()

# Iterate over the files in the Zen directory
for filename in os.listdir(directory):
    # Only process text files
    if filename.endswith(".txt"):
        # Open the text file and read the contents
        with open(os.path.join(directory, filename), "r") as f:
            for line in f:
                # Ignore lines that end in a number, as these usually just contain the title
                if not line[-1].isdigit():
                    # Split the line into a list of words and add them to the list of all words
                    all_words.extend(word.strip(string.punctuation).lower() for word in line.split() if word.strip(string.punctuation).lower() not in stop_words)

# Count the frequency of each word using the Counter class
word_counts = Counter(all_words)

# Open the output file and write the word frequencies to it
with open("word_frequencies.txt", "w") as f:
    for word, count in word_counts.most_common():
        f.write(f"{word}: {count}\n")