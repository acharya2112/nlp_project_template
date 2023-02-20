class LowerCasing:
    def __init__(self):
        """Do something here if you want a more customized lowercasing."""
        ...

    @staticmethod
    def process(text: str) -> str:
        """Return given text in lower case format

        Parameters:
            text (str): Input text.

        Return:
            lowercased_text (str): Input text converted to lower case.
        """
        lowercased_text = text.lower()
        return lowercased_text
