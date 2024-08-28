from find_repeated_sequences import find_repeated_sequences
def test_find_repeated_sequences():
    expected = ["AAAAACCC","AAAACCCC","AAACCCCC"]
    expected.sort()
    result = find_repeated_sequences("AAAAACCCCCAAAAACCCCCC", 8)
    result.sort()
    assert len(result) == len(expected)
    assert result == expected
