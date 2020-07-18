import math

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    hash_table = {}
    result = []

    for num in a:
        abs_val = abs(num)

        if hash_table.get(abs_val) is not None:
            result.append(abs_val)
        else:
            hash_table[abs_val] = abs_val
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
