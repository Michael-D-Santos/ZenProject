#INTENDED TO BE RAN IN ZEN DIRECTORY
import nltk
import spacy
import os

# Set up NLTK for collocation analysis and theme identification
nltk.download("collocations")
nltk.download("punkt")
nltk.download("stopwords")

# Set up spaCy for named entity recognition
nlp = spacy.load("en_core_web_sm")

# Iterate over the .txt files in the directory
for file in os.listdir("ZenDirectoryGoesHere"):
    if file.endswith(".txt"):
        # Read the text from the file
        with open(file, 'r') as f:
            text = f.read()
        
        # Pre-process the text for collocation analysis and theme identification
        tokens = nltk.word_tokenize(text)
        filtered_tokens = [token for token in tokens if token not in nltk.corpus.stopwords.words("english")]
        bigrams = nltk.bigrams(filtered_tokens)
        finder = nltk.BigramCollocationFinder.from_words(bigrams)
        finder.apply_freq_filter(3)
        collocations = finder.nbest(nltk.collocations.BigramAssocMeasures().pmi, 10)
        themes = nltk.Text(filtered_tokens).collocations()
        
        # Perform named entity recognition using spaCy
        doc = nlp(text)
        entities = [(entity.text, entity.label_) for entity in doc.ents]
        
        # Write the results of the analysis to a .txt file
        with open("entities.txt", "w") as f:
            f.write(str(entities))
