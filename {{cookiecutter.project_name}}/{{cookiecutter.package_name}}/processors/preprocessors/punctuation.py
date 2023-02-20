import string
from typing import List


class PunctuationRemoval:
    def __init__(self, punctuation_collection: set = set(string.punctuation)):
        """Replace with your own collection of punctuation if needed."""
        self.punctuation_collection = punctuation_collection

    def process(self, text: str) -> str:
        """Returns given text without punctuations.

        Parameters:
            text (str): Input string.

        Returns:
            punctuation_free_text (str): Input string without punctuations.
        """
        punctuation_free_text = "".join(
            [letter for letter in text if letter not in self.punctuation_collection]
        )
        return punctuation_free_text
