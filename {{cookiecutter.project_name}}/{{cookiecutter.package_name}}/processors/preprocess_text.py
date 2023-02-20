from typing import List

from processors.preprocessors.lemmatization import Lemmatizer
from processors.preprocessors.lowercase import LowerCasing
from processors.preprocessors.punctuation import PunctuationRemoval
from processors.preprocessors.stopwordremoval import StopWordRemoval
from processors.preprocessors.tokenization import Tokenizer
from processors.preprocessors.whitespace import WhitespaceFilter


def get_default_preprocessor_pipeline() -> List:
    preprocessor_pipeline = [
        WhitespaceFilter(),
        LowerCasing(),
        PunctuationRemoval(),
        Tokenizer(),
        StopWordRemoval(),
        # Stemmer(),
        Lemmatizer(),
    ]

    return preprocessor_pipeline
