def arrayManipulation(n, queries):
    arr = [0]*n
    for i in queries:
        arr[i[0] - 1] += i[2]
        if i[1] != len(arr):
            arr[i[1]] -= i[2]
    max_value = 0
    itk = 0
    print(arr)
    for q in arr:
        itk += q
        if itk > max_value:
            max_value = itk
    return max_value
