import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# create empty lists to store the words and frequencies
words = []
freqs = []

# open the text file and read the data
with open("word_frequencies.txt", "r") as f:
    for line in f:
        # split the line into the word and frequency
        word, freq = line.strip().split(": ")
        # add the word and frequency to the lists
        words.append(word)
        freqs.append(int(freq))

# create a dataframe from the list of words and frequencies
df = pd.DataFrame({"words": words, "freqs": freqs})

# create the bar plot
sns.barplot(y="words", x="freqs", data=df)
plt.yticks(fontsize=5)

# set the x-axis labels to be vertical
plt.xticks(rotation=90)

plt.gcf().set_size_inches(8, 6)

# show the plot
plt.savefig("art.png", dpi=400)
