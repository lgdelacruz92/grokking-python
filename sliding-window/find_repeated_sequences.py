def find_repeated_sequences(dna, k):

    # Replace this placeholder return statement with your code
    ans = set()
    record = set()
    for i in range(len(dna)-k):
        substr = dna[i:i+k]
        if substr in record:
            ans.add(substr)
        record.add(substr)
    return list(ans)