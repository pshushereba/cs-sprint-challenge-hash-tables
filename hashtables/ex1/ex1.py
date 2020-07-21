def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    idx_arr = []
    num_pairs = {}
        
    for i in range(0, length):
        comp = limit - weights[i]
        if comp in num_pairs:
            if i != num_pairs[comp]:
                return [i, num_pairs[comp]]
        num_pairs[weights[i]] = i

    return None