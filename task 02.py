def coincidence(lst=None, rng=None):
    if lst is None or rng is None:
        return []
    start, end = rng
    result = [x for x in lst if isinstance(x, (int, float)) and start <= x <= end]
    return result
print(coincidence([1, 2, 3, 4, 5], (2, 5)))
print(coincidence([1, "SNP", 3, "LOL", 5], (0, 4))) 