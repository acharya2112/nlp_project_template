import re


class WhitespaceFilter:
    def __init__(self):
        """Import library and assign here to do something more complex."""
        ...

    @staticmethod
    def process(text: str) -> str:
        """Returns given text stripped of whitespaces.

        Parameters:
            text (str): Input text.

        Returns:
            clean_text (str): Input text stripped of whitespaces.
        """
        clean_text = re.sub(" +", " ", text)
        return clean_text
