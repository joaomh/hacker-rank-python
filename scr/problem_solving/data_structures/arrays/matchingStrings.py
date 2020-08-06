def matchingStrings(strings, queries):
    results = []
    for i in range(len(queries)):
        count = 0
        for j in range(len(strings)):
            if strings[j] == queries[i]:
               count += 1
        results.append(count)
    return results
