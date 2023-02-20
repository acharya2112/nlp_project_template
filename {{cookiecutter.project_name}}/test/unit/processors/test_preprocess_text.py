import pytest
from typing import List

from pytest_lazyfixture import lazy_fixture
from processors.preprocess_text import get_default_preprocessor_pipeline


@pytest.fixture
def preprocessor_pipeline() -> List:
    return get_default_preprocessor_pipeline()


@pytest.mark.parametrize(
    "input_text, expected_text, fixture_pipeline",
    [
        (
            "This is what the default preprocessor pipeline filters out",
            "default preprocessor pipeline filter",
            lazy_fixture("preprocessor_pipeline"),
        ),
        (
            "Our sales figures have sky rocketed",
            "sale figure sky rocketed",
            lazy_fixture("preprocessor_pipeline"),
        ),
        (
            "I am running towards you",
            "running towards",
            lazy_fixture("preprocessor_pipeline"),
        ),
    ],
)
def test_get_default_preprocessor_pipeline(input_text, expected_text, fixture_pipeline):
    text = input_text
    for pipeline in fixture_pipeline:
        text = pipeline.process(text)

    result = " ".join(text)
    assert result == expected_text
