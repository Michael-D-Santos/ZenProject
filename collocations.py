import os
import re
from collections import Counter
from nltk import collocations

# Set the directory containing the text files
directory = "."

# Initialize a list to store the collocations
collocations_list = []

# Iterate through each text file in the directory
for file in os.listdir(directory):
    if file.endswith(".txt"):
        # Open the file and read its contents
        with open(os.path.join(directory, file), "r") as f:
            text = f.read()

        # Remove all punctuation and marks from the text
        text = re.sub(r'[^\w\s]', '', text)

        # Split the text into a list of tokens (words and punctuation)
        tokens = text.split()

        # Use the NLTK's collocations module to find bigrams in the text
        bigram_finder = collocations.BigramCollocationFinder.from_words(tokens)

        # Use the bigram finder to generate a list of bigrams and their frequencies
        bigrams = bigram_finder.ngram_fd.items()

        # Add the bigrams and their frequencies to the collocations list
        collocations_list.extend(bigrams)

# Write the collocations to a text file
with open("collocations.txt", "w") as f:
  f.write(str(collocations_list))
