from sliding_window.find_repeated_sequences import find_repeated_sequences

def test_find_repeated_sequences_1():
    k = 8
    dna = "AAAAACCCCCAAAAACCCCCC"
    expected = ["AAAAACCC","AAAACCCC","AAACCCCC"]
    expected.sort()
    result = find_repeated_sequences(dna, k)
    result.sort()
    assert len(result) == len(expected)
    assert result == expected

def test_find_repeated_sequences_2():
    k = 1
    dna = "CGG"
    expected = ['G']
    expected.sort()
    result = find_repeated_sequences(dna,k)
    result.sort()
    assert len(result) == len(expected)
    assert result == expected
