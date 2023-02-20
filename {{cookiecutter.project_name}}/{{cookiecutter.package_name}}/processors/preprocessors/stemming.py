from typing import List
from nltk.stem.porter import PorterStemmer


class Stemmer:
    def __init__(self, stemmer_instance=PorterStemmer()):
        self.stemmer = stemmer_instance

    def process(self, text: List[str]) -> List[str]:
        """Returns text with stemming applied.

        Parameters:
            text (List[str]): Input tokenized text.

        Returns:
            stemmed_text (List[str]): Input text with stemming applied.
        """
        stemmed_text = [self.stemmer(token) for token in text]
        return stemmed_text
