def slices(series, length):
    if length > len(series): raise ValueError('length > series length')
    if length <= 0: raise ValueError('length <= 0')
    if length == len(series): return [series]
    res = []
    for i in range(len(series) - (length - 1)):
        res.append(series[i: length + i])
    return res
        