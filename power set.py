def power_set_iterative(seq):
    """Return list of all subsets of seq (as lists)."""
    result = [[]]
    for elem in seq:
        # For each existing subset, add a new subset that includes 'elem'
        result += [subset + [elem] for subset in result]
    return result

# Example
print(power_set_iterative([1, 2, 3]))
# Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
