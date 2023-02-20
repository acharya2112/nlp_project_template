from typing import List
from nltk.stem import WordNetLemmatizer


class Lemmatizer:
    def __init__(self, lemmatizer_instance=WordNetLemmatizer()):
        self.lemmatizer = lemmatizer_instance

    def process(self, text: List[str]) -> List[str]:
        """Return text with lemmatizer applied.

        Parameters:
            text (List[str]): Input tokenized text.

        Returns:
            lemmatized_text (List[str]): Returns input text with lemmatization applied.
        """
        lemmatized_text = [self.lemmatizer.lemmatize(token) for token in text]
        return lemmatized_text
