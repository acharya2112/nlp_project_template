from typing import List, Union
from nltk.corpus import stopwords


class StopWordRemoval:
    def __init__(self, stopwords_list: Union[set, None] = None):
        if stopwords_list is None:
            # Note: Only contains stop words in lowercase format
            default_stopwords = set(stopwords.words("english"))
            self.stopwords_list = default_stopwords
        else:
            self.stopwords_list = stopwords_list

    def process(self, text: List[str]) -> List[str]:
        """Return tokenized text without stopwords.

        Note: Given text needs to be tokenized.

        Parameters:
            text (List[str]): Input tokenized text.

        Returns:
            filtered_text (List[str]): Input text without stopwords.
        """
        filtered_text = [token for token in text if token not in self.stopwords_list]
        return filtered_text
