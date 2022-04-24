import pytest
from longest_substring import LOLS


l =LOLS()


@pytest.mark.parametrize(
    "input,expected",
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("dasad", 3),
        ("jacu", 4),
        ("xxyzzfa", 3),
        ("", 0),
    ],
)
def test_length_of_longest_substring(input, expected):
    assert l.lengthOfLongestSubstring(input) == expected, "the function returned the wrong length of the longest substring"
