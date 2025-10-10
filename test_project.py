import pytest
from unittest.mock import patch, MagicMock
from project import get_verse_text, verse_explain, truth_finder


@patch('google.generativeai.GenerativeModel')
def test_get_verse_text(mock_model):
    """Tests the get_verse_text function."""
    mock_response = MagicMock()
    mock_response.text = "For God so loved the world..."
    mock_model.return_value.generate_content.return_value = mock_response

    verse_reference = "John 3:16"
    result = get_verse_text(verse_reference)

    assert result == "For God so loved the world..."


@patch('google.generativeai.GenerativeModel')
def test_verse_explain(mock_model):
    """Tests the verse_explain function."""
    mock_response = MagicMock()
    mock_response.text = "This verse is about God's love..."
    mock_model.return_value.generate_content.return_value = mock_response

    verse_text = "For God so loved the world..."
    result = verse_explain(verse_text)

    assert result == "This verse is about God's love..."


@patch('google.generativeai.GenerativeModel')
def test_truth_finder(mock_model):
    """Tests the truth_finder function."""
    mock_response = MagicMock()
    mock_response.text = "True"
    mock_model.return_value.generate_content.return_value = mock_response

    verse_text = "For God so loved the world..."
    user_explanation = "This verse is about God's love for humanity."
    result = truth_finder(verse_text, user_explanation)

    assert result == "True"