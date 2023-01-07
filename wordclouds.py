# Import the necessary libraries
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from matplotlib.colors import ListedColormap

# Create a list of words and their frequencies
words = []

# Convert the list of tuples into a dictionary
word_dict = dict(words)

# Create the wordcloud object
wordcloud = WordCloud(width=3840, height=2160, background_color="white")

# Generate the wordcloud
wordcloud.generate_from_frequencies(word_dict)

# Plot the wordcloud
plt.figure(figsize=(8,8))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()