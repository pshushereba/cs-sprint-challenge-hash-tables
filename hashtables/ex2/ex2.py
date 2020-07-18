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
    route = []

    for ticket in tickets:
        hash_table[ticket.source] = ticket.destination
    
    sources = list(hash_table.keys())
    destinations = list(hash_table.values())

    for item in sources:
        if item == "None":
            route.append(item)
    
    
    print(route)
    return route