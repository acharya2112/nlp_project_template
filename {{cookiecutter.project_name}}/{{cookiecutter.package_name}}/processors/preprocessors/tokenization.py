from nltk.tokenize import word_tokenize
from typing import List


class Tokenizer:
    def __init__(self, tokenizer_instance=word_tokenize):
        self.tokenizer = tokenizer_instance

    def process(self, text: str) -> List[str]:
        """Returns input text with tokenization applied.

        Parameters:
            text (str): A single string that needs to be broken into tokens.

        Returns:
            tokenized_text (List[str]): Input string converted into individual tokens.
        """
        tokenized_text = self.tokenizer(text)
        return tokenized_text
