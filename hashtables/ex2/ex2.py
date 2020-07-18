#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    hash_table = {}
    route = [None] * length

    for ticket in tickets:
        hash_table[ticket.source] = ticket.destination
    
    sources = list(hash_table.keys())
    destinations = list(hash_table.values())

    route[0] = hash_table["NONE"]
    route[1] = hash_table[route[0]]

    if length > 2:
        for i in range(2, length):
            route[i] = hash_table[route[i-1]]
    
    print(route)
    return route