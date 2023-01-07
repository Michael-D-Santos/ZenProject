import os
import spacy

# Load a pre-trained natural language processing model using spacy
nlp = spacy.load("en_core_web_sm")

def generate_themes(directory):
    themes = {}

    for file in os.listdir(directory):
        with open(os.path.join(directory, file), "r") as f:
            contents = f.read()
            # Extract themes from the text using spacy
            doc = nlp(contents)
            for entity in doc.ents:
                theme = entity.text
                if theme in themes:
                    themes[theme] += 1
                else:
                    themes[theme] = 1

    return themes

# Call the function and pass the directory path as an argument
themes = generate_themes(".")

# Write the themes and their count to a text file, sorted by count in descending order
with open("themes.txt", "w") as f:
    for theme, count in sorted(themes.items(), key=lambda x: x[1], reverse=True):
        f.write(f'{theme}: {count}\n')